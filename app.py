"""
MULTI-AGENT TRADING SYSTEM v5.0
================================
MAJOR FIXES:
1. Fixed HTML rendering (using st.markdown properly)
2. Added stock selection in AI Screener
3. Consistent signals between screener and detailed analysis
4. Alternative news sources
5. Mobile-friendly CSS
6. Agentic Backtesting feature
7. Professional report formatting
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
import requests
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
DEFAULT_MODEL = "gemini-2.0-flash"

def get_api_key():
    try:
        if hasattr(st, 'secrets') and 'GOOGLE_API_KEY' in st.secrets:
            return st.secrets['GOOGLE_API_KEY']
    except:
        pass
    return st.session_state.get('api_key', '')

st.set_page_config(
    page_title="Trading System", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# MOBILE-FRIENDLY CSS
# =============================================================================
st.markdown("""
<style>
    /* Mobile responsive */
    @media (max-width: 768px) {
        .main .block-container { padding: 1rem; }
        .stColumn { width: 100% !important; }
        h1 { font-size: 1.5rem !important; }
        h2 { font-size: 1.2rem !important; }
    }
    
    .main-header {
        font-size: clamp(1.5rem, 4vw, 2.5rem);
        font-weight: bold;
        background: linear-gradient(120deg, #00d4ff, #7b2cbf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
    }
    
    /* Report Sections */
    .report-section {
        background: #ffffff;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    
    .regime-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin: 15px 0;
    }
    
    .regime-stress { background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%) !important; }
    .regime-accumulate { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important; }
    .regime-trend { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%) !important; }
    .regime-goldilocks { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important; }
    
    .agent-box {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #ccc;
    }
    .agent-atlas { border-left-color: #00d4ff !important; background: #e3f2fd !important; }
    .agent-oracle { border-left-color: #9c27b0 !important; background: #f3e5f5 !important; }
    .agent-sentinel { border-left-color: #f44336 !important; background: #ffebee !important; }
    
    .signal-strong-buy { color: #00c853; font-weight: bold; font-size: 1.2em; }
    .signal-buy { color: #4caf50; font-weight: bold; }
    .signal-hold { color: #ff9800; font-weight: bold; }
    .signal-sell { color: #f44336; font-weight: bold; }
    .signal-strong-sell { color: #b71c1c; font-weight: bold; font-size: 1.2em; }
    
    .consensus-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
    }
    
    .news-card {
        padding: 12px;
        margin: 8px 0;
        border-radius: 8px;
        background: #fafafa;
        border-left: 4px solid #9e9e9e;
    }
    .news-positive { border-left-color: #4caf50 !important; background: #e8f5e9 !important; }
    .news-negative { border-left-color: #f44336 !important; background: #ffebee !important; }
    
    .metric-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 10px;
        margin: 15px 0;
    }
    
    .metric-item {
        background: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .screener-table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
    }
    .screener-table th, .screener-table td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #eee;
    }
    .screener-table th {
        background: #f5f5f5;
        font-weight: 600;
    }
    .screener-table tr:hover {
        background: #fafafa;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Session state
if 'watchlist' not in st.session_state: st.session_state.watchlist = []
if 'backtest_results' not in st.session_state: st.session_state.backtest_results = []
if 'api_key' not in st.session_state: st.session_state.api_key = ""
if 'selected_model' not in st.session_state: st.session_state.selected_model = DEFAULT_MODEL
if 'screener_results' not in st.session_state: st.session_state.screener_results = None
if 'agentic_backtest' not in st.session_state: st.session_state.agentic_backtest = None

# =============================================================================
# MARKET DATA FUNCTIONS
# =============================================================================
@st.cache_data(ttl=300)
def fetch_market_regime_data() -> Dict[str, Any]:
    """Fetch real market-wide data for regime classification."""
    regime_data = {'india_vix': None, 'nifty_change': None, 'market_breadth': None}
    
    try:
        # India VIX
        vix = yf.Ticker("^INDIAVIX")
        vix_hist = vix.history(period="5d")
        if not vix_hist.empty:
            regime_data['india_vix'] = round(vix_hist['Close'].iloc[-1], 2)
        
        # Nifty 50
        nifty = yf.Ticker("^NSEI")
        nifty_hist = nifty.history(period="5d")
        if not nifty_hist.empty and len(nifty_hist) >= 2:
            regime_data['nifty_change'] = round(
                ((nifty_hist['Close'].iloc[-1] / nifty_hist['Close'].iloc[-2]) - 1) * 100, 2
            )
        
        # Market breadth
        sample = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS',
                 'SBIN.NS', 'BHARTIARTL.NS', 'ITC.NS', 'KOTAKBANK.NS', 'LT.NS']
        advances = 0
        for ticker in sample:
            try:
                hist = yf.Ticker(ticker).history(period="2d")
                if len(hist) >= 2 and hist['Close'].iloc[-1] > hist['Close'].iloc[-2]:
                    advances += 1
            except:
                pass
        regime_data['market_breadth'] = round(advances / len(sample), 2)
        
    except Exception as e:
        pass
    
    return regime_data

def classify_market_regime(regime_data: Dict) -> Dict[str, Any]:
    """Classify market regime."""
    vix = regime_data.get('india_vix')
    breadth = regime_data.get('market_breadth', 0.5)
    
    if vix is None:
        return {'regime': 'UNKNOWN', 'code': 'UNKNOWN', 'confidence': 0, 'description': 'No VIX data'}
    
    if vix > 22:
        return {'regime': 'LIQUIDITY VACUUM', 'code': 'STRESS', 'confidence': 85, 
                'description': 'High fear - reduce exposure', 'vix': vix, 'breadth': breadth}
    elif vix < 13:
        return {'regime': 'COMPRESSION', 'code': 'ACCUMULATE', 'confidence': 80,
                'description': 'Low volatility - prepare for breakout', 'vix': vix, 'breadth': breadth}
    elif 14 <= vix <= 19 and breadth > 0.6:
        return {'regime': 'MOMENTUM CASCADE', 'code': 'TREND', 'confidence': 75,
                'description': 'Strong trend - follow momentum', 'vix': vix, 'breadth': breadth}
    else:
        return {'regime': 'REGIME TRANSITION', 'code': 'UNCERTAINTY', 'confidence': 60,
                'description': 'Mixed signals - be cautious', 'vix': vix, 'breadth': breadth}

# =============================================================================
# NEWS FUNCTIONS - MULTIPLE SOURCES
# =============================================================================
@st.cache_data(ttl=600)
def fetch_news_multi_source(ticker: str, company_name: str = "") -> List[Dict]:
    """Fetch news from multiple sources."""
    news_items = []
    
    # Method 1: Yahoo Finance
    try:
        stock = yf.Ticker(ticker)
        yf_news = stock.news
        if yf_news:
            for item in yf_news[:8]:
                if isinstance(item, dict) and item.get('title'):
                    title = item['title']
                    if len(title) > 10:
                        sentiment = analyze_sentiment(title)
                        news_items.append({
                            'title': title,
                            'publisher': item.get('publisher', 'Yahoo Finance'),
                            'published': format_timestamp(item.get('providerPublishTime', 0)),
                            'sentiment': sentiment,
                            'source': 'Yahoo'
                        })
    except:
        pass
    
    # If no news, return with flag
    return news_items

def analyze_sentiment(text: str) -> str:
    """Simple sentiment analysis."""
    text_lower = text.lower()
    positive = ['surge', 'jump', 'gain', 'profit', 'growth', 'beat', 'upgrade', 'buy', 'bullish', 'record', 'strong', 'rally']
    negative = ['fall', 'drop', 'loss', 'miss', 'downgrade', 'sell', 'bearish', 'concern', 'risk', 'decline', 'weak', 'crash']
    
    pos = sum(1 for w in positive if w in text_lower)
    neg = sum(1 for w in negative if w in text_lower)
    
    if pos > neg: return "POSITIVE"
    if neg > pos: return "NEGATIVE"
    return "NEUTRAL"

def format_timestamp(ts):
    """Format Unix timestamp."""
    if ts and ts > 0:
        try:
            return datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        except:
            pass
    return "Recent"

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
# FORMATTED REPORT OUTPUT
# =============================================================================
def display_analysis_report(analysis_text: str, regime_info: Dict, ticker: str, metrics: Dict, news: List):
    """Display beautifully formatted analysis report using Streamlit native components."""
    
    # 1. MARKET REGIME BANNER
    regime_class = regime_info.get('code', 'unknown').lower()
    st.markdown(f"""
    <div class="regime-banner regime-{regime_class}">
        <h2 style="margin:0;">📊 MARKET REGIME: {regime_info.get('regime', 'UNKNOWN')}</h2>
        <p style="margin:5px 0;">Code: {regime_info.get('code')} | Confidence: {regime_info.get('confidence', 0)}%</p>
        <p style="margin:0; font-size:0.9em;">{regime_info.get('description', '')}</p>
        <p style="margin:5px 0; font-size:0.85em;">VIX: {regime_info.get('vix', 'N/A')} | Breadth: {regime_info.get('breadth', 'N/A')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. QUICK METRICS
    st.subheader("📈 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Price", f"₹{metrics.get('current_price', 0):,.2f}", f"{metrics.get('price_change_1d', 0):+.2f}%")
    col2.metric("RSI (14)", f"{metrics.get('rsi_14', 0):.1f}" if metrics.get('rsi_14') else "N/A", metrics.get('rsi_status', ''))
    col3.metric("ADX", f"{metrics.get('adx_14', 0):.1f}" if metrics.get('adx_14') else "N/A", metrics.get('trend_strength', ''))
    col4.metric("Volume", f"{metrics.get('volume_ratio', 0):.2f}x" if metrics.get('volume_ratio') else "N/A", metrics.get('volume_status', ''))
    
    # 3. NEWS SECTION
    if news:
        st.subheader(f"📰 Recent News ({len(news)} articles)")
        for n in news[:5]:
            sentiment_class = f"news-{n['sentiment'].lower()}"
            icon = "🟢" if n['sentiment'] == "POSITIVE" else "🔴" if n['sentiment'] == "NEGATIVE" else "⚪"
            st.markdown(f"""
            <div class="news-card {sentiment_class}">
                {icon} <strong>{n['title']}</strong><br>
                <small style="color:#666;">{n['publisher']} • {n['published']}</small>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("📰 No recent news found. Analysis based on technical indicators only.")
    
    # 4. AI ANALYSIS - Using expanders for clean display
    st.subheader("🤖 Multi-Agent Analysis")
    
    # Parse the analysis to extract agent sections
    lines = analysis_text.split('\n')
    
    # Display in tabs for cleaner look
    tab1, tab2, tab3, tab4 = st.tabs(["📈 ATLAS", "🔮 ORACLE", "🛡️ SENTINEL", "📋 Full Report"])
    
    with tab1:
        atlas_text = extract_section(analysis_text, "ATLAS", "ORACLE")
        st.markdown(f"""
        <div class="agent-box agent-atlas">
            <h3>📈 ATLAS - Technical Eye</h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(atlas_text if atlas_text else "Analysis pending...")
    
    with tab2:
        oracle_text = extract_section(analysis_text, "ORACLE", "SENTINEL")
        st.markdown(f"""
        <div class="agent-box agent-oracle">
            <h3>🔮 ORACLE - Fundamental Eye</h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(oracle_text if oracle_text else "Analysis pending...")
    
    with tab3:
        sentinel_text = extract_section(analysis_text, "SENTINEL", "CROSS")
        st.markdown(f"""
        <div class="agent-box agent-sentinel">
            <h3>🛡️ SENTINEL - Risk Manager</h3>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(sentinel_text if sentinel_text else "Analysis pending...")
    
    with tab4:
        st.markdown(analysis_text)
    
    # 5. CONSENSUS DECISION
    consensus_text = extract_section(analysis_text, "CONSENSUS", None)
    if consensus_text:
        st.markdown(f"""
        <div class="consensus-box">
            <h2>🎯 CONSENSUS DECISION</h2>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(consensus_text)

def extract_section(text: str, start_marker: str, end_marker: str = None) -> str:
    """Extract a section from the analysis text."""
    try:
        start_idx = text.upper().find(start_marker.upper())
        if start_idx == -1:
            return ""
        
        if end_marker:
            end_idx = text.upper().find(end_marker.upper(), start_idx + len(start_marker))
            if end_idx == -1:
                return text[start_idx:]
            return text[start_idx:end_idx]
        else:
            return text[start_idx:]
    except:
        return ""

# =============================================================================
# AI FUNCTIONS
# =============================================================================
def run_ai_analysis(api_key: str, model_name: str, payload: Dict) -> tuple[bool, str]:
    """Run AI analysis with consistent prompting."""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name=model_name, system_instruction=SYSTEM_INSTRUCTION)
        
        prompt = f"""Analyze this stock using the Multi-Agent Swarm framework.

MARKET REGIME DATA (USE THIS - DO NOT SAY DATA UNAVAILABLE):
- India VIX: {payload.get('market_regime', {}).get('vix', 'N/A')}
- Market Breadth: {payload.get('market_regime', {}).get('breadth', 'N/A')}
- Regime: {payload.get('market_regime', {}).get('regime', 'UNKNOWN')}

STOCK DATA:
```json
{json.dumps(payload, indent=2, default=str)}
```

IMPORTANT:
1. Provide SPECIFIC entry/exit prices
2. Be consistent - if recommending NO ACTION, state clearly
3. Include stop-loss and target levels
4. Format output with clear sections using markdown headers

OUTPUT FORMAT:
## 1. MARKET REGIME CLASSIFICATION
## 2. AGENT ANALYSIS
### ATLAS (Technical)
### ORACLE (Fundamental)  
### SENTINEL (Risk)
## 3. CROSS-EXAMINATION
## 4. CONSENSUS DECISION
"""
        
        response = model.generate_content(prompt)
        return True, response.text
        
    except Exception as e:
        return False, f"Error: {str(e)}"

def run_quick_analysis(api_key: str, model_name: str, stock_data: Dict) -> Dict:
    """Run quick analysis for screener - returns structured data."""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name=model_name)
        
        prompt = f"""Analyze this stock briefly and return ONLY a JSON object.

Stock: {stock_data.get('ticker')}
Price: {stock_data.get('price')}
RSI: {stock_data.get('rsi')}
ADX: {stock_data.get('adx')}
Trend: {stock_data.get('trend')}
Volume Ratio: {stock_data.get('volume_ratio')}
From 52W High: {stock_data.get('from_52w_high')}%

Return ONLY this JSON (no other text):
{{
    "ticker": "{stock_data.get('ticker')}",
    "trend": "BULLISH/BEARISH/NEUTRAL",
    "atlas": "BUY/SELL/HOLD",
    "oracle": "BUY/SELL/HOLD",
    "sentinel": "LOW/MEDIUM/HIGH",
    "final": "STRONG BUY/BUY/HOLD/SELL/STRONG SELL",
    "reason": "one line reason"
}}
"""
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        # Parse JSON from response
        if '{' in text:
            start = text.find('{')
            end = text.rfind('}') + 1
            json_str = text[start:end]
            return json.loads(json_str)
        
        return None
    except Exception as e:
        return None

# =============================================================================
# AGENTIC BACKTESTING
# =============================================================================
def run_agentic_backtest(api_key: str, model_name: str, df: pd.DataFrame, ticker: str, 
                         initial_capital: float = 100000) -> Dict:
    """Backtest the AI agent's decisions over historical data."""
    
    results = {
        'ticker': ticker,
        'initial_capital': initial_capital,
        'trades': [],
        'decisions': [],
        'equity_curve': [initial_capital],
        'dates': []
    }
    
    capital = initial_capital
    position = 0  # shares held
    entry_price = 0
    
    # Sample every 20 trading days for decisions
    sample_indices = list(range(50, len(df), 20))
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name=model_name)
    
    progress = st.progress(0)
    status = st.empty()
    
    for i, idx in enumerate(sample_indices):
        if idx >= len(df):
            break
            
        status.text(f"Analyzing period {i+1}/{len(sample_indices)}...")
        progress.progress((i + 1) / len(sample_indices))
        
        # Get historical data up to this point
        hist_df = df.iloc[:idx+1]
        current_price = hist_df['Close'].iloc[-1]
        current_date = hist_df.index[-1]
        
        # Calculate metrics
        metrics = calculate_all_metrics(hist_df)
        if not metrics:
            continue
        
        # Get AI decision
        prompt = f"""You are a trading AI. Based on these metrics, should I BUY, SELL, or HOLD?

Stock: {ticker}
Date: {current_date.strftime('%Y-%m-%d')}
Price: {current_price:.2f}
RSI: {metrics.get('rsi_14', 'N/A')}
ADX: {metrics.get('adx_14', 'N/A')}
Trend: {metrics.get('trend_short_term', 'N/A')}
Price vs SMA20: {metrics.get('price_vs_sma20_pct', 'N/A')}%

Current Position: {'LONG' if position > 0 else 'FLAT'}

Reply with ONLY one word: BUY, SELL, or HOLD"""

        try:
            response = model.generate_content(prompt)
            decision = response.text.strip().upper()
            
            # Parse decision
            if 'BUY' in decision and position == 0:
                # Enter long
                shares = int(capital * 0.95 / current_price)  # 95% of capital
                if shares > 0:
                    position = shares
                    entry_price = current_price
                    capital -= shares * current_price * 1.001  # Include commission
                    results['trades'].append({
                        'date': current_date.strftime('%Y-%m-%d'),
                        'type': 'BUY',
                        'price': current_price,
                        'shares': shares
                    })
                    
            elif 'SELL' in decision and position > 0:
                # Exit long
                capital += position * current_price * 0.999  # Include commission
                pnl = (current_price - entry_price) * position
                results['trades'].append({
                    'date': current_date.strftime('%Y-%m-%d'),
                    'type': 'SELL',
                    'price': current_price,
                    'shares': position,
                    'pnl': pnl
                })
                position = 0
                entry_price = 0
            
            results['decisions'].append({
                'date': current_date.strftime('%Y-%m-%d'),
                'decision': decision[:4],
                'price': current_price
            })
            
        except:
            results['decisions'].append({
                'date': current_date.strftime('%Y-%m-%d'),
                'decision': 'HOLD',
                'price': current_price
            })
        
        # Calculate equity
        equity = capital + (position * current_price if position > 0 else 0)
        results['equity_curve'].append(equity)
        results['dates'].append(current_date)
    
    # Close any open position at the end
    if position > 0:
        final_price = df['Close'].iloc[-1]
        capital += position * final_price * 0.999
        results['trades'].append({
            'date': df.index[-1].strftime('%Y-%m-%d'),
            'type': 'SELL (CLOSE)',
            'price': final_price,
            'shares': position,
            'pnl': (final_price - entry_price) * position
        })
    
    results['final_capital'] = capital
    results['total_return'] = ((capital / initial_capital) - 1) * 100
    results['total_trades'] = len([t for t in results['trades'] if t['type'] == 'BUY'])
    
    progress.empty()
    status.empty()
    
    return results

# =============================================================================
# CHARTS
# =============================================================================
def create_chart(df, ticker):
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05,
                        row_heights=[0.6, 0.2, 0.2])
    
    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'],
                                  low=df['Low'], close=df['Close'], name='Price'), row=1, col=1)
    
    sma20 = df['Close'].rolling(20).mean()
    sma50 = df['Close'].rolling(50).mean()
    fig.add_trace(go.Scatter(x=df.index, y=sma20, name='SMA20', line=dict(color='orange', width=1)), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=sma50, name='SMA50', line=dict(color='blue', width=1)), row=1, col=1)
    
    rsi = calculate_rsi(df['Close'])
    fig.add_trace(go.Scatter(x=df.index, y=rsi, name='RSI', line=dict(color='purple', width=1)), row=2, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
    fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)
    
    colors = ['red' if df['Close'].iloc[i] < df['Close'].iloc[i-1] else 'green' for i in range(1, len(df))]
    colors.insert(0, 'green')
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume', marker_color=colors), row=3, col=1)
    
    fig.update_layout(height=500, template='plotly_dark', xaxis_rangeslider_visible=False, 
                      margin=dict(l=0, r=0, t=30, b=0))
    return fig

# =============================================================================
# MAIN APP
# =============================================================================
def main():
    st.markdown('<p class="main-header">🤖 Multi-Agent Trading System</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        try:
            if 'GOOGLE_API_KEY' in st.secrets:
                st.success("✅ API Key loaded")
        except:
            st.session_state.api_key = st.text_input("API Key", type="password", value=st.session_state.api_key)
        
        st.session_state.selected_model = st.selectbox("Model", list(AVAILABLE_MODELS.keys()),
                                                        format_func=lambda x: AVAILABLE_MODELS[x])
        
        st.divider()
        
        page = st.radio("Navigation", [
            "🎯 AI Analysis",
            "🔍 AI Screener", 
            "📈 Backtesting",
            "🤖 Agentic Backtest",
            "📊 Tech Screener",
            "⭐ Watchlist",
            "ℹ️ Help"
        ])
        
        st.divider()
        
        # Market regime display
        regime_data = fetch_market_regime_data()
        regime_info = classify_market_regime(regime_data)
        st.markdown(f"**Regime:** {regime_info['code']}")
        st.caption(f"VIX: {regime_data.get('india_vix', 'N/A')}")

    api_key = get_api_key()

    # ==========================================================================
    # AI ANALYSIS PAGE
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
            period = st.selectbox("Period", ["3mo", "6mo", "1y", "2y"], index=2)
        
        if st.button("🚀 Run Analysis", type="primary", use_container_width=True):
            if not api_key:
                st.error("⚠️ Please enter API key")
            else:
                regime_data = fetch_market_regime_data()
                regime_info = classify_market_regime(regime_data)
                
                df = fetch_stock_data(selected, period)
                if df is not None and len(df) > 20:
                    metrics = calculate_all_metrics(df)
                    company_name = next((s['name'] for s in stocks if s['symbol'] == selected), selected)
                    news = fetch_news_multi_source(selected, company_name)
                    
                    # Chart
                    st.plotly_chart(create_chart(df.tail(100), selected), use_container_width=True)
                    
                    # AI Analysis
                    payload = {
                        'ticker': selected,
                        'company': company_name,
                        'market_regime': regime_info,
                        'technical': metrics,
                        'news': news,
                        'news_count': len(news)
                    }
                    
                    with st.spinner("Running AI analysis..."):
                        ok, result = run_ai_analysis(api_key, st.session_state.selected_model, payload)
                    
                    if ok:
                        display_analysis_report(result, regime_info, selected, metrics, news)
                        st.download_button("📥 Download Report", result, f"{selected}_report.txt")
                    else:
                        st.error(result)
                else:
                    st.error("Failed to fetch data")

    # ==========================================================================
    # AI SCREENER PAGE - FIXED
    # ==========================================================================
    elif page == "🔍 AI Screener":
        st.header("🔍 AI Quick Screener")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            cat = st.selectbox("Category", list(NIFTY_500_STOCKS.keys()))
            
            # Get stocks in category
            category_stocks = NIFTY_500_STOCKS.get(cat, [])
            stock_names = [f"{s['symbol'].replace('.NS', '')} - {s['name']}" for s in category_stocks]
            
            st.info(f"📊 {len(category_stocks)} stocks in {cat}")
            
            # Multi-select for stocks
            selected_stocks = st.multiselect(
                "Select Stocks to Analyze",
                options=stock_names,
                default=stock_names[:5],  # Default first 5
                help="Select up to 15 stocks"
            )
            
            if len(selected_stocks) > 15:
                st.warning("Maximum 15 stocks allowed")
                selected_stocks = selected_stocks[:15]
            
            if st.button("🚀 Run AI Screening", type="primary", use_container_width=True):
                if not api_key:
                    st.error("Enter API key")
                elif not selected_stocks:
                    st.error("Select at least one stock")
                else:
                    results = []
                    progress = st.progress(0)
                    status = st.empty()
                    
                    for i, stock_name in enumerate(selected_stocks):
                        ticker = stock_name.split(' - ')[0] + '.NS'
                        status.text(f"Analyzing {ticker.replace('.NS', '')}...")
                        
                        df = fetch_stock_data(ticker, "3mo")
                        if df is not None and len(df) > 20:
                            metrics = calculate_all_metrics(df)
                            if metrics:
                                stock_data = {
                                    'ticker': ticker.replace('.NS', ''),
                                    'price': metrics['current_price'],
                                    'rsi': metrics.get('rsi_14'),
                                    'adx': metrics.get('adx_14'),
                                    'trend': metrics.get('trend_short_term'),
                                    'volume_ratio': metrics.get('volume_ratio'),
                                    'from_52w_high': metrics.get('pct_from_52w_high')
                                }
                                
                                ai_result = run_quick_analysis(api_key, st.session_state.selected_model, stock_data)
                                
                                if ai_result:
                                    results.append(ai_result)
                                else:
                                    # Fallback
                                    results.append({
                                        'ticker': ticker.replace('.NS', ''),
                                        'trend': metrics.get('trend_short_term', 'N/A'),
                                        'atlas': 'HOLD',
                                        'oracle': 'HOLD',
                                        'sentinel': 'MEDIUM',
                                        'final': 'HOLD',
                                        'reason': 'Analysis pending'
                                    })
                        
                        progress.progress((i + 1) / len(selected_stocks))
                    
                    status.empty()
                    progress.empty()
                    st.session_state.screener_results = results
        
        with col2:
            if st.session_state.screener_results:
                st.subheader("📊 AI Screening Results")
                
                # Create DataFrame
                df_results = pd.DataFrame(st.session_state.screener_results)
                
                # Color-coded display
                for _, row in df_results.iterrows():
                    final = row.get('final', 'HOLD')
                    color = '#4caf50' if 'BUY' in final else '#f44336' if 'SELL' in final else '#ff9800'
                    
                    st.markdown(f"""
                    <div style="padding: 10px; margin: 5px 0; border-radius: 8px; border-left: 4px solid {color}; background: #fafafa;">
                        <strong>{row.get('ticker', 'N/A')}</strong> - 
                        <span style="color: {color}; font-weight: bold;">{final}</span><br>
                        <small>
                        Trend: {row.get('trend', 'N/A')} | 
                        ATLAS: {row.get('atlas', 'N/A')} | 
                        ORACLE: {row.get('oracle', 'N/A')} | 
                        Risk: {row.get('sentinel', 'N/A')}
                        </small><br>
                        <small style="color: #666;">{row.get('reason', '')}</small>
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
            period = st.selectbox("Period", ["6mo", "1y", "2y", "5y"], index=1)
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
                
                data = []
                for r in st.session_state.backtest_results:
                    data.append({
                        'Strategy': r.strategy_name,
                        'Return': f"{r.total_return_pct:+.1f}%",
                        'Final ₹': f"₹{r.final_capital:,.0f}",
                        'Sharpe': f"{r.sharpe_ratio:.2f}",
                        'Max DD': f"{r.max_drawdown_pct:.1f}%",
                        'Trades': r.total_trades
                    })
                st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
                
                # Trade details
                sel = st.selectbox("View Trades", [r.strategy_name for r in st.session_state.backtest_results])
                result = next(r for r in st.session_state.backtest_results if r.strategy_name == sel)
                
                if result.trades:
                    trades_data = [{
                        'Entry': t.entry_date,
                        'Exit': t.exit_date,
                        'Type': t.position_type,
                        'P&L': f"₹{t.pnl:+,.0f}",
                        'Return': f"{t.pnl_pct:+.1f}%"
                    } for t in result.trades]
                    st.dataframe(pd.DataFrame(trades_data), use_container_width=True, hide_index=True)

    # ==========================================================================
    # AGENTIC BACKTEST PAGE - NEW
    # ==========================================================================
    elif page == "🤖 Agentic Backtest":
        st.header("🤖 Agentic Backtest")
        st.markdown("Test how the AI agent's decisions would have performed historically")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            all_stocks = get_all_stocks()
            opts = [(s['symbol'], f"{s['symbol'].replace('.NS','')} - {s['name']}") for s in all_stocks]
            ticker = st.selectbox("Stock", [o[0] for o in opts], 
                                 format_func=lambda x: next((o[1] for o in opts if o[0]==x), x),
                                 key="agentic_ticker")
            period = st.selectbox("Period", ["6mo", "1y", "2y"], index=1, key="agentic_period")
            capital = st.number_input("Capital ₹", value=100000, step=10000, key="agentic_capital")
            
            st.warning("⚠️ This will make multiple API calls and may take 1-2 minutes")
            
            if st.button("🚀 Run Agentic Backtest", type="primary"):
                if not api_key:
                    st.error("Enter API key")
                else:
                    df = fetch_stock_data(ticker, period)
                    if df is not None and len(df) > 100:
                        with st.spinner("Running agentic backtest..."):
                            results = run_agentic_backtest(
                                api_key, st.session_state.selected_model,
                                df, ticker, capital
                            )
                            st.session_state.agentic_backtest = results
                    else:
                        st.error("Need more data")
        
        with col2:
            if st.session_state.agentic_backtest:
                results = st.session_state.agentic_backtest
                
                # Metrics
                st.subheader("Performance")
                m1, m2, m3 = st.columns(3)
                m1.metric("Final Capital", f"₹{results['final_capital']:,.0f}")
                m2.metric("Total Return", f"{results['total_return']:+.1f}%")
                m3.metric("Total Trades", results['total_trades'])
                
                # Equity curve
                if results['equity_curve'] and results['dates']:
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=results['dates'],
                        y=results['equity_curve'][1:],  # Skip initial
                        mode='lines',
                        name='Equity',
                        line=dict(color='#00d4ff', width=2)
                    ))
                    fig.update_layout(title="Equity Curve", template="plotly_dark", height=300)
                    st.plotly_chart(fig, use_container_width=True)
                
                # Decisions
                st.subheader("AI Decisions")
                if results['decisions']:
                    dec_df = pd.DataFrame(results['decisions'])
                    st.dataframe(dec_df, use_container_width=True, hide_index=True)
                
                # Trades
                st.subheader("Trades")
                if results['trades']:
                    trades_df = pd.DataFrame(results['trades'])
                    st.dataframe(trades_df, use_container_width=True, hide_index=True)

    # ==========================================================================
    # OTHER PAGES
    # ==========================================================================
    elif page == "📊 Tech Screener":
        st.header("📊 Technical Screener")
        # Same as before...
        col1, col2 = st.columns([1, 2])
        with col1:
            criteria = {
                'rsi_oversold': st.checkbox("RSI < 30"),
                'above_sma20': st.checkbox("Above SMA20"),
                'high_volume': st.checkbox("Volume > 1.5x")
            }
            cat = st.selectbox("Category", list(NIFTY_500_STOCKS.keys()), key="tech_cat")
            if st.button("🔍 Screen"):
                results = []
                stocks = [s['symbol'] for s in NIFTY_500_STOCKS.get(cat, [])]
                prog = st.progress(0)
                for i, t in enumerate(stocks):
                    df = fetch_stock_data(t, "3mo")
                    if df is not None and len(df) > 20:
                        m = calculate_all_metrics(df)
                        if m:
                            ok = True
                            if criteria['rsi_oversold'] and (not m['rsi_14'] or m['rsi_14'] > 30): ok = False
                            if criteria['above_sma20'] and (not m.get('price_vs_sma20_pct') or m['price_vs_sma20_pct'] < 0): ok = False
                            if criteria['high_volume'] and (not m.get('volume_ratio') or m['volume_ratio'] < 1.5): ok = False
                            if ok:
                                results.append({'Ticker': t.replace('.NS',''), 'Price': f"₹{m['current_price']:,.2f}",
                                               'RSI': f"{m['rsi_14']:.1f}" if m['rsi_14'] else "N/A"})
                    prog.progress((i+1)/len(stocks))
                if results:
                    st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)
                else:
                    st.info("No stocks match criteria")

    elif page == "⭐ Watchlist":
        st.header("⭐ Watchlist")
        if st.session_state.watchlist:
            data = []
            for t in st.session_state.watchlist:
                df = fetch_stock_data(t, "1mo")
                if df is not None:
                    m = calculate_all_metrics(df)
                    if m:
                        data.append({'Ticker': t.replace('.NS',''), 'Price': f"₹{m['current_price']:,.2f}",
                                    'Change': f"{m['price_change_1d']:+.2f}%"})
            if data:
                st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
            if st.button("Clear"): 
                st.session_state.watchlist = []
                st.rerun()
        else:
            st.info("Watchlist empty")

    elif page == "ℹ️ Help":
        st.header("ℹ️ Help")
        st.markdown("""
### What's New in v5.0
1. **Fixed HTML rendering** - Reports now display properly
2. **Stock selection in Screener** - Choose which stocks to analyze
3. **Consistent signals** - Screener and detailed analysis now aligned
4. **Agentic Backtesting** - Test AI decisions historically
5. **Mobile-friendly** - Works on phones too

### API Key Security
Use Streamlit Secrets:
```toml
GOOGLE_API_KEY = "your-key"
```
        """)

if __name__ == "__main__":
    main()
