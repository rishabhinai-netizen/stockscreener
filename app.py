"""
MULTI-AGENT TRADING SYSTEM v6.1 - UPDATED
========================================
UPDATES:
1. DeepSeek API Fallback added
2. Robust Error Handling for Stock Data
3. Enhanced "Price Action Sentiment" (Volume/Relative Strength)
4. Hiding Streamlit Headers/Footers
"""

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
import google.generativeai as genai
from typing import Dict, List, Optional, Any
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
from openai import OpenAI  # Added for DeepSeek
warnings.filterwarnings('ignore')

from nifty500_stocks import NIFTY_500_STOCKS, get_all_stocks, get_all_sectors, search_stocks
from indicators import calculate_all_metrics, calculate_rsi, calculate_macd, calculate_bollinger_bands
from backtesting import BacktestEngine, AVAILABLE_STRATEGIES
from system_prompt import SYSTEM_INSTRUCTION

# =============================================================================
# CONFIG
# =============================================================================
AVAILABLE_MODELS = {
    "gemini-2.0-flash": "Gemini 2.0 Flash (Recommended)",
    "gemini-2.5-flash": "Gemini 2.5 Flash (Latest)",
}

def get_api_key(key_name):
    try:
        if hasattr(st, 'secrets') and key_name in st.secrets:
            return st.secrets[key_name]
    except:
        pass
    return st.session_state.get(key_name.lower(), '')

st.set_page_config(page_title="Trading System", page_icon="🤖", layout="wide")

