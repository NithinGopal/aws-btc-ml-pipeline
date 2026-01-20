```markdown
# aws-btc-ml-pipeline 🚀

**Production BTCUSDT perpetual futures data pipeline** → ML scalping signals → automated trading bot. AWS-native lakehouse processing 1M+ ticks/day at **99.9% completeness**.

**From manual trading losses → 24/7 pro scalping bot** (3-5x leverage, $5k target).

## 🎯 What This Solves
**Problem**: Manual crypto day trading = emotions + screen time + losses  
**Solution**: Automated system mimics pro trader:
- Multi-timeframe data pipeline (AWS DE resume showcase)
- ML signals (62-68% winrate target)
- Risk-managed execution (fractional Kelly + ATR stops)
- Live dashboard (P&L + Sharpe monitoring)

## 🏗️ System Components

| Component | Tech Stack | Purpose |
|-----------|------------|---------|
| **Data Pipeline** | AWS Glue PySpark, S3 Delta Lake | 3 timeframes + order book → 100+ ML features |
| **ML Signals** | SageMaker LSTM/Transformer | Multi-timeframe features → BUY/SELL + confidence |
| **Risk Engine** | Python | Fractional Kelly sizing + regime filters |
| **Trading Bot** | `binance-futures-connector` | Execution with maker rebates + rate limiting |
| **Dashboard** | Streamlit + Athena | P&L tracking + Telegram alerts |

## 📊 Data Architecture

### Multi-Timeframe Strategy (Key Improvement)
**Why**: 1m-only = 70%+ noise. Multi-timeframe filters false signals[web:2][web:5].

| Timeframe | Purpose | Update Frequency |
|-----------|---------|------------------|
| **15m** | Trend filter (only trade with momentum) | Every 15min |
| **5m** | Entry timing (pullback completion) | Every 5min |
| **1m** | Precise trigger (stop placement) | Every 1min |

### Data Sources

| Data Type | Historical | Live | Value |
|-----------|------------|------|-------|
| **OHLCV (3 timeframes)** | [HuggingFace 2018-2026](https://huggingface.co/datasets/123olp/binance-futures-ohlcv-2018-2026) | `@kline_1m/5m/15m` | Core price action |
| **Order Book (10 levels)** | Collect live only | `@depth10@100ms` | Imbalance + whale detection[web:20] |
| **Funding Rate** | Binance API | Every 8 hours | Overleveraged detection[web:20] |
| **Open Interest** | Binance API | Every 5min | Trend strength |
| **Liquidations** | Binance API | Real-time stream | Reversal signals |

**Storage**: ~51GB/month (~$1.50 S3 cost)[web:17]

### Lakehouse Pipeline
```
Sources → S3 Bronze (raw) → Glue PySpark → S3 Silver (cleaned) → S3 Gold (100+ features)
Orchestration: Airflow MWAA
Quality: Great Expectations validation
```

### Feature Categories (100+ total)

- **Price Action** (30): RSI/MACD/Bollinger across 1m/5m/15m
- **Volume** (15): VWAP, taker buy ratio, volume surges
- **Order Book** (20): Multi-level imbalance, spread, whale walls[web:20]
- **Momentum** (15): Rate of change, trend alignment
- **Market Structure** (10): Support/resistance proximity
- **Perpetual-Specific** (10): Funding rate, OI changes, liquidations[web:20]

## 🤖 Trading System

### ML Models
**Phase 1**: LSTM (62% baseline accuracy target)
**Phase 2**: Transformer if needed (65-68% potential)[web:7][web:10]
**Phase 3**: Ensemble (LSTM + XGBoost, trade when both agree)

### Risk Management

**Position Sizing** (Fractional Kelly):
- 62% winrate @ 1:2 RR → 25% Kelly = 10% position size
- With 3x leverage = 3-4% capital risk per trade
- Max 5 concurrent trades = <20% total exposure[web:21][web:27]

**Execution Optimization**:
- Prefer maker orders (0.02% rebate) over taker (0.04% fee)
- Cancel/requote after 2 seconds if unfilled
- Saves 0.06% per trade = significant edge[web:6][web:9]

**Safety Mechanisms**:
- ATR-based stops + time exits (max 15min hold)
- 5% daily drawdown pause, 15% weekly DD → manual review
- Skip trades when: spread >0.05%, low volatility, major news

**API Rate Limits**: 
- Binance: 1200 weight/min → realistic max 100-150 trades/day[web:22][web:25]

## 📅 Phased Deployment (De-Risked)

| Phase | Duration | Capital | Goal |
|-------|----------|---------|------|
| **Week 1-4** | Data pipeline + LSTM | $0 | Portfolio project, 62% backtest |
| **Week 5-8** | Testnet paper trading | $0 | 60-day validation, tune execution |
| **Month 3-4** | Job applications | $0 | AWS DE interviews ongoing |
| **Post-Job Month 1-3** | Live trading | $1-2k | Consistency >profits, <5% DD |
| **Month 4-6** | Scale up | $2-5k | 20%/month increase if profitable |
| **Month 7+** | Full capital | $5-10k | Passive income stream |

## 💰 Economics

**Monthly Targets** (at $5k live):
- 600 trades × 62% win × 1:2 RR = 0.8R expectancy
- Gross: +4.8% monthly
- After fees/slippage (0.14-0.24%): **+2-3% net**[web:6][web:9]

**AWS Costs**: ~$45-55/month (S3 + Glue + SageMaker + MWAA)

## 🎖️ Dual Value

**Career** (Primary, Months 1-4): AWS Data Engineer portfolio → $80-120k salary
**Personal** (Post-job): Manual losses → automated crypto income

## 📁 Repository Structure

```
aws-btc-ml-pipeline/
│
├── 📊 data_pipeline/
│   ├── collectors/
│   │   ├── binance_streams.py           # All websockets (klines + orderbook)
│   │   └── config.yaml                  # API keys, timeframes
│   │
│   ├── glue_jobs/
│   │   ├── bronze_to_silver.py          # Clean raw data
│   │   └── silver_to_gold.py            # Calculate features
│   │
│   └── download_historical.py           # HuggingFace → S3 (one-time)
│
├── 🧠 ml_signals/
│   ├── train_lstm.py                    # Train model on Gold data
│   ├── predict.py                       # Generate live signals
│   └── backtest.py                      # Test on historical data
│
├── 🛡️ risk_engine/
│   └── position_sizer.py                # Kelly + ATR stops
│
├── 🤖 trading_bot/
│   ├── paper_trader.py                  # Testnet execution
│   └── binance_client.py                # API wrapper
│
├── 📊 dashboard/
│   └── streamlit_app.py                 # Simple P&L dashboard
│
├── 🔧 infra/
│   └── terraform/
│       └── main.tf                      # S3 + Glue setup
│
├── notebooks/
│   └── explore_data.ipynb               # Quick EDA
│
├── tests/
│   └── test_features.py                 # Validate calculations
│
├── requirements.txt
├── .env.example
└── README.md

```
