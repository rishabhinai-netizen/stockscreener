"""
MULTI-AGENT TRADING SYSTEM v6.0 - FINAL
========================================
CRITICAL FIXES:
1. VIX/Breadth properly passed to AI
2. Consistent signals between screener and detailed
3. Clean section separation in reports
4. Alternative to news - using price action sentiment
5. Restored original agentic approach
6. Removed Tech Screener
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

def get_api_key():
    try:
        if hasattr(st, 'secrets') and 'GOOGLE_API_KEY' in st.secrets:
            return st.secrets['GOOGLE_API_KEY']
    except:
        pass
    return st.session_state.get('api_key', '')

st.set_page_config(page_title="Trading System", page_icon="🤖", layout="wide")

# =============================================================================
# CSS
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
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Session state
for key in ['watchlist', 'backtest_results', 'api_key', 'selected_model', 'screener_results', 'agentic_backtest']:
    if key not in st.session_state:
        st.session_state[key] = [] if key in ['watchlist', 'backtest_results'] else (None if key != 'api_key' else "")
if 'selected_model' not in st.session_state:
    st.session_state.selected_model = "gemini-2.0-flash"

# =============================================================================
# MARKET DATA - PROPERLY STRUCTURED
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
# PRICE ACTION SENTIMENT (ALTERNATIVE TO NEWS)
# =============================================================================
def calculate_price_sentiment(df: pd.DataFrame, metrics: Dict) -> Dict:
    """Calculate sentiment from price action instead of news."""
    
    sentiment = {
        'overall': 'NEUTRAL',
        'score': 0,
        'factors': []
    }
    
    score = 0
    factors = []
    
    # 1. Trend Analysis
    if metrics.get('trend_short_term') == 'BULLISH':
        score += 2
        factors.append("Short-term trend is BULLISH (+2)")
    elif metrics.get('trend_short_term') == 'BEARISH':
        score -= 2
        factors.append("Short-term trend is BEARISH (-2)")
    
    if metrics.get('trend_medium_term') == 'BULLISH':
        score += 1
        factors.append("Medium-term trend is BULLISH (+1)")
    elif metrics.get('trend_medium_term') == 'BEARISH':
        score -= 1
        factors.append("Medium-term trend is BEARISH (-1)")
    
    # 2. RSI Analysis
    rsi = metrics.get('rsi_14')
    if rsi:
        if rsi < 30:
            score += 2
            factors.append(f"RSI oversold at {rsi:.1f} - Potential bounce (+2)")
        elif rsi > 70:
            score -= 2
            factors.append(f"RSI overbought at {rsi:.1f} - Potential pullback (-2)")
        elif 40 <= rsi <= 60:
            factors.append(f"RSI neutral at {rsi:.1f}")
    
    # 3. Volume Analysis
    vol_ratio = metrics.get('volume_ratio')
    if vol_ratio:
        if vol_ratio > 1.5:
            if metrics.get('price_change_1d', 0) > 0:
                score += 1
                factors.append(f"High volume on up day ({vol_ratio:.2f}x) (+1)")
            else:
                score -= 1
                factors.append(f"High volume on down day ({vol_ratio:.2f}x) (-1)")
    
    # 4. Price Position
    pct_from_high = metrics.get('pct_from_52w_high', 0)
    pct_from_low = metrics.get('pct_from_52w_low', 0)
    
    if pct_from_high and pct_from_high > -5:
        score += 1
        factors.append(f"Near 52-week high ({pct_from_high:+.1f}%) - Strength (+1)")
    elif pct_from_low and pct_from_low < 10:
        score += 1
        factors.append(f"Near 52-week low ({pct_from_low:+.1f}%) - Potential value (+1)")
    
    # 5. Moving Average Analysis
    price_vs_sma = metrics.get('price_vs_sma20_pct', 0)
    if price_vs_sma:
        if price_vs_sma > 5:
            score += 1
            factors.append(f"Price {price_vs_sma:+.1f}% above SMA20 - Bullish (+1)")
        elif price_vs_sma < -5:
            score -= 1
            factors.append(f"Price {price_vs_sma:+.1f}% below SMA20 - Bearish (-1)")
    
    # 6. MACD
    macd_status = metrics.get('macd_status')
    if macd_status == 'BULLISH':
        score += 1
        factors.append("MACD bullish crossover (+1)")
    elif macd_status == 'BEARISH':
        score -= 1
        factors.append("MACD bearish crossover (-1)")
    
    # 7. ADX Trend Strength
    adx = metrics.get('adx_14')
    if adx and adx > 25:
        factors.append(f"Strong trend (ADX: {adx:.1f})")
    elif adx and adx < 20:
        factors.append(f"Weak/No trend (ADX: {adx:.1f})")
    
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
    try:
        return yf.Ticker(ticker).history(period=period)
    except:
        return None

# =============================================================================
# UNIFIED AI ANALYSIS - CONSISTENT FOR BOTH SCREENER AND DETAILED
# =============================================================================
def get_unified_recommendation(metrics: Dict, regime: Dict, sentiment: Dict) -> Dict:
    """Generate consistent recommendation based on rules - used by both screener and detailed."""
    
    # Initialize scores
    atlas_signal = 'HOLD'
    atlas_confidence = 50
    oracle_signal = 'HOLD'
    oracle_confidence = 50
    sentinel_signal = 'MEDIUM'
    
    # ATLAS (Technical) Analysis
    rsi = metrics.get('rsi_14', 50)
    adx = metrics.get('adx_14', 20)
    trend = metrics.get('trend_short_term', 'NEUTRAL')
    price_vs_sma = metrics.get('price_vs_sma20_pct', 0)
    macd = metrics.get('macd_status', 'NEUTRAL')
    
    atlas_score = 0
    
    # RSI signals
    if rsi and rsi < 30:
        atlas_score += 2
    elif rsi and rsi > 70:
        atlas_score -= 2
    
    # Trend signals
    if trend == 'BULLISH':
        atlas_score += 1
    elif trend == 'BEARISH':
        atlas_score -= 1
    
    # MACD signals
    if macd == 'BULLISH':
        atlas_score += 1
    elif macd == 'BEARISH':
        atlas_score -= 1
    
    # Price vs SMA
    if price_vs_sma and price_vs_sma > 2:
        atlas_score += 1
    elif price_vs_sma and price_vs_sma < -2:
        atlas_score -= 1
    
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
    if volatility and volatility > 30:
        risk_score += 2
    if rsi and (rsi > 75 or rsi < 25):
        risk_score += 1
    if pct_from_high < 5:  # Near 52-week high
        risk_score += 1
    
    if risk_score >= 3:
        sentinel_signal = 'HIGH'
    elif risk_score >= 1:
        sentinel_signal = 'MEDIUM'
    else:
        sentinel_signal = 'LOW'
    
    # Calculate weighted final decision
    atlas_weight = regime.get('atlas_weight', 33) / 100
    oracle_weight = regime.get('oracle_weight', 33) / 100
    sentinel_weight = regime.get('sentinel_weight', 34) / 100
    
    # Convert signals to scores
    signal_scores = {'BUY': 1, 'HOLD': 0, 'SELL': -1}
    risk_modifier = {'LOW': 1.0, 'MEDIUM': 0.7, 'HIGH': 0.4}
    
    weighted_score = (
        signal_scores.get(atlas_signal, 0) * atlas_weight +
        signal_scores.get(oracle_signal, 0) * oracle_weight
    ) * risk_modifier.get(sentinel_signal, 0.7)
    
    # Determine final recommendation
    if weighted_score >= 0.4:
        final = 'STRONG BUY'
    elif weighted_score >= 0.15:
        final = 'BUY'
    elif weighted_score <= -0.4:
        final = 'STRONG SELL'
    elif weighted_score <= -0.15:
        final = 'SELL'
    else:
        final = 'HOLD'
    
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
# AI DETAILED ANALYSIS
# =============================================================================
def run_detailed_analysis(api_key: str, model_name: str, ticker: str, metrics: Dict, 
                          regime: Dict, sentiment: Dict, recommendation: Dict) -> str:
    """Run detailed AI analysis with all context properly passed."""
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name=model_name, system_instruction=SYSTEM_INSTRUCTION)
        
        prompt = f"""
