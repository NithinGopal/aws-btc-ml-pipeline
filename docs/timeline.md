# BTC Scalping Bot Project Timeline: 4 Weeks to Live Trading

**Simple roadmap**—each day builds the next piece. **Week 1 = resume-ready**, Week 4 = money-making bot.

## 📅 **Week 1: Data Pipeline (Foundation)**
*Purpose: Get pro-level BTC data flowing 24/7 → powers everything else*

| Day | Task | Why Important | Deliverable |
|-----|------|--------------|-------------|
| **Day 1** | Download historical data | **No data = no trading**—5GB BTC 1min ready | `data_pipeline/datasets/` folder |
| **Day 2** | AWS S3 lakehouse setup | **Storage backbone** for all components | Buckets + IAM live |
| **Day 3** | Bronze layer (raw data) | **Archive everything**—never lose ticks | S3 bronze bucket populated |
| **Day 4** | Airflow daily updates | **Keeps data fresh** automatically | First incremental run success |
| **Day 5** | Glue PySpark ETL | **Turns raw → gold** (RSI/MACD magic) | Gold lake with 15+ features |
| **Day 6** | Completeness dashboard | **Prove 99.9% reliability** to recruiters | Streamlit app live |
| **Day 7** | GitHub + resume screenshots | **Portfolio piece complete** | Repo live, LinkedIn post-ready |

**Week 1 Win**: "AWS BTC pipeline, 1M ticks/day"—interview bullet done.

## 📈 **Week 2: ML Signals (Prediction Engine)**
*Purpose: Data → "BUY/SELL" decisions → bot knows what to trade*

| Day | Task | Why Important | Deliverable |
|-----|------|--------------|-------------|
| **Day 8** | Feature engineering | **Raw numbers → trade signals** (60 features) | Feature store ready |
| **Day 9** | LSTM model training | **Learns winning patterns** from history | 62% accuracy backtest |
| **Day 10** | Model deployment | **Live predictions** (<100ms) | SageMaker endpoint |
| **Day 11** | Signal validation | **Test predictions → paper P&L** | Signal accuracy dashboard |
| **Day 12** | Daily retraining pipeline | **Model stays fresh** with new data | Automated ML refresh |
| **Day 13** | Signal quality tests | **Only good signals go live** | 60%+ threshold confirmed |
| **Day 14** | GitHub Week 2 merge | **ML portfolio piece** | `ml_scalping_signals/` live |

**Week 2 Win**: Bot now "thinks" like pro trader (BUY/SELL calls).

## 🛡️ **Week 3: Risk + Paper Trading (Safety First)**
*Purpose: Smart money management → survive losses → compound wins*

| Day | Task | Why Important | Deliverable |
|-----|------|--------------|-------------|
| **Day 15** | Kelly position sizing | **Optimal bet size** (math beats gut) | Risk calculator |
| **Day 16** | Stop-loss logic | **Cut losses quick** (1:2 risk/reward) | ATR-based exits |
| **Day 17** | Paper trading bot | **Testnet proof**—no real money risk | Binance testnet live |
| **Day 18** | Leverage management | **5x safe sizing** (no liquidation) | Position limits |
| **Day 19** | Circuit breakers | **Pause on 5% loss** → protect capital | Auto-pause logic |
| **Day 20** | 1-week paper backtest | **Prove system works** (Sharpe >1.5) | P&L report |
| **Day 21** | GitHub Week 3 merge | **Risk-managed system** | `risk_engine/` + `trading_bot/paper/` |

**Week 3 Win**: Bot trades fake money → real profits proven.

## 💰 **Week 4: Live Trading + Dashboard (Money Time)**
*Purpose: $5k live → daily P&L → scale to pro levels*

| Day | Task | Why Important | Deliverable |
|-----|------|--------------|-------------|
| **Day 22** | Live bot switch | **Real money starts** ($5k deposit) | Binance live API |
| **Day 23** | Dashboard build | **Live P&L tracking** + alerts | Streamlit production |
| **Day 24** | Monitoring setup | **99.95% uptime** + error alerts | CloudWatch + Telegram |
| **Day 25** | First week live review | **Tune based on reality** | Performance report |
| **Day 26** | Tax/compliance | **India crypto tax** ready | P&L export |
| **Day 27** | Scale-up plan | **Add pairs, optimize** | Multi-symbol ready |
| **Day 28** | Full GitHub release | **Portfolio complete** | v1.0 tag + demo video |

**Week 4 Win**: Bot live trading your account → passive income.

## 📊 **Milestone Checklist**
```
☐ Week 1: [ ] Data pipeline live (99.9%) → LinkedIn post
☐ Week 2: [ ] ML 62% accuracy → Recruiter demo  
☐ Week 3: [ ] Paper +3% → Confidence boost
☐ Week 4: [ ] Live $5k → "I built a trading bot"
```

## 🎯 **Big Picture Progress**
```
End Week 1: Data pro (DE resume done)
End Week 2: Bot thinks (ML skills shown)
End Week 3: Bot trades safely (risk mastery)
End Week 4: Money flows (full-stack trader)
```

**Daily 2-3hr commits** → **live bot by Feb 16**. **Day 1 download command ready?** Daily check-ins keep momentum.