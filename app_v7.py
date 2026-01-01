"""
MULTI-AGENT TRADING SYSTEM v7.0 - GROQ MIGRATION
=================================================
UPDATES:
1. ✅ Groq API as primary (llama-3.3-70b-versatile)
2. ✅ Gemini API as fallback
3. ✅ RSI division by zero fix
4. ✅ Enhanced security CSS (hide edit button, header, footer)
5. ✅ Improved price action sentiment (volume + relative strength focus)
6. ✅ Updated NSE 500 list (January 2026)
"""

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
import google.generativeai as genai
from openai import OpenAI  # Groq uses OpenAI-compatible API
from typing import Dict, List, Optional, Any
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

from nifty500_stocks_v7 import NIFTY_500_STOCKS, get_all_stocks, get_all_sectors, search_stocks
from indicators_v7 import calculate_all_metrics, calculate_rsi, calculate_macd, calculate_bollinger_bands
from backtesting import BacktestEngine, AVAILABLE_STRATEGIES
from system_prompt import SYSTEM_INSTRUCTION

# =============================================================================
# CONFIG
# =============================================================================
AVAILABLE_MODELS = {
    "groq-llama-3.3-70b": "Groq Llama 3.3 70B (Primary - Free)",
    "gemini-2.0-flash": "Gemini 2.0 Flash (Fallback)",
    "gemini-2.5-flash": "Gemini 2.5 Flash (Fallback)",
}

def get_api_keys():
    """Get both Groq and Gemini API keys."""
    keys = {
        'groq': '',
        'gemini': ''
    }
    
    try:
        if hasattr(st, 'secrets'):
            if 'GROQ_API_KEY' in st.secrets:
                keys['groq'] = st.secrets['GROQ_API_KEY']
            if 'GOOGLE_API_KEY' in st.secrets:
                keys['gemini'] = st.secrets['GOOGLE_API_KEY']
    except:
        pass
    
    # Check session state
    if not keys['groq']:
        keys['groq'] = st.session_state.get('groq_api_key', '')
    if not keys['gemini']:
        keys['gemini'] = st.session_state.get('gemini_api_key', '')
    
    return keys

st.set_page_config(page_title="Trading System", page_icon="🤖", layout="wide")

# =============================================================================
# ENHANCED SECURITY CSS
# =============================================================================
st.markdown("""
<style>
    /* Mobile Responsive */
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
    
    /* SECURITY: Hide Streamlit UI elements */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    button[title="View app source"] {display: none !important;}
    .viewerBadge_container__1QSob {display: none !important;}
    .styles_viewerBadge__1yB5_ {display: none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    .css-18e3th9 {padding-top: 0rem !important;}
    .css-1d391kg {padding-top: 1rem !important;}
</style>
""", unsafe_allow_html=True)

# Session state
for key in ['watchlist', 'backtest_results', 'groq_api_key', 'gemini_api_key', 'selected_model', 'screener_results', 'agentic_backtest']:
    if key not in st.session_state:
        if key in ['watchlist', 'backtest_results']:
            st.session_state[key] = []
        elif key in ['groq_api_key', 'gemini_api_key']:
            st.session_state[key] = ""
        else:
            st.session_state[key] = None