Analyze {ticker} using the Multi-Agent Swarm Decision Engine.

═══════════════════════════════════════════════════════════════
MARKET REGIME DATA (USE THIS - IT IS REAL-TIME DATA):
═══════════════════════════════════════════════════════════════
- India VIX: {regime.get('vix', 'N/A')}
- Nifty 50 Level: {regime.get('nifty_level', 'N/A')}
- Nifty Change: {regime.get('nifty_change', 0):+.2f}%
- Market Breadth: {regime.get('breadth', 'N/A')} (Advances/Declines)
- Detected Regime: {regime.get('regime', 'UNKNOWN')} ({regime.get('code', 'N/A')})
- Regime Confidence: {regime.get('confidence', 0)}%
- Recommended Strategy: {regime.get('strategy', 'N/A')}

Agent Weights for this Regime:
- ATLAS (Technical): {regime.get('atlas_weight', 33)}%
- ORACLE (Sentiment): {regime.get('oracle_weight', 33)}%
- SENTINEL (Risk): {regime.get('sentinel_weight', 34)}%

═══════════════════════════════════════════════════════════════
STOCK TECHNICAL DATA:
═══════════════════════════════════════════════════════════════
- Current Price: ₹{metrics.get('current_price', 0):,.2f}
- Day Change: {metrics.get('price_change_1d', 0):+.2f}%
- RSI (14): {metrics.get('rsi_14', 'N/A')} - {metrics.get('rsi_status', '')}
- ADX (14): {metrics.get('adx_14', 'N/A')} - {metrics.get('trend_strength', '')}
- MACD Status: {metrics.get('macd_status', 'N/A')}
- Trend (Short): {metrics.get('trend_short_term', 'N/A')}
- Trend (Medium): {metrics.get('trend_medium_term', 'N/A')}
- Price vs SMA20: {metrics.get('price_vs_sma20_pct', 0):+.2f}%
- Volume Ratio: {metrics.get('volume_ratio', 0):.2f}x
- 52W High: ₹{metrics.get('high_52w', 0):,.2f} ({metrics.get('pct_from_52w_high', 0):+.1f}%)
- 52W Low: ₹{metrics.get('low_52w', 0):,.2f} ({metrics.get('pct_from_52w_low', 0):+.1f}%)
- Volatility (20D): {metrics.get('realized_volatility_20d', 0):.1f}%
- ATR%: {metrics.get('atr_pct', 0):.2f}%

