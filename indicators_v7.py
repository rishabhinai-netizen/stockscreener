"""
TECHNICAL INDICATORS MODULE v7.0
==================================
UPDATES:
- ✅ Fixed RSI division by zero error
- ✅ Added safety checks for all division operations
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, Optional


def calculate_rsi(data: pd.Series, period: int = 14) -> pd.Series:
    """
    Calculate Relative Strength Index with division-by-zero protection.
    
    v7.0 FIX: Handles cases where stocks don't move (loss = 0)
    """
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    # FIX: Prevent division by zero
    # When loss is 0 or very small, RSI should be 100 (all gains, no losses)
    rs = gain / loss.replace(0, np.finfo(float).eps)  # Replace 0 with tiny number
    rsi = 100 - (100 / (1 + rs))
    
    # Handle edge cases
    rsi = rsi.fillna(50)  # Neutral RSI if calculation fails
    rsi = rsi.clip(0, 100)  # Ensure RSI stays in 0-100 range
    
    return rsi


def calculate_macd(data: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> Dict[str, pd.Series]:
    """Calculate MACD indicator."""
    exp1 = data.ewm(span=fast, adjust=False).mean()
    exp2 = data.ewm(span=slow, adjust=False).mean()
    macd_line = exp1 - exp2
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram = macd_line - signal_line
    return {'macd': macd_line, 'signal': signal_line, 'histogram': histogram}


def calculate_bollinger_bands(data: pd.Series, period: int = 20, std_dev: int = 2) -> Dict[str, pd.Series]:
    """Calculate Bollinger Bands with division protection."""
    sma = data.rolling(window=period).mean()
    std = data.rolling(window=period).std()
    upper = sma + (std * std_dev)
    lower = sma - (std * std_dev)
    
    # Protect against division by zero in width calculation
    width = ((upper - lower) / sma.replace(0, np.finfo(float).eps)) * 100
    width = width.fillna(0)
    
    return {'upper': upper, 'middle': sma, 'lower': lower, 'width': width}


def calculate_adx(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Average Directional Index with safety checks."""
    plus_dm = high.diff()
    minus_dm = low.diff()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm > 0] = 0
    
    tr1 = high - low
    tr2 = abs(high - close.shift())
    tr3 = abs(low - close.shift())
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    
    atr = tr.rolling(window=period).mean()
    
    # Protect against division by zero
    atr_safe = atr.replace(0, np.finfo(float).eps)
    plus_di = 100 * (plus_dm.rolling(window=period).mean() / atr_safe)
    minus_di = abs(100 * (minus_dm.rolling(window=period).mean() / atr_safe))
    
    # Protect against division by zero in DX calculation
    di_sum = (plus_di + minus_di).replace(0, np.finfo(float).eps)
    dx = (abs(plus_di - minus_di) / di_sum) * 100
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
    """Calculate Stochastic Oscillator with division protection."""
    lowest_low = low.rolling(window=k_period).min()
    highest_high = high.rolling(window=k_period).max()
    
    # Protect against division by zero
    range_val = (highest_high - lowest_low).replace(0, np.finfo(float).eps)
    k = 100 * (close - lowest_low) / range_val
    k = k.fillna(50).clip(0, 100)
    
    d = k.rolling(window=d_period).mean()
    return {'k': k, 'd': d}


def calculate_obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Calculate On-Balance Volume."""
    obv = (np.sign(close.diff()) * volume).fillna(0).cumsum()
    return obv


def calculate_vwap(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Calculate Volume Weighted Average Price with safety."""
    typical_price = (high + low + close) / 3
    
    # Protect against zero volume
    volume_safe = volume.replace(0, np.finfo(float).eps)
    vwap = (typical_price * volume).cumsum() / volume_safe.cumsum()
    
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
    """Calculate Rate of Change with division protection."""
    shifted = data.shift(period).replace(0, np.finfo(float).eps)
    return ((data - data.shift(period)) / shifted) * 100