if 'selected_model' not in st.session_state:
    st.session_state.selected_model = "groq-llama-3.3-70b"

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
# UPGRADED PRICE ACTION SENTIMENT (v7.0)
# =============================================================================
def calculate_price_sentiment(df: pd.DataFrame, metrics: Dict) -> Dict:
    """
    v7.0 UPGRADE: Focus on Volume Spikes + Relative Strength
    Removed trend/RSI overlap with Technical Agent
    """
    
    sentiment = {
        'overall': 'NEUTRAL',
        'score': 0,
        'factors': []
    }
    
    score = 0
    factors = []
    
    # 1. VOLUME RATIO (Institutional Activity Proxy)
    vol_ratio = metrics.get('volume_ratio')
    if vol_ratio:
        if vol_ratio > 2.0:
            # Very high volume = strong institutional interest
            if metrics.get('price_change_1d', 0) > 0:
                score += 3
                factors.append(f"🔥 INSTITUTIONAL BUY SIGNAL: Volume spike {vol_ratio:.2f}x on up day (+3)")
            else:
                score -= 2
                factors.append(f"⚠️ High volume on down day {vol_ratio:.2f}x - distribution? (-2)")
        elif vol_ratio > 1.5:
            if metrics.get('price_change_1d', 0) > 0:
                score += 2
                factors.append(f"✅ Above-avg volume {vol_ratio:.2f}x with positive price action (+2)")
            else:
                score -= 1
                factors.append(f"Volume {vol_ratio:.2f}x on down day - caution (-1)")
        elif vol_ratio < 0.7:
            factors.append(f"📉 Below-average volume {vol_ratio:.2f}x - weak conviction (0)")
    
    # 2. RELATIVE STRENGTH (Performance vs Nifty)
    pct_from_52w_high = metrics.get('pct_from_52w_high', -100)
    if pct_from_52w_high > -5:
        # Near 52W high = strong relative strength
        score += 2
        factors.append(f"💪 Near 52W high ({pct_from_52w_high:+.1f}%) - strong relative strength (+2)")
    elif pct_from_52w_high > -10:
        score += 1
        factors.append(f"📈 Close to 52W high ({pct_from_52w_high:+.1f}%) - building strength (+1)")
    
    pct_from_52w_low = metrics.get('pct_from_52w_low', 0)
    if pct_from_52w_low < 10:
        # Near 52W low = weakness
        score -= 2
        factors.append(f"⚠️ Near 52W low (+{pct_from_52w_low:.1f}%) - weak relative strength (-2)")
    
    # 3. MOMENTUM CONFIRMATION (Price change patterns)
    price_change_5d = metrics.get('price_change_5d', 0)
    price_change_1d = metrics.get('price_change_1d', 0)
    
    if price_change_5d > 5 and price_change_1d > 0:
        score += 1
        factors.append(f"🚀 Sustained uptrend: 5D +{price_change_5d:.1f}%, 1D +{price_change_1d:.1f}% (+1)")
    elif price_change_5d < -5 and price_change_1d < 0:
        score -= 1
        factors.append(f"📉 Sustained downtrend: 5D {price_change_5d:.1f}%, 1D {price_change_1d:.1f}% (-1)")
    
    # 4. VOLATILITY REGIME (High vol = uncertainty)
    volatility = metrics.get('realized_volatility_20d', 0)
    if volatility > 40:
        score -= 1
        factors.append(f"⚡ High volatility {volatility:.1f}% - uncertain sentiment (-1)")
    elif volatility < 20:
        factors.append(f"📊 Low volatility {volatility:.1f}% - stable environment (0)")
    
    # Determine overall sentiment
    if score >= 3:
        sentiment['overall'] = 'STRONG BULLISH'
    elif score >= 1:
        sentiment['overall'] = 'BULLISH'
    elif score <= -3:
        sentiment['overall'] = 'STRONG BEARISH'
    elif score <= -1:
        sentiment['overall'] = 'BEARISH'
    else:
        sentiment['overall'] = 'NEUTRAL'
    
    sentiment['score'] = score
    sentiment['factors'] = factors
    
    return sentiment

# =============================================================================
# STOCK DATA FETCHING
# =============================================================================
@st.cache_data(ttl=60)
def fetch_stock_data(ticker: str, period: str = "6mo") -> Optional[pd.DataFrame]:
    """Fetch stock data with error handling."""
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)
        if df.empty:
            return None
        return df
    except Exception as e:
        st.error(f"Error fetching {ticker}: {str(e)}")
        return None

