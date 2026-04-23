# Stock Screener

**AI-powered NSE stock screener with technical analysis and strategy signals.**

A Streamlit-based screener for Indian equities that combines technical indicators with an AI system prompt layer for intelligent signal generation across the Nifty 500 universe.

---

## Features

- Multi-strategy signal generation across Nifty 500
- Technical indicators: RSI, VWAP, moving averages, volume analysis
- Backtesting engine for strategy validation
- AI-powered insights via configurable system prompts
- Interactive charts and filtering

---

## Setup

```bash
pip install -r requirements.txt
# Install system dependencies
cat packages.txt | xargs apt-get install -y
streamlit run app.py
```

---

## Tech Stack

- **Streamlit** — Web interface
- **yfinance** — Market data
- **Pandas / NumPy** — Technical analysis
- **Plotly** — Charting

---

## Built By

Rishabh Inai — NSE trader and fraud investigator.
