"""
TECHNICAL INDICATORS MODULE
============================
Comprehensive technical analysis indicators for trading system.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, Optional


def calculate_rsi(data: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Relative Strength Index."""
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    # Avoid division by zero
    loss = loss.replace(0, np.nan)
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    
    # Fill NaNs resulting from division by zero or start of data
    return rsi.fillna(50)


def calculate_macd(data: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> Dict[str, pd.Series]:
    """Calculate MACD indicator."""
    exp1 = data.ewm(span=fast, adjust=False).mean()
    exp2 = data.ewm(span=slow, adjust=False).mean()
    macd_line = exp1 - exp2
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram = macd_line - signal_line
    return {'macd': macd_line, 'signal': signal_line, 'histogram': histogram}


def calculate_bollinger_bands(data: pd.Series, period: int = 20, std_dev: int = 2) -> Dict[str, pd.Series]:
    """Calculate Bollinger Bands."""
    sma = data.rolling(window=period).mean()
    std = data.rolling(window=period).std()
    upper = sma + (std * std_dev)
    lower = sma - (std * std_dev)
    # Avoid division by zero
    sma_safe = sma.replace(0, np.nan)
    width = ((upper - lower) / sma_safe) * 100
    return {'upper': upper, 'middle': sma, 'lower': lower, 'width': width.fillna(0)}


def calculate_adx(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Average Directional Index."""
    plus_dm = high.diff()
    minus_dm = low.diff()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm > 0] = 0
    
    tr1 = high - low
    tr2 = abs(high - close.shift())
    tr3 = abs(low - close.shift())
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    
    atr = tr.rolling(window=period).mean()
    
    # Avoid division by zero
    atr_safe = atr.replace(0, np.nan)
    
    plus_di = 100 * (plus_dm.rolling(window=period).mean() / atr_safe)
    minus_di = abs(100 * (minus_dm.rolling(window=period).mean() / atr_safe))
    
    sum_di = plus_di + minus_di
    sum_di_safe = sum_di.replace(0, np.nan)
    
    dx = (abs(plus_di - minus_di) / sum_di_safe) * 100
    adx = dx.rolling(window=period).mean()
    return adx.fillna(0)


def calculate_atr(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Average True Range."""
    tr1 = high - low
    tr2 = abs(high - close.shift())
    tr3 = abs(low - close.shift())
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    return tr.rolling(window=period).mean()


def calculate_stochastic(high: pd.Series, low: pd.Series, close: pd.Series, 
                         k_period: int = 14, d_period: int = 3) -> Dict[str, pd.Series]:
    """Calculate Stochastic Oscillator."""
    lowest_low = low.rolling(window=k_period).min()
    highest_high = high.rolling(window=k_period).max()
    
    denominator = highest_high - lowest_low
    denominator = denominator.replace(0, np.nan)
    
    k = 100 * (close - lowest_low) / denominator
    d = k.rolling(window=d_period).mean()
    return {'k': k.fillna(50), 'd': d.fillna(50)}


def calculate_obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Calculate On-Balance Volume."""
    obv = (np.sign(close.diff()) * volume).fillna(0).cumsum()
    return obv


def calculate_vwap(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Calculate Volume Weighted Average Price."""
    typical_price = (high + low + close) / 3
    cum_vol = volume.cumsum().replace(0, np.nan)
    vwap = (typical_price * volume).cumsum() / cum_vol
    return vwap.fillna(typical_price)


def calculate_ema(data: pd.Series, period: int) -> pd.Series:
    """Calculate Exponential Moving Average."""
    return data.ewm(span=period, adjust=False).mean()


def calculate_sma(data: pd.Series, period: int) -> pd.Series:
    """Calculate Simple Moving Average."""
    return data.rolling(window=period).mean()


def calculate_momentum(data: pd.Series, period: int = 10) -> pd.Series:
    """Calculate Momentum indicator."""
    return data.diff(period)


def calculate_roc(data: pd.Series, period: int = 10) -> pd.Series:
    """Calculate Rate of Change."""
    shift_data = data.shift(period).replace(0, np.nan)
    return ((data - shift_data) / shift_data) * 100


def calculate_williams_r(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Williams %R."""
    highest_high = high.rolling(window=period).max()
    lowest_low = low.rolling(window=period).min()
    denominator = highest_high - lowest_low
    denominator = denominator.replace(0, np.nan)
    wr = -100 * (highest_high - close) / denominator
    return wr.fillna(-50)


def calculate_cci(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 20) -> pd.Series:
    """Calculate Commodity Channel Index."""
    typical_price = (high + low + close) / 3
    sma_tp = typical_price.rolling(window=period).mean()
    mean_deviation = typical_price.rolling(window=period).apply(lambda x: np.abs(x - x.mean()).mean())
    mean_deviation = mean_deviation.replace(0, np.nan)
    cci = (typical_price - sma_tp) / (0.015 * mean_deviation)
    return cci.fillna(0)


def calculate_mfi(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Money Flow Index."""
    typical_price = (high + low + close) / 3
    raw_money_flow = typical_price * volume
    
    positive_flow = pd.Series(0.0, index=close.index)
    negative_flow = pd.Series(0.0, index=close.index)
    
    # We can use vectorization here for speed instead of loop
    price_diff = typical_price.diff()
    positive_flow[price_diff > 0] = raw_money_flow[price_diff > 0]
    negative_flow[price_diff < 0] = raw_money_flow[price_diff < 0]
    
    positive_mf = positive_flow.rolling(window=period).sum()
    negative_mf = negative_flow.rolling(window=period).sum()
    
    negative_mf = negative_mf.replace(0, np.nan)
    
    mfi = 100 - (100 / (1 + positive_mf / negative_mf))
    return mfi.fillna(50)


def calculate_all_metrics(df: pd.DataFrame) -> Optional[Dict[str, Any]]:
    """Calculate all technical indicators and metrics for a stock."""
    if df is None or df.empty:
        return None
    
    close = df['Close']
    high = df['High']
    low = df['Low']
    volume = df['Volume']
    
    # Moving Averages
    sma_5 = calculate_sma(close, 5)
    sma_10 = calculate_sma(close, 10)
    sma_20 = calculate_sma(close, 20)
    sma_50 = calculate_sma(close, 50)
    sma_200 = calculate_sma(close, 200) if len(close) >= 200 else pd.Series([np.nan] * len(close))
    ema_12 = calculate_ema(close, 12)
    ema_26 = calculate_ema(close, 26)
    
    # RSI
    rsi = calculate_rsi(close)
    
    # MACD
    macd = calculate_macd(close)
    
    # Bollinger Bands
    bb = calculate_bollinger_bands(close)
    
    # ADX
    adx = calculate_adx(high, low, close)
    
    # ATR
    atr = calculate_atr(high, low, close)
    
    # Stochastic
    stoch = calculate_stochastic(high, low, close)
    
    # VWAP
    vwap = calculate_vwap(high, low, close, volume)
    
    # OBV
    obv = calculate_obv(close, volume)
    
    # Volume metrics
    avg_volume_20 = volume.rolling(window=20).mean()
    # Handle division by zero for volume ratio
    avg_vol_safe = avg_volume_20.replace(0, np.nan)
    volume_ratio = volume / avg_vol_safe
    
    # Volatility
    returns = close.pct_change()
    realized_vol_20 = returns.rolling(window=20).std() * np.sqrt(252) * 100
    
    # Price metrics
    current_price = close.iloc[-1]
    price_vs_sma20 = ((current_price - sma_20.iloc[-1]) / sma_20.iloc[-1]) * 100 if pd.notna(sma_20.iloc[-1]) and sma_20.iloc[-1] != 0 else 0
    price_vs_sma50 = ((current_price - sma_50.iloc[-1]) / sma_50.iloc[-1]) * 100 if pd.notna(sma_50.iloc[-1]) and sma_50.iloc[-1] != 0 else 0
    
    # 52-week high/low
    high_52w = high.tail(252).max() if len(high) >= 252 else high.max()
    low_52w = low.tail(252).min() if len(low) >= 252 else low.min()
    pct_from_52w_high = ((current_price - high_52w) / high_52w) * 100
    pct_from_52w_low = ((current_price - low_52w) / low_52w) * 100
    
    # Support/Resistance (pivot points)
    recent_high = high.tail(20).max()
    recent_low = low.tail(20).min()
    pivot = (recent_high + recent_low + current_price) / 3
    r1 = 2 * pivot - recent_low
    s1 = 2 * pivot - recent_high
    r2 = pivot + (recent_high - recent_low)
    s2 = pivot - (recent_high - recent_low)
    
    # Trend detection
    trend_short = "BULLISH" if current_price > sma_20.iloc[-1] else "BEARISH" if pd.notna(sma_20.iloc[-1]) else "UNKNOWN"
    trend_medium = "BULLISH" if current_price > sma_50.iloc[-1] else "BEARISH" if pd.notna(sma_50.iloc[-1]) else "UNKNOWN"
    trend_long = "BULLISH" if pd.notna(sma_200.iloc[-1]) and current_price > sma_200.iloc[-1] else "BEARISH" if pd.notna(sma_200.iloc[-1]) else "UNKNOWN"
    
    # Golden/Death cross detection
    golden_cross = sma_50.iloc[-1] > sma_200.iloc[-1] if pd.notna(sma_200.iloc[-1]) else None
    
    return {
        # Price data
        'current_price': round(current_price, 2),
        'open': round(df['Open'].iloc[-1], 2),
        'high': round(high.iloc[-1], 2),
        'low': round(low.iloc[-1], 2),
        'prev_close': round(close.iloc[-2], 2) if len(close) > 1 else None,
        
        # Price changes
        'price_change_1d': round(returns.iloc[-1] * 100, 2) if pd.notna(returns.iloc[-1]) else 0,
        'price_change_5d': round((close.iloc[-1] / close.iloc[-5] - 1) * 100, 2) if len(close) >= 5 else 0,
        'price_change_20d': round((close.iloc[-1] / close.iloc[-20] - 1) * 100, 2) if len(close) >= 20 else 0,
        'price_change_50d': round((close.iloc[-1] / close.iloc[-50] - 1) * 100, 2) if len(close) >= 50 else 0,
        
        # Moving Averages
        'sma_5': round(sma_5.iloc[-1], 2) if pd.notna(sma_5.iloc[-1]) else None,
        'sma_10': round(sma_10.iloc[-1], 2) if pd.notna(sma_10.iloc[-1]) else None,
        'sma_20': round(sma_20.iloc[-1], 2) if pd.notna(sma_20.iloc[-1]) else None,
        'sma_50': round(sma_50.iloc[-1], 2) if pd.notna(sma_50.iloc[-1]) else None,
        'sma_200': round(sma_200.iloc[-1], 2) if pd.notna(sma_200.iloc[-1]) else None,
        'ema_12': round(ema_12.iloc[-1], 2) if pd.notna(ema_12.iloc[-1]) else None,
        'ema_26': round(ema_26.iloc[-1], 2) if pd.notna(ema_26.iloc[-1]) else None,
        
        'price_vs_sma20_pct': round(price_vs_sma20, 2),
        'price_vs_sma50_pct': round(price_vs_sma50, 2),
        
        # RSI
        'rsi_14': round(rsi.iloc[-1], 2) if pd.notna(rsi.iloc[-1]) else None,
        'rsi_status': 'OVERSOLD' if rsi.iloc[-1] < 30 else ('OVERBOUGHT' if rsi.iloc[-1] > 70 else 'NEUTRAL'),
        
        # MACD
        'macd_line': round(macd['macd'].iloc[-1], 4) if pd.notna(macd['macd'].iloc[-1]) else None,
        'macd_signal': round(macd['signal'].iloc[-1], 4) if pd.notna(macd['signal'].iloc[-1]) else None,
        'macd_histogram': round(macd['histogram'].iloc[-1], 4) if pd.notna(macd['histogram'].iloc[-1]) else None,
        'macd_status': 'BULLISH' if macd['histogram'].iloc[-1] > 0 else 'BEARISH',
        
        # Bollinger Bands
        'bb_upper': round(bb['upper'].iloc[-1], 2) if pd.notna(bb['upper'].iloc[-1]) else None,
        'bb_middle': round(bb['middle'].iloc[-1], 2) if pd.notna(bb['middle'].iloc[-1]) else None,
        'bb_lower': round(bb['lower'].iloc[-1], 2) if pd.notna(bb['lower'].iloc[-1]) else None,
        'bb_width': round(bb['width'].iloc[-1], 2) if pd.notna(bb['width'].iloc[-1]) else None,
        'bb_position': 'ABOVE_UPPER' if current_price > bb['upper'].iloc[-1] else ('BELOW_LOWER' if current_price < bb['lower'].iloc[-1] else 'WITHIN_BANDS'),
        
        # ADX
        'adx_14': round(adx.iloc[-1], 2) if pd.notna(adx.iloc[-1]) else None,
        'trend_strength': 'STRONG' if pd.notna(adx.iloc[-1]) and adx.iloc[-1] > 25 else ('MODERATE' if pd.notna(adx.iloc[-1]) and adx.iloc[-1] > 20 else 'WEAK'),
        
        # ATR
        'atr_14': round(atr.iloc[-1], 2) if pd.notna(atr.iloc[-1]) else None,
        'atr_pct': round((atr.iloc[-1] / current_price) * 100, 2) if pd.notna(atr.iloc[-1]) else None,
        
        # Stochastic
        'stoch_k': round(stoch['k'].iloc[-1], 2) if pd.notna(stoch['k'].iloc[-1]) else None,
        'stoch_d': round(stoch['d'].iloc[-1], 2) if pd.notna(stoch['d'].iloc[-1]) else None,
        
        # VWAP
        'vwap': round(vwap.iloc[-1], 2) if pd.notna(vwap.iloc[-1]) else None,
        'price_vs_vwap': 'ABOVE' if current_price > vwap.iloc[-1] else 'BELOW',
        
        # Volume
        'volume_current': int(volume.iloc[-1]),
        'volume_avg_20': int(avg_volume_20.iloc[-1]) if pd.notna(avg_volume_20.iloc[-1]) else None,
        'volume_ratio': round(volume_ratio.iloc[-1], 2) if pd.notna(volume_ratio.iloc[-1]) else None,
        'volume_status': 'HIGH' if pd.notna(volume_ratio.iloc[-1]) and volume_ratio.iloc[-1] > 1.5 else ('LOW' if pd.notna(volume_ratio.iloc[-1]) and volume_ratio.iloc[-1] < 0.5 else 'NORMAL'),
        
        # Volatility
        'realized_volatility_20d': round(realized_vol_20.iloc[-1], 2) if pd.notna(realized_vol_20.iloc[-1]) else None,
        'volatility_status': 'HIGH' if pd.notna(realized_vol_20.iloc[-1]) and realized_vol_20.iloc[-1] > 30 else ('LOW' if pd.notna(realized_vol_20.iloc[-1]) and realized_vol_20.iloc[-1] < 15 else 'MODERATE'),
        
        # 52-week metrics
        'high_52w': round(high_52w, 2),
        'low_52w': round(low_52w, 2),
        'pct_from_52w_high': round(pct_from_52w_high, 2),
        'pct_from_52w_low': round(pct_from_52w_low, 2),
        
        # Support/Resistance
        'pivot_point': round(pivot, 2),
        'resistance_1': round(r1, 2),
        'resistance_2': round(r2, 2),
        'support_1': round(s1, 2),
        'support_2': round(s2, 2),
        'recent_high_20d': round(recent_high, 2),
        'recent_low_20d': round(recent_low, 2),
        
        # Trend
        'trend_short_term': trend_short,
        'trend_medium_term': trend_medium,
        'trend_long_term': trend_long,
        'golden_cross': golden_cross,
        
        # Data info
        'data_start_date': df.index[0].strftime('%Y-%m-%d'),
        'data_end_date': df.index[-1].strftime('%Y-%m-%d'),
        'total_trading_days': len(df)
    }