═══════════════════════════════════════════════════════════════
PRICE ACTION SENTIMENT ANALYSIS:
═══════════════════════════════════════════════════════════════
- Overall Sentiment: {sentiment.get('overall', 'NEUTRAL')}
- Sentiment Score: {sentiment.get('score', 0)} (Range: -6 to +6)
- Key Factors:
{chr(10).join(['  • ' + f for f in sentiment.get('factors', [])])}

═══════════════════════════════════════════════════════════════
PRE-CALCULATED RECOMMENDATION (For Consistency):
═══════════════════════════════════════════════════════════════
- ATLAS Signal: {recommendation.get('atlas_signal')}
- ORACLE Signal: {recommendation.get('oracle_signal')}
- SENTINEL Risk: {recommendation.get('sentinel_risk')}
- Weighted Score: {recommendation.get('weighted_score')}
- Final: {recommendation.get('final_recommendation')}

═══════════════════════════════════════════════════════════════
YOUR TASK:
═══════════════════════════════════════════════════════════════
Provide detailed analysis following this EXACT structure:

## 1. MARKET REGIME CLASSIFICATION
(Brief - use the data provided above)

## 2. AGENT ANALYSIS

### AGENT A: ATLAS (Technical Eye)
- Signal: {recommendation.get('atlas_signal')}
- Confidence: [your assessment]%
- Weight: {regime.get('atlas_weight', 33)}%
- Reasoning: [detailed technical analysis]
- Risk Flags: [list any concerns]