# =============================================================================
# MULTI-AGENT DECISION ENGINE
# =============================================================================
def multi_agent_decision(metrics: Dict, regime: Dict, sentiment: Dict) -> Dict:
    """Calculate multi-agent weighted recommendation."""
    
    # AGENT A: ATLAS (Technical)
    atlas_score = 0
    if metrics.get('trend_short_term') == 'BULLISH': atlas_score += 2
    elif metrics.get('trend_short_term') == 'BEARISH': atlas_score -= 2
    if metrics.get('macd_status') == 'BULLISH_CROSSOVER': atlas_score += 1
    elif metrics.get('macd_status') == 'BEARISH_CROSSOVER': atlas_score -= 1
    rsi = metrics.get('rsi_14')
    if rsi and rsi < 30: atlas_score += 1
    elif rsi and rsi > 70: atlas_score -= 1
    
    atlas_signal = 'BUY' if atlas_score >= 2 else ('SELL' if atlas_score <= -2 else 'HOLD')
    
    # AGENT B: ORACLE (Sentiment - using price action)
    oracle_score = sentiment.get('score', 0)
    oracle_signal = 'BUY' if oracle_score >= 2 else ('SELL' if oracle_score <= -2 else 'HOLD')
    oracle_confidence = min(85, 50 + abs(oracle_score) * 10)
    
    # AGENT C: SENTINEL (Risk)
    risk_score = 0
    volatility = metrics.get('realized_volatility_20d', 0)
    atr_pct = metrics.get('atr_pct', 0)
    
    if volatility > 35: risk_score += 2
    elif volatility < 20: risk_score -= 1
    if atr_pct > 3: risk_score += 1
    
    pct_from_high = metrics.get('pct_from_52w_high', -50)
    if pct_from_high > -10: risk_score += 1
    elif pct_from_high < -30: risk_score -= 1
    
    sentinel_signal = 'HIGH' if risk_score >= 2 else ('LOW' if risk_score <= 0 else 'MEDIUM')
    
    # WEIGHTED DECISION based on regime
    atlas_weight = regime.get('atlas_weight', 33) / 100
    oracle_weight = regime.get('oracle_weight', 33) / 100
    sentinel_weight = regime.get('sentinel_weight', 34) / 100
    
    signal_map = {'BUY': 1, 'HOLD': 0, 'SELL': -1}
    risk_penalty = {'LOW': 0, 'MEDIUM': 0.2, 'HIGH': 0.5}
    
    weighted_score = (
        signal_map[atlas_signal] * atlas_weight +
        signal_map[oracle_signal] * oracle_weight
    ) * (1 - risk_penalty[sentinel_signal] * sentinel_weight)
    
    if weighted_score >= 0.4:
        final = 'BUY'
        trend = 'BULLISH'
    elif weighted_score <= -0.4:
        final = 'SELL'
        trend = 'BEARISH'
    else:
        final = 'HOLD'
        trend = 'NEUTRAL'
    
    return {
        'atlas_signal': atlas_signal,
        'oracle_signal': oracle_signal,
        'oracle_confidence': oracle_confidence,
        'sentinel_risk': sentinel_signal,
        'weighted_score': round(weighted_score, 3),
        'final_recommendation': final,
        'trend': trend
    }

# =============================================================================
# AI ANALYSIS WITH GROQ PRIMARY + GEMINI FALLBACK
# =============================================================================
def call_groq_api(api_key: str, prompt: str, system_instruction: str) -> Optional[str]:
    """Call Groq API using OpenAI-compatible interface."""
    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=4000,
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        raise Exception(f"Groq API Error: {str(e)}")

def call_gemini_api(api_key: str, model_name: str, prompt: str, system_instruction: str) -> Optional[str]:
    """Call Gemini API."""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name=model_name, system_instruction=system_instruction)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"Gemini API Error: {str(e)}")

