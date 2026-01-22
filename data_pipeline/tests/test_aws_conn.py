import os
import boto3
from dotenv import load_dotenv

# Test AWS S3 Connection
def test_aws_conn():
    # Load .env variables
    load_dotenv()
    
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    region = os.getenv("AWS_DEFAULT_REGION")
    bucket_name = os.getenv("AWS_S3_BUCKET_NAME")
    
    print("Testing AWS Connection")
    print(f"Region: {region}")
    print(f"S3 Bucket: {bucket_name}")
    
    try:
        # Create S3 Client
        s3 = boto3.client(
            "s3",
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key,
            region_name = region
        )
        
        # List all the buckets available in s3
        buckets = s3.list_buckets()
        print(f"Connected! You have {len(buckets["Buckets"])} S3 Buckets")
        
        # Check if our bucket exists
        if s3.head_bucket(Bucket=bucket_name):
            print(f"{bucket_name} exists!")
        else:
            print(f"{bucket_name} DOES NOT EXIST")
        
        # List bronze to check existing data
        resp = s3.list_objects_v2(Bucket=bucket_name, Prefix='bronze/')
        if resp.get('Contents'):
            print("Existing bronze data found.")
        else:
            print("No bronze data yet - Ready for backfill.")
        
        return True
        
    except Exception as e:
        print(f"Connection Failed: {e}")
        print("Check your .env file and AWS Credentials")
        return False
    
if __name__ == "__main__":
    test_aws_conn()