### AGENT B: ORACLE (Sentiment Eye)  
- Signal: {recommendation.get('oracle_signal')}
- Confidence: [your assessment]%
- Weight: {regime.get('oracle_weight', 33)}%
- Reasoning: [use the price action sentiment factors above]
- Risk Flags: [list any concerns]

### AGENT C: SENTINEL (Risk Manager)
- Risk Level: {recommendation.get('sentinel_risk')}
- Confidence: [your assessment]%
- Weight: {regime.get('sentinel_weight', 34)}%
- Reasoning: [risk assessment based on volatility, position, regime]
- Risk Flags: [list all risks]

## 3. CROSS-EXAMINATION DEBATE
(Brief debate between agents - 3-4 exchanges max)

## 4. CONSENSUS DECISION
- Final Action: {recommendation.get('final_recommendation')}
- Weighted Score: {recommendation.get('weighted_score')}
- Entry Price: [specific level]
- Stop Loss: [specific level with reasoning]
- Target 1: [specific level]
- Target 2: [specific level]
- Position Size: [% recommendation based on regime]
- Key Drivers: [bullet points]
- Risk Warnings: [bullet points]
- Invalidation: [when this trade idea fails]

BE CONCISE. DO NOT REPEAT SECTIONS. Each section should have unique content.
"""
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"Error generating analysis: {str(e)}"

# =============================================================================
# CHARTS
# =============================================================================
def create_chart(df, ticker):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.08,
                        row_heights=[0.7, 0.3])
    
    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'],
                                  low=df['Low'], close=df['Close'], name='Price'), row=1, col=1)
    
    sma20 = df['Close'].rolling(20).mean()
    sma50 = df['Close'].rolling(50).mean()
    fig.add_trace(go.Scatter(x=df.index, y=sma20, name='SMA20', line=dict(color='orange', width=1)), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=sma50, name='SMA50', line=dict(color='blue', width=1)), row=1, col=1)
    
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
    
    # Fetch market regime data once
    regime_data = fetch_market_regime_data()
    regime = classify_regime(regime_data)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        try:
            if 'GOOGLE_API_KEY' in st.secrets:
                st.success("✅ API Key loaded")
        except:
            st.session_state.api_key = st.text_input("API Key", type="password", 
                                                      value=st.session_state.api_key)
        
        st.session_state.selected_model = st.selectbox(
            "Model", list(AVAILABLE_MODELS.keys()),
            format_func=lambda x: AVAILABLE_MODELS[x]
        )
        
        st.divider()
        
        page = st.radio("Navigation", [
            "🎯 AI Analysis",
            "🔍 AI Screener",
            "📈 Backtesting",
            "🤖 Agentic Backtest",
            "⭐ Watchlist",
            "ℹ️ Help"
        ])
        
        st.divider()
        
        # Market Regime Display
        st.markdown("### 📊 Market Regime")
        regime_class = regime.get('code', 'unknown').lower()
        st.markdown(f"""
        <div class="regime-banner regime-{regime_class}">
            <strong>{regime.get('regime', 'UNKNOWN')}</strong><br>
            <small>VIX: {regime.get('vix', 'N/A')} | Breadth: {regime.get('breadth', 'N/A')}</small>
        </div>
        """, unsafe_allow_html=True)
        st.caption(f"Confidence: {regime.get('confidence', 0)}%")

    api_key = get_api_key()

    # ==========================================================================
    # AI ANALYSIS PAGE
    # ==========================================================================
    if page == "🎯 AI Analysis":
        st.header("🎯 AI Analysis")
        
        # Display market context
        st.markdown(f"""
        <div class="regime-banner regime-{regime.get('code', 'unknown').lower()}">
            <h3 style="margin:0;">Market Regime: {regime.get('regime', 'UNKNOWN')}</h3>
            <p style="margin:5px 0;">VIX: {regime.get('vix', 'N/A')} | Nifty: {regime.get('nifty_level', 'N/A')} ({regime.get('nifty_change', 0):+.2f}%) | Breadth: {regime.get('breadth', 'N/A')}</p>
            <p style="margin:0;font-size:0.9em;">{regime.get('description', '')}</p>
        </div>
        """, unsafe_allow_html=True)
        
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
            if not api_key:
                st.error("⚠️ Enter API key in sidebar")
            else:
                df = fetch_stock_data(selected, period)
                if df is not None and len(df) > 20:
                    metrics = calculate_all_metrics(df)
                    sentiment = calculate_price_sentiment(df, metrics)
                    recommendation = get_unified_recommendation(metrics, regime, sentiment)
                    
                    # Chart
                    st.plotly_chart(create_chart(df.tail(90), selected), use_container_width=True)
                    
                    # Quick Metrics
                    c1, c2, c3, c4 = st.columns(4)
                    c1.metric("Price", f"₹{metrics['current_price']:,.2f}", f"{metrics['price_change_1d']:+.2f}%")
                    c2.metric("RSI", f"{metrics.get('rsi_14', 0):.1f}", metrics.get('rsi_status', ''))
                    c3.metric("ADX", f"{metrics.get('adx_14', 0):.1f}", metrics.get('trend_strength', ''))
                    c4.metric("Trend", metrics.get('trend_short_term', 'N/A'))
                    
                    # Sentiment Analysis (Alternative to News)
                    st.subheader("📊 Price Action Sentiment")
                    sentiment_class = sentiment['overall'].lower().replace(' ', '-')
                    if 'bullish' in sentiment_class:
                        sent_css = 'sentiment-bullish'
                    elif 'bearish' in sentiment_class:
                        sent_css = 'sentiment-bearish'
                    else:
                        sent_css = 'sentiment-neutral'
                    
                    st.markdown(f"""
                    <div class="sentiment-card {sent_css}">
                        <strong>Sentiment: {sentiment['overall']}</strong> (Score: {sentiment['score']:+d})<br>
                        <small>Based on price action analysis - Alternative to news sentiment</small>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    with st.expander("View Sentiment Factors"):
                        for factor in sentiment['factors']:
                            st.write(f"• {factor}")
                    
                    # Quick Recommendation Summary
                    st.subheader("⚡ Quick Recommendation")
                    final = recommendation['final_recommendation']
                    color = '#4caf50' if 'BUY' in final else '#f44336' if 'SELL' in final else '#ff9800'
                    
                    st.markdown(f"""
                    <div style="padding:20px; background:#f5f5f5; border-radius:10px; border-left:5px solid {color};">
                        <h2 style="margin:0; color:{color};">{final}</h2>
                        <p>ATLAS: {recommendation['atlas_signal']} | ORACLE: {recommendation['oracle_signal']} | Risk: {recommendation['sentinel_risk']}</p>
                        <small>Weighted Score: {recommendation['weighted_score']}</small>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Detailed AI Analysis
                    st.subheader("🤖 Detailed Multi-Agent Analysis")
                    
                    with st.spinner("Generating detailed analysis..."):
                        analysis = run_detailed_analysis(
                            api_key, st.session_state.selected_model,
                            selected, metrics, regime, sentiment, recommendation
                        )
                    
                    # Display in tabs
                    tab1, tab2, tab3, tab4 = st.tabs(["📈 ATLAS", "🔮 ORACLE", "🛡️ SENTINEL", "📋 Full Report"])
                    
                    with tab1:
                        atlas_section = extract_section(analysis, "ATLAS", "ORACLE")
                        st.markdown(atlas_section if atlas_section else "Analysis not available")
                    
                    with tab2:
                        oracle_section = extract_section(analysis, "ORACLE", "SENTINEL")
                        st.markdown(oracle_section if oracle_section else "Analysis not available")
                    
                    with tab3:
                        sentinel_section = extract_section(analysis, "SENTINEL", "CROSS")
                        st.markdown(sentinel_section if sentinel_section else "Analysis not available")
                    
                    with tab4:
                        st.markdown(analysis)
                    
                    st.download_button("📥 Download Report", analysis, f"{selected}_report.txt")
                else:
                    st.error("Failed to fetch data")

    # ==========================================================================
    # AI SCREENER PAGE - USING SAME LOGIC
    # ==========================================================================
    elif page == "🔍 AI Screener":
        st.header("🔍 AI Quick Screener")
        
        # Market context
        st.info(f"📊 Market Regime: **{regime.get('regime')}** | VIX: {regime.get('vix')} | Breadth: {regime.get('breadth')}")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            cat = st.selectbox("Category", list(NIFTY_500_STOCKS.keys()))
            category_stocks = NIFTY_500_STOCKS.get(cat, [])
            stock_names = [f"{s['symbol'].replace('.NS', '')} - {s['name']}" for s in category_stocks]
            
            st.info(f"📊 {len(category_stocks)} stocks in {cat}")
            
            selected_stocks = st.multiselect(
                "Select Stocks",
                options=stock_names,
                default=stock_names[:5],
                help="Select up to 15 stocks"
            )
            
            if len(selected_stocks) > 15:
                st.warning("Max 15 stocks")
                selected_stocks = selected_stocks[:15]
            
            if st.button("🚀 Run Screening", type="primary", use_container_width=True):
                if not selected_stocks:
                    st.error("Select at least one stock")
                else:
                    results = []
                    progress = st.progress(0)
                    
                    for i, stock_name in enumerate(selected_stocks):
                        ticker = stock_name.split(' - ')[0] + '.NS'
                        
                        df = fetch_stock_data(ticker, "3mo")
                        if df is not None and len(df) > 20:
                            metrics = calculate_all_metrics(df)
                            if metrics:
                                sentiment = calculate_price_sentiment(df, metrics)
                                # USE SAME RECOMMENDATION LOGIC
                                rec = get_unified_recommendation(metrics, regime, sentiment)
                                
                                results.append({
                                    'ticker': ticker.replace('.NS', ''),
                                    'price': metrics['current_price'],
                                    'change': metrics.get('price_change_1d', 0),
                                    'trend': rec['trend'],
                                    'atlas': rec['atlas_signal'],
                                    'oracle': rec['oracle_signal'],
                                    'risk': rec['sentinel_risk'],
                                    'final': rec['final_recommendation'],
                                    'score': rec['weighted_score']
                                })
                        
                        progress.progress((i + 1) / len(selected_stocks))
                    
                    st.session_state.screener_results = results
        
        with col2:
            if st.session_state.screener_results:
                st.subheader("📊 Results")
                
                for r in st.session_state.screener_results:
                    final = r['final']
                    if 'STRONG BUY' in final:
                        color, css = '#2e7d32', 'result-buy'
                    elif 'BUY' in final:
                        color, css = '#4caf50', 'result-buy'
                    elif 'STRONG SELL' in final:
                        color, css = '#c62828', 'result-sell'
                    elif 'SELL' in final:
                        color, css = '#f44336', 'result-sell'
                    else:
                        color, css = '#ff9800', 'result-hold'
                    
                    st.markdown(f"""
                    <div class="result-card {css}">
                        <strong>{r['ticker']}</strong> - 
                        <span style="color:{color}; font-weight:bold;">{final}</span>
                        <span style="float:right;">₹{r['price']:,.2f} ({r['change']:+.1f}%)</span><br>
                        <small>Trend: {r['trend']} | ATLAS: {r['atlas']} | ORACLE: {r['oracle']} | Risk: {r['risk']} | Score: {r['score']}</small>
                    </div>
                    """, unsafe_allow_html=True)

    # ==========================================================================
    # BACKTESTING PAGE
    # ==========================================================================
    elif page == "📈 Backtesting":
        st.header("📈 Strategy Backtesting")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            all_stocks = get_all_stocks()
            opts = [(s['symbol'], f"{s['symbol'].replace('.NS','')} - {s['name']}") for s in all_stocks]
            ticker = st.selectbox("Stock", [o[0] for o in opts],
                                 format_func=lambda x: next((o[1] for o in opts if o[0]==x), x))
            period = st.selectbox("Period", ["6mo", "1y", "2y"], index=1)
            capital = st.number_input("Capital ₹", value=100000, step=10000)
            strategies = st.multiselect("Strategies", AVAILABLE_STRATEGIES,
                                       default=["Buy and Hold", "SMA Crossover (20/50)"])
            
            if st.button("▶️ Run Backtest", type="primary"):
                df = fetch_stock_data(ticker, period)
                if df is not None and len(df) > 50:
                    engine = BacktestEngine(capital, 0.001)
                    st.session_state.backtest_results = engine.compare_strategies(df, strategies, ticker)
                else:
                    st.error("Insufficient data")
        
        with col2:
            if st.session_state.backtest_results:
                st.subheader("Results")
                data = [{
                    'Strategy': r.strategy_name,
                    'Return': f"{r.total_return_pct:+.1f}%",
                    'Final': f"₹{r.final_capital:,.0f}",
                    'Sharpe': f"{r.sharpe_ratio:.2f}",
                    'MaxDD': f"{r.max_drawdown_pct:.1f}%",
                    'Trades': r.total_trades
                } for r in st.session_state.backtest_results]
                st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
                
                sel = st.selectbox("View Trades", [r.strategy_name for r in st.session_state.backtest_results])
                result = next(r for r in st.session_state.backtest_results if r.strategy_name == sel)
                
                if result.trades:
                    trades = [{
                        'Entry': t.entry_date, 'Exit': t.exit_date,
                        'P&L': f"₹{t.pnl:+,.0f}", 'Return': f"{t.pnl_pct:+.1f}%"
                    } for t in result.trades]
                    st.dataframe(pd.DataFrame(trades), use_container_width=True, hide_index=True)

    # ==========================================================================
    # AGENTIC BACKTEST PAGE
    # ==========================================================================
    elif page == "🤖 Agentic Backtest":
        st.header("🤖 Agentic Backtest")
        st.markdown("Test how the unified recommendation system would have performed")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            all_stocks = get_all_stocks()
            opts = [(s['symbol'], f"{s['symbol'].replace('.NS','')} - {s['name']}") for s in all_stocks]
            ticker = st.selectbox("Stock", [o[0] for o in opts],
                                 format_func=lambda x: next((o[1] for o in opts if o[0]==x), x),
                                 key="agentic_ticker")
            period = st.selectbox("Period", ["6mo", "1y", "2y"], index=1, key="agentic_period")
            capital = st.number_input("Capital ₹", value=100000, key="agentic_capital")
            
            if st.button("🚀 Run Agentic Backtest", type="primary"):
                df = fetch_stock_data(ticker, period)
                if df is not None and len(df) > 100:
                    results = run_agentic_backtest_unified(df, ticker, capital, regime)
                    st.session_state.agentic_backtest = results
                else:
                    st.error("Need more data")
        
        with col2:
            if st.session_state.agentic_backtest:
                r = st.session_state.agentic_backtest
                
                c1, c2, c3 = st.columns(3)
                c1.metric("Final Capital", f"₹{r['final_capital']:,.0f}")
                c2.metric("Return", f"{r['total_return']:+.1f}%")
                c3.metric("Trades", r['total_trades'])
                
                if r.get('decisions'):
                    st.dataframe(pd.DataFrame(r['decisions']), use_container_width=True, hide_index=True)

    # ==========================================================================
    # OTHER PAGES
    # ==========================================================================
    elif page == "⭐ Watchlist":
        st.header("⭐ Watchlist")
        if st.session_state.watchlist:
            for t in st.session_state.watchlist:
                df = fetch_stock_data(t, "1mo")
                if df is not None:
                    m = calculate_all_metrics(df)
                    if m:
                        st.write(f"**{t.replace('.NS','')}**: ₹{m['current_price']:,.2f} ({m['price_change_1d']:+.2f}%)")
            if st.button("Clear"):
                st.session_state.watchlist = []
                st.rerun()
        else:
            st.info("Empty")

    elif page == "ℹ️ Help":
        st.header("ℹ️ Help")
        st.markdown("""
### v6.0 Changes
1. **VIX/Breadth** - Now properly passed to AI analysis
2. **Consistent Signals** - Screener and detailed use SAME logic
3. **Price Action Sentiment** - Replaces unreliable news API
4. **Clean Reports** - Each tab shows only relevant content
5. **Removed Tech Screener** - Simplified navigation

### How It Works
- **ATLAS**: Technical analysis (RSI, MACD, trend, volume)
- **ORACLE**: Sentiment from price action (replaces news)
- **SENTINEL**: Risk assessment (volatility, position)
- **Weights**: Change based on market regime (VIX level)
        """)

def extract_section(text: str, start: str, end: str = None) -> str:
    """Extract section from analysis."""
    try:
        start_idx = text.upper().find(start.upper())
        if start_idx == -1:
            return ""
        if end:
            end_idx = text.upper().find(end.upper(), start_idx + len(start))
            if end_idx == -1:
                return text[start_idx:]
            return text[start_idx:end_idx]
        return text[start_idx:]
    except:
        return ""

def run_agentic_backtest_unified(df: pd.DataFrame, ticker: str, capital: float, regime: Dict) -> Dict:
    """Run backtest using unified recommendation logic."""
    results = {
        'ticker': ticker,
        'initial_capital': capital,
        'decisions': [],
        'trades': []
    }
    
    position = 0
    entry_price = 0
    cash = capital
    
    # Sample every 10 days
    for i in range(50, len(df), 10):
        hist = df.iloc[:i+1]
        metrics = calculate_all_metrics(hist)
        if not metrics:
            continue
        
        sentiment = calculate_price_sentiment(hist, metrics)
        rec = get_unified_recommendation(metrics, regime, sentiment)
        
        current_price = hist['Close'].iloc[-1]
        current_date = hist.index[-1].strftime('%Y-%m-%d')
        
        # Trading logic
        if rec['final_recommendation'] in ['STRONG BUY', 'BUY'] and position == 0:
            shares = int(cash * 0.95 / current_price)
            if shares > 0:
                position = shares
                entry_price = current_price
                cash -= shares * current_price
                results['trades'].append({'date': current_date, 'type': 'BUY', 'price': current_price})
        
        elif rec['final_recommendation'] in ['STRONG SELL', 'SELL'] and position > 0:
            cash += position * current_price
            results['trades'].append({'date': current_date, 'type': 'SELL', 'price': current_price,
                                     'pnl': (current_price - entry_price) * position})
            position = 0
        
        results['decisions'].append({
            'date': current_date,
            'price': f"₹{current_price:,.2f}",
            'signal': rec['final_recommendation'],
            'score': rec['weighted_score']
        })
    
    # Close position
    if position > 0:
        cash += position * df['Close'].iloc[-1]
    
    results['final_capital'] = cash
    results['total_return'] = ((cash / capital) - 1) * 100
    results['total_trades'] = len([t for t in results['trades'] if t['type'] == 'BUY'])
    
    return results

if __name__ == "__main__":
    main()