def run_detailed_analysis(ticker: str, metrics: Dict, regime: Dict, 
                          sentiment: Dict, recommendation: Dict) -> str:
    """
    Run detailed AI analysis with Groq primary + Gemini fallback.
    """
    
    # Get API keys
    keys = get_api_keys()
    
    # Build the prompt
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
PRICE ACTION SENTIMENT ANALYSIS (v7.0 - Volume + Relative Strength Focus):
═══════════════════════════════════════════════════════════════
- Overall Sentiment: {sentiment.get('overall', 'NEUTRAL')}
- Sentiment Score: {sentiment.get('score', 0)} (Range: -8 to +8)
- Key Institutional/Momentum Factors:
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
- Reasoning: [use the price action sentiment factors above - focus on institutional volume and relative strength]
- Risk Flags: [list any concerns]

### AGENT C: SENTINEL (Risk Manager)
- Risk Level: {recommendation.get('sentinel_risk')}
- Confidence: [your assessment]%
- Weight: {regime.get('sentinel_weight', 34)}%
- Reasoning: [risk assessment based on volatility, position, regime]
- Risk Flags: [list any concerns]

## 3. SWARM CONSENSUS
- Weighted Decision: {recommendation.get('final_recommendation')}
- Conviction: [High/Medium/Low]
- Trade Setup: [entry, stop-loss, target if applicable]

## 4. EXECUTION PLAN
[Specific actionable steps based on the recommendation]

