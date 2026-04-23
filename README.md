# Stock Screener

> Multi-strategy NSE signal generation with an AI interpretation layer.

A Streamlit-based screening engine for Nifty 500 equities that combines technical indicators with a configurable AI system prompt layer — so signals come with reasoning, not just numbers.

---

## What Makes This Different

Most screeners output a list of stocks that match rules. This one outputs stocks that match rules *and* explains why they matter, using an LLM system prompt trained on the specific strategy context.

## Strategies

| Strategy | Indicators Used |
|----------|----------------|
| Momentum Breakout | Price vs 52W high, volume surge, ATR expansion |
| VWAP Reclaim | Intraday VWAP cross with volume confirmation |
| RSI Oversold Bounce | RSI < 35, price at support, volume uptick |
| Moving Average Stack | 20/50/200 DMA alignment with trend confirmation |
| Volume Climax | Unusual volume with price reversal signal |

## Architecture

```
stockscreener/
├── app.py              # Streamlit UI + orchestration
├── indicators.py       # Technical indicator calculations
├── screener_engine.py  → signal generation (implied)
├── backtesting.py      # Basic strategy validation
├── nifty500_stocks.py  # Stock universe definition
├── system_prompt.py    # AI interpretation layer prompts
└── packages.txt        # System-level dependencies
```

## Setup

```bash
git clone https://github.com/rishabhinai-netizen/stockscreener
cd stockscreener
pip install -r requirements.txt
streamlit run app.py
```

---

*An earlier-stage tool in the NSE trading toolkit. See [RS-screener](https://github.com/rishabhinai-netizen/RS-screener) for the more complete implementation.*
