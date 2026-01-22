# Lists Parquet files
# Queries max timestamp for resume logic
# write partitioned parquet datasets
# state management

import os
import json # For state management - tracks last processed per timestamp
import pyarrow as pa # instead of pandas for efficient S#-native Parquet I/O
import pyarrow.parquet as pq
import pyarrow.dataset as ds
from pyarrow.fs import S3FileSystem
from datetime import datetime
import boto3
import yaml
from typing import Optional, Dict, List, Tuple
import logging

# Logging Setup
# timestamps - log levels - messages
logging.basicConfig(
    level=logging.INFO, # Only show INFO messages and above
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log Format: "2026-01-21 05:16:00 - INFO - Pipeline started"
)
logger = logging.getLogger(__name__)    # __name__ makes logs traceable to specific files


def load_config(config_path: str = 'data_pipeline/config/config.yaml') -> Dict:
    # Load YAML config
    # Centralizes params for reusability
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
    
# Create S3 filesystem to able pyarrow S3 access
def get_s3_fs(region: str) -> S3FileSystem:
    return S3FileSystem(region=region)

# Construct partitioned S3 path
# s3://btc-ml-data-bkt/bronze/timeframe=1h/year=2026/month=01/data.parquet
# for better querying
def s3_path(
    config: Dict,
    timeframe: str,
    year: int,
    month: int,
    ext: str = ''
) -> str:
    return f"s3://{config['aws']['bucket']}/bronze/timeframe={timeframe}/year={year}/month={month}/{ext}"

# query max(close_time) from existing parquet dataset with schema check
# Schema Discovery: Dynamically find 'close_time' column 
# Fallback: Use index 6 if unnamed in case of old binance CSV
def get_max_timestamp(
    config: Dict,
    timeframe: str,
    fs: S3FileSystem
) -> Optional[int]:
    bronze_path = f"s3://{config['aws']['bucket']}/bronze/timeframe={timeframe}"
    try:
        dataset = ds.dataset(bronze_path, filesystem=fs, format='parquet')
        if dataset.count_rows() == 0:
            logger.info(f"No data in {bronze_path}")
            return None
        
        # Schema discovery: Prefer named 'close_time' col or fallback to index [6]
        schema = dataset.schema
        close_time_col = None
        if 'close_time' in schema.names:
            close_time_col = 'close_time'
            logger.info(f"Found named column: {close_time_col}")
        else:
            # Fallback to the 6th column by default
            close_time_col = schema.field(6).name if len(schema) > 6 else None
            logger.info(f"Fallback to column 6: {close_time_col}")
            
        if close_time_col is None:
            raise ValueError("No 'close_time' column found (expected at index 6)")
        
        # metadata aggregate: No full table load
        ts_table = dataset.to_table(columns=[close_time_col])
        max_ts = ts_table.column(close_time_col).max().as_py()
        logger.info(f"Max {close_time_col} for {timeframe}: {datetime.fromtimestamp(max_ts/1000)} ({max_ts})")
        return int(max_ts)
    
    except Exception as e:
        logger.warning(f"Query error for {timeframe}: {e}. Starting from beginning.")
        return None
    
# Write PyArrow Table as partitioned Parquet dataset. Appends to existing data
def write_parquet(
    df: pa.Table,
    config: Dict,
    timeframe: str,
    year: int,
    month: int,
    fs: S3FileSystem
):
    path = s3_path(config, timeframe, year, month)
    pq.write_to_dataset(df, path, filesystem=fs, basename_template='data.parquet')
    logger.info(f"Wrote {df.num_rows} rows to {path}")
    
# Update State of this process in state.json with last processed timestamp per timeframe. Enables pause/resume
def update_state(config: Dict, timeframe: str, last_ts: int, fs: S3FileSystem):
    state_path = f"s3://{config['aws']['bucket']}/metadata/state.json"
    state = {}
    try:
        with fs.open_input_file(state_path) as f:
            state = json.load(f)
    except:
        pass # New state
    state[timeframe] = last_ts
    with fs.open_output_stream(state_path) as f:
        json.dump(state, f, indent=2)
    logger.info(f"Updated state for {timeframe}: {datetime.fromtimestamp(last_ts/1000)}")
    
if __name__ == "__main__":
    config = load_config()
    fs = get_s3_fs(config['aws']['region'])
    print("S3 utils OK:", config['aws']['bucket'])
    print("Max ts for 1hr:", get_max_timestamp(config, '1h', fs)) 