# =============================================================================
# CSS - Hiding Footers and Headers
# =============================================================================
st.markdown("""
<style>
    @media (max-width: 768px) {
        .main .block-container { padding: 1rem; }
    }
    
    .main-header {
        font-size: 2rem;
        font-weight: bold;
        background: linear-gradient(120deg, #00d4ff, #7b2cbf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 0.5rem 0;
    }
    
    .regime-banner {
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
        color: white;
    }
    .regime-stress { background: linear-gradient(135deg, #ff416c, #ff4b2b); }
    .regime-accumulate { background: linear-gradient(135deg, #667eea, #764ba2); }
    .regime-trend { background: linear-gradient(135deg, #11998e, #38ef7d); }
    .regime-goldilocks { background: linear-gradient(135deg, #f093fb, #f5576c); }
    .regime-unknown { background: linear-gradient(135deg, #bdc3c7, #2c3e50); }
    
    .sentiment-card {
        padding: 12px;
        margin: 8px 0;
        border-radius: 8px;
        border-left: 4px solid #9e9e9e;
        background: #f5f5f5;
    }
    .sentiment-bullish { border-left-color: #4caf50; background: #e8f5e9; }
    .sentiment-bearish { border-left-color: #f44336; background: #ffebee; }
    .sentiment-neutral { border-left-color: #ff9800; background: #fff3e0; }
    
    .result-card {
        padding: 12px;
        margin: 8px 0;
        border-radius: 8px;
        border-left: 4px solid #ccc;
        background: #fafafa;
    }
    .result-buy { border-left-color: #4caf50; }
    .result-sell { border-left-color: #f44336; }
    .result-hold { border-left-color: #ff9800; }
    
    /* HIDE STREAMLIT ELEMENTS */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stHeader"] {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Session state
for key in ['watchlist', 'backtest_results', 'google_api_key', 'deepseek_api_key', 'selected_model', 'screener_results', 'agentic_backtest']:
    if key not in st.session_state:
        st.session_state[key] = [] if key in ['watchlist', 'backtest_results'] else (None if 'key' not in key else "")
if 'selected_model' not in st.session_state:
    st.session_state.selected_model = "gemini-2.0-flash"

# =============================================================================
# MARKET DATA
# =============================================================================
@st.cache_data(ttl=300)
def fetch_market_regime_data() -> Dict[str, Any]:
    """Fetch market-wide data for regime classification."""
    data = {
        'india_vix': None,
        'nifty_change': None,
        'market_breadth': None,
        'nifty_level': None
    }
    
    try:
        # India VIX
        vix = yf.Ticker("^INDIAVIX")
        vix_hist = vix.history(period="5d")
        if not vix_hist.empty:
            data['india_vix'] = round(vix_hist['Close'].iloc[-1], 2)
        
        # Nifty 50
        nifty = yf.Ticker("^NSEI")
        nifty_hist = nifty.history(period="5d")
        if not nifty_hist.empty:
            data['nifty_level'] = round(nifty_hist['Close'].iloc[-1], 2)
            if len(nifty_hist) >= 2:
                data['nifty_change'] = round(
                    ((nifty_hist['Close'].iloc[-1] / nifty_hist['Close'].iloc[-2]) - 1) * 100, 2
                )
        
        # Market breadth from Nifty 50 components
        advances = 0
        declines = 0
        sample = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS',
                 'SBIN.NS', 'BHARTIARTL.NS', 'ITC.NS', 'KOTAKBANK.NS', 'LT.NS',
                 'HINDUNILVR.NS', 'BAJFINANCE.NS', 'AXISBANK.NS', 'MARUTI.NS', 'TITAN.NS']
        
        for ticker in sample:
            try:
                hist = yf.Ticker(ticker).history(period="2d")
                if len(hist) >= 2:
                    if hist['Close'].iloc[-1] > hist['Close'].iloc[-2]:
                        advances += 1
                    else:
                        declines += 1
            except:
                pass
        
        if advances + declines > 0:
            data['market_breadth'] = round(advances / (advances + declines), 2)
            data['advances'] = advances
            data['declines'] = declines
            
    except Exception as e:
        pass
    
    return data

def classify_regime(data: Dict) -> Dict:
    """Classify market regime with full details."""
    vix = data.get('india_vix')
    breadth = data.get('market_breadth', 0.5)
    
    if vix is None:
        return {
            'regime': 'UNKNOWN',
            'code': 'UNKNOWN', 
            'confidence': 0,
            'description': 'Unable to fetch VIX data',
            'strategy': 'Wait for data',
            'vix': 'N/A',
            'breadth': breadth
        }
    
    if vix > 22:
        regime = {
            'regime': 'LIQUIDITY VACUUM',
            'code': 'STRESS',
            'confidence': min(95, 70 + (vix - 22) * 2),
            'description': 'High fear environment - Risk-off mode',
            'strategy': 'Reduce exposure, hedge positions, increase cash to 60-70%',
            'atlas_weight': 10,
            'oracle_weight': 20,
            'sentinel_weight': 70
        }
    elif vix < 13:
        regime = {
            'regime': 'COMPRESSION',
            'code': 'ACCUMULATE',
            'confidence': min(90, 65 + (13 - vix) * 3),
            'description': 'Low volatility - Market coiling for breakout',
            'strategy': 'Prepare for breakout, mean-reversion trades, cash 40-50%',
            'atlas_weight': 25,
            'oracle_weight': 35,
            'sentinel_weight': 40
        }
    elif 14 <= vix <= 19 and breadth and breadth > 0.6:
        regime = {
            'regime': 'MOMENTUM CASCADE',
            'code': 'TREND',
            'confidence': 75,
            'description': 'Strong directional trend in progress',
            'strategy': 'Follow momentum, trail stops, cash 20-30%',
            'atlas_weight': 50,
            'oracle_weight': 20,
            'sentinel_weight': 30
        }
    elif 13 <= vix <= 17 and breadth and 0.4 <= breadth <= 0.6:
        regime = {
            'regime': 'LIQUIDITY DRIFT',
            'code': 'GOLDILOCKS',
            'confidence': 70,
            'description': 'Optimal conditions for alpha generation',
            'strategy': 'Active trading, balanced exposure, cash 25-35%',
            'atlas_weight': 35,
            'oracle_weight': 40,
            'sentinel_weight': 25
        }
    else:
        regime = {
            'regime': 'REGIME TRANSITION',
            'code': 'UNCERTAINTY',
            'confidence': 55,
            'description': 'Mixed signals - Transition period',
            'strategy': 'Reduce position sizes, wait for clarity, cash 50%',
            'atlas_weight': 20,
            'oracle_weight': 30,
            'sentinel_weight': 50
        }
    
    regime['vix'] = vix
    regime['breadth'] = breadth
    regime['nifty_level'] = data.get('nifty_level', 'N/A')
    regime['nifty_change'] = data.get('nifty_change', 0)
    
    return regime

# =============================================================================
# PRICE ACTION SENTIMENT (IMPROVED)
# =============================================================================
def calculate_price_sentiment(df: pd.DataFrame, metrics: Dict) -> Dict:
    """Calculate sentiment from price action - Improved with Volume/Relative Strength."""
    
    sentiment = {
        'overall': 'NEUTRAL',
        'score': 0,
        'factors': []
    }
    
    score = 0
    factors = []
    
    # 1. Volume Analysis (True Institutional Interest)
    vol_ratio = metrics.get('volume_ratio', 1.0)
    price_change = metrics.get('price_change_1d', 0)
    
    if vol_ratio > 1.5 and price_change > 0:
        score += 2
        factors.append(f"Strong Institutional Buying (Vol {vol_ratio:.1f}x) (+2)")
    elif vol_ratio > 1.5 and price_change < 0:
        score -= 2
        factors.append(f"Strong Institutional Selling (Vol {vol_ratio:.1f}x) (-2)")
    
    # 2. Relative Strength (vs Simple Benchmark Logic)
    # If stock is near 52w high while market (Nifty) is not, that's relative strength
    pct_high = metrics.get('pct_from_52w_high', -100)
    if pct_high > -5:
        score += 2
        factors.append(f"High Relative Strength (Near 52W High) (+2)")
    elif pct_high < -30:
        score -= 1
        factors.append(f"Relative Weakness (Deep in drawdown) (-1)")

    # 3. Delivery/Trend Confirmation
    if metrics.get('trend_medium_term') == 'BULLISH':
        score += 1
        factors.append("Medium-term Trend Alignment (+1)")
    
    # 4. RSI Context (Avoid pure double counting of Atlas)
    rsi = metrics.get('rsi_14', 50)
    if rsi < 30:
        score += 1
        factors.append("Contrarian Value: Deep Oversold (+1)") # Fundamental view sees value
    
    # Determine overall sentiment
    if score >= 3:
        sentiment['overall'] = 'STRONGLY BULLISH'
    elif score >= 1:
        sentiment['overall'] = 'BULLISH'
    elif score <= -3:
        sentiment['overall'] = 'STRONGLY BEARISH'
    elif score <= -1:
        sentiment['overall'] = 'BEARISH'
    else:
        sentiment['overall'] = 'NEUTRAL'
    
    sentiment['score'] = score
    sentiment['factors'] = factors
    
    return sentiment

# =============================================================================
# DATA FUNCTIONS
# =============================================================================
@st.cache_data(ttl=300)
def fetch_stock_data(ticker: str, period: str = "1y"):
    """Fetch stock data with robust validation."""
    try:
        data = yf.Ticker(ticker).history(period=period)
        if data.empty:
            return None
        return data
    except:
        return None

# =============================================================================
# UNIFIED AI ANALYSIS
# =============================================================================
def get_unified_recommendation(metrics: Dict, regime: Dict, sentiment: Dict) -> Dict:
    """Generate consistent recommendation based on rules."""
    
    # Initialize scores
    atlas_signal = 'HOLD'
    atlas_confidence = 50
    oracle_signal = 'HOLD'
    oracle_confidence = 50
    sentinel_signal = 'MEDIUM'
    
    # ATLAS (Technical) Analysis
    rsi = metrics.get('rsi_14', 50)
    trend = metrics.get('trend_short_term', 'NEUTRAL')
    price_vs_sma = metrics.get('price_vs_sma20_pct', 0)
    macd = metrics.get('macd_status', 'NEUTRAL')
    
    atlas_score = 0
    
    if rsi and rsi < 30: atlas_score += 2
    elif rsi and rsi > 70: atlas_score -= 2
    
    if trend == 'BULLISH': atlas_score += 1
    elif trend == 'BEARISH': atlas_score -= 1
    
    if macd == 'BULLISH': atlas_score += 1
    elif macd == 'BEARISH': atlas_score -= 1
    
    if price_vs_sma > 2: atlas_score += 1
    elif price_vs_sma < -2: atlas_score -= 1
    
    if atlas_score >= 2:
        atlas_signal = 'BUY'
        atlas_confidence = min(80, 50 + atlas_score * 10)
    elif atlas_score <= -2:
        atlas_signal = 'SELL'
        atlas_confidence = min(80, 50 + abs(atlas_score) * 10)
    
    # ORACLE (Fundamental/Sentiment) Analysis
    sentiment_score = sentiment.get('score', 0)
    
    if sentiment_score >= 2:
        oracle_signal = 'BUY'
        oracle_confidence = min(75, 50 + sentiment_score * 8)
    elif sentiment_score <= -2:
        oracle_signal = 'SELL'
        oracle_confidence = min(75, 50 + abs(sentiment_score) * 8)
    
    # SENTINEL (Risk) Analysis
    volatility = metrics.get('realized_volatility_20d', 20)
    pct_from_high = abs(metrics.get('pct_from_52w_high', 0))
    
    risk_score = 0
    if volatility and volatility > 30: risk_score += 2
    if rsi and (rsi > 75 or rsi < 25): risk_score += 1
    if pct_from_high < 5: risk_score += 1
    
    if risk_score >= 3: sentinel_signal = 'HIGH'
    elif risk_score >= 1: sentinel_signal = 'MEDIUM'
    else: sentinel_signal = 'LOW'
    
    # Calculate weighted final decision
    atlas_weight = regime.get('atlas_weight', 33) / 100
    oracle_weight = regime.get('oracle_weight', 33) / 100
    sentinel_weight = regime.get('sentinel_weight', 34) / 100
    
    signal_scores = {'BUY': 1, 'HOLD': 0, 'SELL': -1}
    risk_modifier = {'LOW': 1.0, 'MEDIUM': 0.7, 'HIGH': 0.4}
    
    weighted_score = (
        signal_scores.get(atlas_signal, 0) * atlas_weight +
        signal_scores.get(oracle_signal, 0) * oracle_weight
    ) * risk_modifier.get(sentinel_signal, 0.7)
    
    if weighted_score >= 0.4: final = 'STRONG BUY'
    elif weighted_score >= 0.15: final = 'BUY'
    elif weighted_score <= -0.4: final = 'STRONG SELL'
    elif weighted_score <= -0.15: final = 'SELL'
    else: final = 'HOLD'
    
    return {
        'atlas_signal': atlas_signal,
        'atlas_confidence': atlas_confidence,
        'oracle_signal': oracle_signal,
        'oracle_confidence': oracle_confidence,
        'sentinel_risk': sentinel_signal,
        'weighted_score': round(weighted_score, 3),
        'final_recommendation': final,
        'trend': trend
    }

# =============================================================================
# AI DETAILED ANALYSIS - WITH DEEPSEEK FALLBACK
# =============================================================================
def run_detailed_analysis(google_key: str, deepseek_key: str, model_name: str, ticker: str, metrics: Dict, 
                          regime: Dict, sentiment: Dict, recommendation: Dict) -> str:
    """Run detailed AI analysis with DeepSeek Fallback."""
    
    prompt = f"""
Analyze {ticker} using the Multi-Agent Swarm Decision Engine.

═══════════════════════════════════════════════════════════════
MARKET REGIME DATA (REAL-TIME):
═══════════════════════════════════════════════════════════════
- India VIX: {regime.get('vix', 'N/A')}
- Nifty 50 Level: {regime.get('nifty_level', 'N/A')}
- Market Breadth: {regime.get('breadth', 'N/A')}
- Detected Regime: {regime.get('regime', 'UNKNOWN')}
- Recommended Strategy: {regime.get('strategy', 'N/A')}

Agent Weights:
- ATLAS: {regime.get('atlas_weight', 33)}%
- ORACLE: {regime.get('oracle_weight', 33)}%
- SENTINEL: {regime.get('sentinel_weight', 34)}%

═══════════════════════════════════════════════════════════════
STOCK DATA:
═══════════════════════════════════════════════════════════════
- Price: ₹{metrics.get('current_price', 0):,.2f} ({metrics.get('price_change_1d', 0):+.2f}%)
- RSI (14): {metrics.get('rsi_14', 'N/A')}
- Volume Ratio: {metrics.get('volume_ratio', 0):.2f}x
- 52W High: {metrics.get('pct_from_52w_high', 0):+.1f}% from high
- Volatility: {metrics.get('realized_volatility_20d', 0):.1f}%

═══════════════════════════════════════════════════════════════
SENTIMENT (Price Action):
═══════════════════════════════════════════════════════════════
- Score: {sentiment.get('score', 0)}
- Factors: {', '.join(sentiment.get('factors', []))}

═══════════════════════════════════════════════════════════════
RECOMMENDATION:
═══════════════════════════════════════════════════════════════
- ATLAS: {recommendation.get('atlas_signal')}
- ORACLE: {recommendation.get('oracle_signal')}
- SENTINEL: {recommendation.get('sentinel_risk')}
- Final: {recommendation.get('final_recommendation')}

Generate a detailed Multi-Agent report with:
1. MARKET REGIME
2. AGENT ANALYSIS (ATLAS, ORACLE, SENTINEL)
3. DEBATE
4. FINAL CONSENSUS (Entry, Stop, Target)
"""
    
    # 1. Try Google Gemini
    try:
        genai.configure(api_key=google_key)
        model = genai.GenerativeModel(model_name=model_name, system_instruction=SYSTEM_INSTRUCTION)
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        error_str = str(e).lower()
        # Check for Quota/Rate Limit errors
        if "429" in error_str or "resource" in error_str or "quota" in error_str:
            st.warning("⚠️ Gemini Limit Reached. Switching to DeepSeek...")
            
            # 2. Fallback to DeepSeek
            if not deepseek_key:
                return f"⚠️ Gemini Quota Exhausted and no DeepSeek Key provided. Gemini Error: {str(e)}"
            
            try:
                client = OpenAI(
                    api_key=deepseek_key,
                    base_url="https://api.deepseek.com"
                )
                
                response = client.chat.completions.create(
                    model="deepseek-chat", 
                    messages=[
                        {"role": "system", "content": SYSTEM_INSTRUCTION},
                        {"role": "user", "content": prompt},
                    ],
                    stream=False
                )
                return response.choices[0].message.content
                
            except Exception as ds_e:
                return f"❌ Both APIs failed. Gemini: {str(e)} | DeepSeek: {str(ds_e)}"
        else:
            return f"❌ Analysis Error: {str(e)}"

# =============================================================================
# CHARTS
# =============================================================================
def create_chart(df, ticker):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.08,
                        row_heights=[0.7, 0.3])
    
    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'],
                                  low=df['Low'], close=df['Close'], name='Price'), row=1, col=1)
    
    sma20 = df['Close'].rolling(20).mean()
    fig.add_trace(go.Scatter(x=df.index, y=sma20, name='SMA20', line=dict(color='orange', width=1)), row=1, col=1)
    
    colors = ['#ef5350' if df['Close'].iloc[i] < df['Open'].iloc[i] else '#26a69a' for i in range(len(df))]
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume', marker_color=colors), row=2, col=1)
    
    fig.update_layout(height=450, template='plotly_dark', xaxis_rangeslider_visible=False,
                      margin=dict(l=0, r=0, t=30, b=0), showlegend=False)
    return fig

# =============================================================================
# MAIN APP
# =============================================================================
def main():
    st.markdown('<p class="main-header">🤖 Multi-Agent Trading System</p>', unsafe_allow_html=True)
    
    regime_data = fetch_market_regime_data()
    regime = classify_regime(regime_data)
    
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # KEY MANAGEMENT
        try:
            if 'GOOGLE_API_KEY' in st.secrets:
                st.success("✅ Google Key loaded")
            if 'DEEPSEEK_API_KEY' in st.secrets:
                st.success("✅ DeepSeek Key loaded")
        except:
            pass

        if 'GOOGLE_API_KEY' not in st.secrets:
            st.session_state.google_api_key = st.text_input("Google API Key", type="password", value=st.session_state.google_api_key)
        
        if 'DEEPSEEK_API_KEY' not in st.secrets:
            st.session_state.deepseek_api_key = st.text_input("DeepSeek API Key (Fallback)", type="password", value=st.session_state.deepseek_api_key)
        
        st.session_state.selected_model = st.selectbox(
            "Model", list(AVAILABLE_MODELS.keys()),
            format_func=lambda x: AVAILABLE_MODELS[x]
        )
        
        st.divider()
        page = st.radio("Navigation", ["🎯 AI Analysis", "🔍 AI Screener", "📈 Backtesting", "🤖 Agentic Backtest", "⭐ Watchlist", "ℹ️ Help"])
        
        st.divider()
        st.markdown(f"**Regime:** {regime.get('regime', 'UNKNOWN')}")
        st.caption(f"VIX: {regime.get('vix', 'N/A')}")

    google_key = get_api_key('GOOGLE_API_KEY')
    deepseek_key = get_api_key('DEEPSEEK_API_KEY')

    # ==========================================================================
    # PAGE LOGIC
    # ==========================================================================
    if page == "🎯 AI Analysis":
        st.header("🎯 AI Analysis")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            cat = st.selectbox("Category", ["All"] + list(NIFTY_500_STOCKS.keys()))
            stocks = get_all_stocks() if cat == "All" else NIFTY_500_STOCKS.get(cat, [])
            opts = [(s['symbol'], f"{s['symbol'].replace('.NS','')} - {s['name']}") for s in stocks]
            selected = st.selectbox("Stock", [o[0] for o in opts],
                                   format_func=lambda x: next((o[1] for o in opts if o[0]==x), x))
        with col2:
            period = st.selectbox("Period", ["3mo", "6mo", "1y"], index=1)
        
        if st.button("🚀 Run Analysis", type="primary", use_container_width=True):
            if not google_key:
                st.error("⚠️ Enter Google API key")
            else:
                df = fetch_stock_data(selected, period)
                if df is not None and len(df) > 20:
                    metrics = calculate_all_metrics(df)
                    sentiment = calculate_price_sentiment(df, metrics)
                    recommendation = get_unified_recommendation(metrics, regime, sentiment)
                    
                    st.plotly_chart(create_chart(df.tail(90), selected), use_container_width=True)
                    
                    # Sentiment Display
                    st.subheader("📊 Price Action Sentiment")
                    sent_color = "green" if "BULLISH" in sentiment['overall'] else "red" if "BEARISH" in sentiment['overall'] else "orange"
                    st.markdown(f"**Overall:** :{sent_color}[{sentiment['overall']}] (Score: {sentiment['score']})")
                    for factor in sentiment['factors']:
                        st.text(f"• {factor}")
                    
                    # Analysis
                    st.subheader("🤖 Detailed Analysis")
                    with st.spinner("Analyzing..."):
                        analysis = run_detailed_analysis(
                            google_key, deepseek_key, st.session_state.selected_model,
                            selected, metrics, regime, sentiment, recommendation
                        )
                    st.markdown(analysis)
                else:
                    st.error("Failed to fetch data")

    elif page == "🔍 AI Screener":
        st.header("🔍 AI Quick Screener")
        st.info("Uses local logic first. No API cost for screening.")
        
        cat = st.selectbox("Category", list(NIFTY_500_STOCKS.keys()))
        stock_names = [f"{s['symbol'].replace('.NS', '')} - {s['name']}" for s in NIFTY_500_STOCKS.get(cat, [])]
        selected_stocks = st.multiselect("Select Stocks (Max 15)", stock_names, max_selections=15)
        
        if st.button("Run Screen"):
            results = []
            progress = st.progress(0)
            for i, s_name in enumerate(selected_stocks):
                ticker = s_name.split(' - ')[0] + '.NS'
                df = fetch_stock_data(ticker, "3mo")
                if df is not None:
                    metrics = calculate_all_metrics(df)
                    if metrics:
                        sent = calculate_price_sentiment(df, metrics)
                        rec = get_unified_recommendation(metrics, regime, sent)
                        results.append({
                            'Stock': ticker, 'Price': metrics['current_price'], 
                            'Signal': rec['final_recommendation'], 'Score': rec['weighted_score']
                        })
                progress.progress((i+1)/len(selected_stocks))
            
            if results:
                st.dataframe(pd.DataFrame(results))

    elif page == "📈 Backtesting":
        st.header("📈 Backtesting")
        ticker = st.text_input("Ticker Symbol (e.g. RELIANCE.NS)", value="RELIANCE.NS")
        if st.button("Run"):
            df = fetch_stock_data(ticker)
            if df is not None:
                engine = BacktestEngine(100000)
                results = engine.compare_strategies(df, ["Buy and Hold", "SMA Crossover (20/50)"], ticker)
                st.dataframe(pd.DataFrame([{
                    'Strategy': r.strategy_name, 'Return': f"{r.total_return_pct:.2f}%", 'Trades': r.total_trades
                } for r in results]))

    elif page == "⭐ Watchlist":
        st.header("⭐ Watchlist")
        if st.session_state.watchlist:
            for t in st.session_state.watchlist:
                st.write(t)
        else:
            st.info("Watchlist empty")

    elif page == "ℹ️ Help":
        st.markdown("### System Info\n- **DeepSeek Fallback:** Enabled\n- **Zero Cost Screening:** Enabled")

if __name__ == "__main__":
    main()