def calculate_williams_r(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Williams %R with division protection."""
    highest_high = high.rolling(window=period).max()
    lowest_low = low.rolling(window=period).min()
    
    range_val = (highest_high - lowest_low).replace(0, np.finfo(float).eps)
    wr = -100 * (highest_high - close) / range_val
    
    return wr.fillna(-50).clip(-100, 0)


def calculate_cci(high: pd.Series, low: pd.Series, close: pd.Series, period: int = 20) -> pd.Series:
    """Calculate Commodity Channel Index with division protection."""
    typical_price = (high + low + close) / 3
    sma_tp = typical_price.rolling(window=period).mean()
    mean_deviation = typical_price.rolling(window=period).apply(lambda x: np.abs(x - x.mean()).mean())
    
    # Protect against division by zero
    mean_deviation_safe = mean_deviation.replace(0, np.finfo(float).eps)
    cci = (typical_price - sma_tp) / (0.015 * mean_deviation_safe)
    
    return cci.fillna(0)


def calculate_mfi(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, period: int = 14) -> pd.Series:
    """Calculate Money Flow Index with division protection."""
    typical_price = (high + low + close) / 3
    raw_money_flow = typical_price * volume
    
    positive_flow = pd.Series(0.0, index=close.index)
    negative_flow = pd.Series(0.0, index=close.index)
    
    for i in range(1, len(typical_price)):
        if typical_price.iloc[i] > typical_price.iloc[i-1]:
            positive_flow.iloc[i] = raw_money_flow.iloc[i]
        elif typical_price.iloc[i] < typical_price.iloc[i-1]:
            negative_flow.iloc[i] = raw_money_flow.iloc[i]
    
    positive_mf = positive_flow.rolling(window=period).sum()
    negative_mf = negative_flow.rolling(window=period).sum()
    
    # Protect against division by zero
    negative_mf_safe = negative_mf.replace(0, np.finfo(float).eps)
    mfi = 100 - (100 / (1 + positive_mf / negative_mf_safe))
    
    return mfi.fillna(50).clip(0, 100)


def calculate_all_metrics(df: pd.DataFrame, ticker: str) -> Optional[Dict[str, Any]]:
    """
    Calculate comprehensive technical metrics with error handling.
    
    v7.0: Enhanced error handling for all division operations
    """
    try:
        if df is None or len(df) < 30:
            return None
        
        # Ensure we have required columns
        required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        if not all(col in df.columns for col in required_columns):
            return None
        
        # Calculate indicators with try-except for each
        metrics = {}
        
        # Basic price metrics
        metrics['current_price'] = float(df['Close'].iloc[-1])
        metrics['price_change_1d'] = ((df['Close'].iloc[-1] / df['Close'].iloc[-2]) - 1) * 100 if len(df) >= 2 else 0
        metrics['price_change_5d'] = ((df['Close'].iloc[-1] / df['Close'].iloc[-6]) - 1) * 100 if len(df) >= 6 else 0
        
        # 52-week high/low
        metrics['high_52w'] = float(df['High'].max())
        metrics['low_52w'] = float(df['Low'].min())
        metrics['pct_from_52w_high'] = ((metrics['current_price'] / metrics['high_52w']) - 1) * 100
        metrics['pct_from_52w_low'] = ((metrics['current_price'] / metrics['low_52w']) - 1) * 100
        
        # Volume metrics with safety
        avg_volume = df['Volume'].iloc[-20:].mean()
        current_volume = df['Volume'].iloc[-1]
        metrics['volume_ratio'] = current_volume / avg_volume if avg_volume > 0 else 1.0
        
        # RSI with fix
        try:
            df['rsi_14'] = calculate_rsi(df['Close'], 14)
            metrics['rsi_14'] = float(df['rsi_14'].iloc[-1])
            
            if metrics['rsi_14'] < 30:
                metrics['rsi_status'] = 'OVERSOLD'
            elif metrics['rsi_14'] > 70:
                metrics['rsi_status'] = 'OVERBOUGHT'
            else:
                metrics['rsi_status'] = 'NEUTRAL'
        except Exception as e:
            metrics['rsi_14'] = 50.0
            metrics['rsi_status'] = 'ERROR'
        
        # MACD
        try:
            macd_data = calculate_macd(df['Close'])
            df['macd'] = macd_data['macd']
            df['macd_signal'] = macd_data['signal']
            df['macd_histogram'] = macd_data['histogram']
            
            if len(df) >= 2:
                if df['macd_histogram'].iloc[-1] > 0 and df['macd_histogram'].iloc[-2] <= 0:
                    metrics['macd_status'] = 'BULLISH_CROSSOVER'
                elif df['macd_histogram'].iloc[-1] < 0 and df['macd_histogram'].iloc[-2] >= 0:
                    metrics['macd_status'] = 'BEARISH_CROSSOVER'
                else:
                    metrics['macd_status'] = 'BULLISH' if df['macd_histogram'].iloc[-1] > 0 else 'BEARISH'
            else:
                metrics['macd_status'] = 'NEUTRAL'
        except Exception as e:
            metrics['macd_status'] = 'ERROR'
        
        # Moving Averages
        try:
            df['sma_20'] = calculate_sma(df['Close'], 20)
            df['ema_50'] = calculate_ema(df['Close'], 50)
            
            metrics['price_vs_sma20_pct'] = ((metrics['current_price'] / df['sma_20'].iloc[-1]) - 1) * 100
            
            # Trend determination
            if df['Close'].iloc[-1] > df['sma_20'].iloc[-1] > df['ema_50'].iloc[-1]:
                metrics['trend_short_term'] = 'BULLISH'
            elif df['Close'].iloc[-1] < df['sma_20'].iloc[-1] < df['ema_50'].iloc[-1]:
                metrics['trend_short_term'] = 'BEARISH'
            else:
                metrics['trend_short_term'] = 'NEUTRAL'
            
            metrics['trend_medium_term'] = 'BULLISH' if df['ema_50'].iloc[-1] > df['ema_50'].iloc[-10] else 'BEARISH'
        except Exception as e:
            metrics['trend_short_term'] = 'NEUTRAL'
            metrics['trend_medium_term'] = 'NEUTRAL'
            metrics['price_vs_sma20_pct'] = 0
        
        # ADX
        try:
            df['adx_14'] = calculate_adx(df['High'], df['Low'], df['Close'], 14)
            metrics['adx_14'] = float(df['adx_14'].iloc[-1])
            
            if metrics['adx_14'] > 25:
                metrics['trend_strength'] = 'STRONG'
            elif metrics['adx_14'] > 20:
                metrics['trend_strength'] = 'MODERATE'
            else:
                metrics['trend_strength'] = 'WEAK'
        except Exception as e:
            metrics['adx_14'] = 20.0
            metrics['trend_strength'] = 'UNKNOWN'
        
        # ATR
        try:
            df['atr_14'] = calculate_atr(df['High'], df['Low'], df['Close'], 14)
            atr_value = float(df['atr_14'].iloc[-1])
            metrics['atr_pct'] = (atr_value / metrics['current_price']) * 100 if metrics['current_price'] > 0 else 0
        except Exception as e:
            metrics['atr_pct'] = 0
        
        # Volatility
        try:
            returns = df['Close'].pct_change()
            metrics['realized_volatility_20d'] = float(returns.iloc[-20:].std() * np.sqrt(252) * 100)
        except Exception as e:
            metrics['realized_volatility_20d'] = 0
        
        # Bollinger Bands
        try:
            bb = calculate_bollinger_bands(df['Close'], 20, 2)
            df['bb_upper'] = bb['upper']
            df['bb_middle'] = bb['middle']
            df['bb_lower'] = bb['lower']
        except Exception as e:
            pass
        
        return metrics
        
    except Exception as e:
        print(f"Error calculating metrics for {ticker}: {str(e)}")
        return None