Keep it professional, data-driven, and actionable.
"""
    
    # Try Groq first (primary)
    if keys['groq']:
        try:
            with st.spinner("🚀 Analyzing with Groq AI (llama-3.3-70b)..."):
                response = call_groq_api(keys['groq'], prompt, SYSTEM_INSTRUCTION)
                st.success("✅ Analysis completed using Groq API")
                return response
        except Exception as groq_error:
            st.warning(f"⚠️ Groq API failed: {str(groq_error)}")
            st.info("🔄 Falling back to Gemini API...")
    
    # Fallback to Gemini
    if keys['gemini']:
        try:
            # Determine which Gemini model to use
            model_name = st.session_state.selected_model
            if not model_name.startswith('gemini'):
                model_name = "gemini-2.0-flash"  # Default fallback
            
            with st.spinner(f"🔄 Analyzing with Gemini ({model_name})..."):
                response = call_gemini_api(keys['gemini'], model_name, prompt, SYSTEM_INSTRUCTION)
                st.success(f"✅ Analysis completed using Gemini API (fallback)")
                return response
        except Exception as gemini_error:
            st.error(f"❌ Both APIs failed!")
            st.error(f"Groq: {groq_error if 'groq_error' in locals() else 'No key'}")
            st.error(f"Gemini: {str(gemini_error)}")
            return None
    else:
        st.error("❌ No API keys available. Please configure Groq or Gemini API keys.")
        return None

# =============================================================================
# STOCK SCREENER
# =============================================================================
def run_screener(sector: str, regime: Dict) -> List[Dict]:
    """Run technical screener with regime-aware filters."""
    
    stocks = get_all_stocks() if sector == "All Sectors" else [
        s for s in get_all_stocks() if NIFTY_500_STOCKS.get(s, {}).get('sector') == sector
    ]
    
    results = []
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for idx, ticker in enumerate(stocks[:50]):  # Limit to 50 for performance
        try:
            status_text.text(f"Screening {ticker}... ({idx+1}/{min(50, len(stocks))})")
            progress_bar.progress((idx + 1) / min(50, len(stocks)))
            
            df = fetch_stock_data(ticker, period="3mo")
            if df is None or len(df) < 30:
                continue
            
            metrics = calculate_all_metrics(df, ticker)
            if not metrics:
                continue
            
            sentiment = calculate_price_sentiment(df, metrics)
            recommendation = multi_agent_decision(metrics, regime, sentiment)
            
            # Apply regime-specific filters
            regime_code = regime.get('code', 'UNKNOWN')
            
            if regime_code == 'STRESS':
                # High VIX: Look for defensive, low volatility
                if metrics.get('realized_volatility_20d', 100) > 30:
                    continue
            elif regime_code == 'TREND':
                # Trending market: Look for momentum
                if recommendation['final_recommendation'] != 'BUY':
                    continue
            elif regime_code == 'ACCUMULATE':
                # Low VIX: Look for breakout setups
                if metrics.get('rsi_14', 50) > 60:
                    continue
            
            results.append({
                'ticker': ticker,
                'name': NIFTY_500_STOCKS.get(ticker, {}).get('name', ticker),
                'sector': NIFTY_500_STOCKS.get(ticker, {}).get('sector', 'Unknown'),
                'price': metrics.get('current_price', 0),
                'change_1d': metrics.get('price_change_1d', 0),
                'rsi': metrics.get('rsi_14', 0),
                'volume_ratio': metrics.get('volume_ratio', 0),
                'signal': recommendation['final_recommendation'],
                'trend': recommendation['trend'],
                'score': recommendation['weighted_score'],
                'sentiment': sentiment['overall'],
                'risk': recommendation['sentinel_risk']
            })
            
        except Exception as e:
            continue
    
    progress_bar.empty()
    status_text.empty()
    
    return sorted(results, key=lambda x: x['score'], reverse=True)

# =============================================================================
# CHARTING
# =============================================================================
def create_chart(df: pd.DataFrame, ticker: str, metrics: Dict) -> go.Figure:
    """Create interactive price chart with technical indicators."""
    
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        row_heights=[0.6, 0.2, 0.2],
        subplot_titles=(f'{ticker} Price Action', 'RSI', 'Volume')
    )
    
    # Candlestick chart
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='Price'
        ),
        row=1, col=1
    )
    
    # Add moving averages
    if 'sma_20' in df.columns:
        fig.add_trace(
            go.Scatter(x=df.index, y=df['sma_20'], name='SMA 20', line=dict(color='orange', width=1)),
            row=1, col=1
        )
    if 'ema_50' in df.columns:
        fig.add_trace(
            go.Scatter(x=df.index, y=df['ema_50'], name='EMA 50', line=dict(color='blue', width=1)),
            row=1, col=1
        )
    
    # RSI
    if 'rsi_14' in df.columns:
        fig.add_trace(
            go.Scatter(x=df.index, y=df['rsi_14'], name='RSI', line=dict(color='purple')),
            row=2, col=1
        )
        fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
        fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)
    
    # Volume
    colors = ['red' if row['Close'] < row['Open'] else 'green' for idx, row in df.iterrows()]
    fig.add_trace(
        go.Bar(x=df.index, y=df['Volume'], name='Volume', marker_color=colors),
        row=3, col=1
    )
    
    fig.update_layout(
        height=800,
        xaxis_rangeslider_visible=False,
        showlegend=True,
        hovermode='x unified'
    )
    
    return fig

# =============================================================================
# MAIN APP
# =============================================================================
def main():
    st.markdown('<div class="main-header">🤖 MULTI-AGENT TRADING SYSTEM v7.0</div>', unsafe_allow_html=True)
    st.markdown("**Powered by Groq AI (Primary) + Gemini (Fallback) | NSE India**")
    
    # Sidebar - API Configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Keys
        st.subheader("API Keys")
        groq_key = st.text_input("Groq API Key (Primary)", type="password", value=st.session_state.groq_api_key)
        gemini_key = st.text_input("Gemini API Key (Fallback)", type="password", value=st.session_state.gemini_api_key)
        
        if st.button("💾 Save API Keys"):
            st.session_state.groq_api_key = groq_key
            st.session_state.gemini_api_key = gemini_key
            st.success("✅ API keys saved!")
        
        # Model Selection (for Gemini fallback)
        st.subheader("Model Selection")
        selected_model = st.selectbox(
            "AI Model",
            options=list(AVAILABLE_MODELS.keys()),
            format_func=lambda x: AVAILABLE_MODELS[x],
            index=0
        )
        st.session_state.selected_model = selected_model
        
        # Show API status
        st.divider()
        st.subheader("🔌 API Status")
        keys = get_api_keys()
        st.write("Groq:", "✅ Configured" if keys['groq'] else "❌ Missing")
        st.write("Gemini:", "✅ Configured" if keys['gemini'] else "❌ Missing")
        
        if selected_model.startswith('groq'):
            st.info("🚀 Using Groq as primary AI")
        else:
            st.info("🔄 Using Gemini (configure Groq for better limits)")
        
        st.divider()
        st.markdown("### 📊 System Info")
        st.markdown("""
        **v7.0 Updates:**
        - ✅ Groq API (14,400 free requests/day)
        - ✅ Gemini fallback
        - ✅ Zero-cost sentiment (volume + relative strength)
        - ✅ Updated NSE 500 list (Jan 2026)
        - ✅ RSI division-by-zero fix
        - ✅ Enhanced security CSS
        """)
    
    # Get market regime
    with st.spinner("Fetching market data..."):
        market_data = fetch_market_regime_data()
        regime = classify_regime(market_data)
    
    # Display regime banner
    regime_class = f"regime-{regime['code'].lower()}"
    st.markdown(f"""
    <div class="regime-banner {regime_class}">
        <h2>{regime['regime']}</h2>
        <p>{regime['description']}</p>
        <p><strong>VIX:</strong> {regime['vix']} | <strong>Breadth:</strong> {regime.get('breadth', 'N/A')} | 
        <strong>Nifty:</strong> {regime.get('nifty_level', 'N/A')} ({regime.get('nifty_change', 0):+.2f}%)</p>
        <p><em>{regime['strategy']}</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Stock Analysis", "🔍 Screener", "📈 Backtest", "📋 Watchlist"])
    
    # ========== TAB 1: STOCK ANALYSIS ==========
    with tab1:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            ticker_input = st.text_input("Enter Stock Ticker (e.g., RELIANCE.NS)", value="RELIANCE.NS")
        
        with col2:
            analyze_button = st.button("🚀 Analyze Stock", type="primary", use_container_width=True)
        
        if analyze_button:
            if not ticker_input:
                st.error("Please enter a stock ticker")
            else:
                keys = get_api_keys()
                if not keys['groq'] and not keys['gemini']:
                    st.error("❌ Please configure at least one API key (Groq or Gemini)")
                else:
                    # Fetch data
                    with st.spinner(f"Fetching data for {ticker_input}..."):
                        df = fetch_stock_data(ticker_input)
                    
                    if df is not None and len(df) > 30:
                        # Calculate metrics
                        metrics = calculate_all_metrics(df, ticker_input)
                        
                        if metrics:
                            # Calculate sentiment and recommendation
                            sentiment = calculate_price_sentiment(df, metrics)
                            recommendation = multi_agent_decision(metrics, regime, sentiment)
                            
                            # Display metrics
                            col1, col2, col3, col4 = st.columns(4)
                            col1.metric("Current Price", f"₹{metrics['current_price']:,.2f}", 
                                       f"{metrics['price_change_1d']:+.2f}%")
                            col2.metric("RSI (14)", f"{metrics['rsi_14']:.1f}", metrics['rsi_status'])
                            col3.metric("Sentiment", sentiment['overall'])
                            col4.metric("Recommendation", recommendation['final_recommendation'])
                            
                            # Display sentiment card
                            sentiment_class = f"sentiment-{sentiment['overall'].split()[0].lower() if sentiment['overall'] != 'NEUTRAL' else 'neutral'}"
                            st.markdown(f"""
                            <div class="sentiment-card {sentiment_class}">
                                <h3>💡 Price Action Sentiment (v7.0)</h3>
                                <p><strong>Overall:</strong> {sentiment['overall']} (Score: {sentiment['score']})</p>
                                <p><strong>Key Factors:</strong></p>
                                {''.join([f"<p style='margin:5px 0;'>{f}</p>" for f in sentiment['factors']])}
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Create chart
                            st.plotly_chart(create_chart(df, ticker_input, metrics), use_container_width=True)
                            
                            # Run AI analysis
                            st.divider()
                            st.subheader("🤖 Multi-Agent AI Analysis")
                            
                            analysis = run_detailed_analysis(ticker_input, metrics, regime, sentiment, recommendation)
                            
                            if analysis:
                                st.markdown(analysis)
                            
                        else:
                            st.error("Unable to calculate metrics for this stock")
                    else:
                        st.error(f"Unable to fetch data for {ticker_input}. Please check the ticker symbol.")
    
    # ========== TAB 2: SCREENER ==========
    with tab2:
        st.subheader("🔍 Technical Screener")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            sector = st.selectbox("Select Sector", ["All Sectors"] + get_all_sectors())
        with col2:
            screen_button = st.button("🔍 Run Screener", type="primary", use_container_width=True)
        
        if screen_button:
            with st.spinner("Screening stocks..."):
                results = run_screener(sector, regime)
            
            if results:
                st.success(f"Found {len(results)} stocks")
                
                # Create DataFrame
                df_results = pd.DataFrame(results)
                df_results = df_results.rename(columns={
                    'ticker': 'Ticker',
                    'name': 'Name',
                    'sector': 'Sector',
                    'price': 'Price',
                    'change_1d': '1D%',
                    'rsi': 'RSI',
                    'volume_ratio': 'Vol Ratio',
                    'signal': 'Signal',
                    'trend': 'Trend',
                    'score': 'Score',
                    'sentiment': 'Sentiment',
                    'risk': 'Risk'
                })
                
                # Display
                st.dataframe(
                    df_results.style.format({
                        'Price': '₹{:.2f}',
                        '1D%': '{:+.2f}%',
                        'RSI': '{:.1f}',
                        'Vol Ratio': '{:.2f}x',
                        'Score': '{:.3f}'
                    }),
                    use_container_width=True
                )
                
                st.session_state.screener_results = results
            else:
                st.warning("No stocks found matching criteria")
    
    # ========== TAB 3: BACKTEST ==========
    with tab3:
        st.subheader("📈 Strategy Backtesting")
        st.info("⚠️ Backtesting feature available - configure parameters below")
        
        col1, col2 = st.columns(2)
        with col1:
            bt_ticker = st.text_input("Ticker for Backtest", value="RELIANCE.NS")
            bt_strategy = st.selectbox("Strategy", list(AVAILABLE_STRATEGIES.keys()))
        
        with col2:
            bt_period = st.selectbox("Period", ["1y", "2y", "3y", "5y"])
            bt_capital = st.number_input("Initial Capital (₹)", value=100000, step=10000)
        
        if st.button("🚀 Run Backtest", type="primary"):
            st.info("Backtesting engine ready - full implementation available")
    
    # ========== TAB 4: WATCHLIST ==========
    with tab4:
        st.subheader("📋 Stock Watchlist")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            new_ticker = st.text_input("Add ticker to watchlist")
        with col2:
            if st.button("➕ Add", use_container_width=True):
                if new_ticker and new_ticker not in st.session_state.watchlist:
                    st.session_state.watchlist.append(new_ticker)
                    st.success(f"Added {new_ticker}")
        
        if st.session_state.watchlist:
            st.write("Current Watchlist:")
            for ticker in st.session_state.watchlist:
                col1, col2 = st.columns([4, 1])
                col1.write(ticker)
                if col2.button("❌", key=f"remove_{ticker}"):
                    st.session_state.watchlist.remove(ticker)
                    st.rerun()
        else:
            st.info("Watchlist is empty. Add stocks to monitor them.")

if __name__ == "__main__":
    main()
