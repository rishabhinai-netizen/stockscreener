"""
BACKTESTING ENGINE MODULE
=========================
Simple but powerful backtesting engine for strategy validation.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from indicators import calculate_rsi, calculate_macd, calculate_sma, calculate_ema, calculate_bollinger_bands


@dataclass
class TradeResult:
    """Represents a single trade."""
    entry_date: str
    exit_date: str
    entry_price: float
    exit_price: float
    position_type: str  # 'LONG' or 'SHORT'
    pnl: float
    pnl_pct: float
    holding_days: int


@dataclass
class BacktestResult:
    """Complete backtest results."""
    strategy_name: str
    ticker: str
    start_date: str
    end_date: str
    initial_capital: float
    final_capital: float
    total_return: float
    total_return_pct: float
    annualized_return: float
    total_trades: int
    winning_trades: int
    losing_trades: int
    win_rate: float
    max_drawdown: float
    max_drawdown_pct: float
    sharpe_ratio: float
    sortino_ratio: float
    profit_factor: float
    avg_trade_pnl: float
    avg_winning_trade: float
    avg_losing_trade: float
    largest_win: float
    largest_loss: float
    avg_holding_period: float
    trades: List[TradeResult]
    equity_curve: pd.Series
    drawdown_curve: pd.Series
    benchmark_return: float


class BacktestEngine:
    """
    Simple backtesting engine for technical strategies.
    """
    
    def __init__(self, initial_capital: float = 100000, commission: float = 0.001):
        """
        Initialize backtesting engine.
        
        Args:
            initial_capital: Starting capital in INR
            commission: Commission per trade (0.1% = 0.001)
        """
        self.initial_capital = initial_capital
        self.commission = commission
    
    def _calculate_signals(self, df: pd.DataFrame, strategy: str) -> pd.DataFrame:
        """Generate buy/sell signals based on strategy."""
        signals = pd.DataFrame(index=df.index)
        signals['signal'] = 0
        
        close = df['Close']
        high = df['High']
        low = df['Low']
        volume = df['Volume']
        
        if strategy == "SMA Crossover (20/50)":
            sma_fast = calculate_sma(close, 20)
            sma_slow = calculate_sma(close, 50)
            signals['signal'] = np.where(sma_fast > sma_slow, 1, -1)
            
        elif strategy == "EMA Crossover (12/26)":
            ema_fast = calculate_ema(close, 12)
            ema_slow = calculate_ema(close, 26)
            signals['signal'] = np.where(ema_fast > ema_slow, 1, -1)
            
        elif strategy == "RSI Mean Reversion":
            rsi = calculate_rsi(close, 14)
            signals['signal'] = np.where(rsi < 30, 1, np.where(rsi > 70, -1, 0))
            
        elif strategy == "MACD Signal":
            macd = calculate_macd(close)
            signals['signal'] = np.where(macd['histogram'] > 0, 1, -1)
            
        elif strategy == "Bollinger Band Bounce":
            bb = calculate_bollinger_bands(close)
            signals['signal'] = np.where(close < bb['lower'], 1, 
                                        np.where(close > bb['upper'], -1, 0))
            
        elif strategy == "Golden Cross (50/200)":
            sma_50 = calculate_sma(close, 50)
            sma_200 = calculate_sma(close, 200)
            signals['signal'] = np.where(sma_50 > sma_200, 1, -1)
            
        elif strategy == "Triple EMA (5/13/26)":
            ema_5 = calculate_ema(close, 5)
            ema_13 = calculate_ema(close, 13)
            ema_26 = calculate_ema(close, 26)
            signals['signal'] = np.where((ema_5 > ema_13) & (ema_13 > ema_26), 1,
                                        np.where((ema_5 < ema_13) & (ema_13 < ema_26), -1, 0))
            
        elif strategy == "Volume Breakout":
            avg_vol = volume.rolling(20).mean()
            sma_20 = calculate_sma(close, 20)
            signals['signal'] = np.where((close > sma_20) & (volume > 1.5 * avg_vol), 1,
                                        np.where((close < sma_20) & (volume > 1.5 * avg_vol), -1, 0))
            
        elif strategy == "Buy and Hold":
            signals['signal'] = 1  # Always long
            
        return signals
    
    def run_backtest(self, df: pd.DataFrame, strategy: str, ticker: str = "UNKNOWN") -> BacktestResult:
        """
        Run backtest for a given strategy.
        
        Args:
            df: DataFrame with OHLCV data
            strategy: Strategy name
            ticker: Stock ticker symbol
            
        Returns:
            BacktestResult object with complete metrics
        """
        # Special handling for Buy and Hold
        if strategy == "Buy and Hold":
            return self._run_buy_and_hold(df, ticker)
        
        # Generate signals for other strategies
        signals = self._calculate_signals(df, strategy)
        
        # Initialize tracking variables
        capital = self.initial_capital
        position = 0  # 1 = long, -1 = short, 0 = flat
        entry_price = 0
        entry_date = None
        trades = []
        equity = [capital]
        
        close = df['Close']
        
        # Iterate through each day
        for i in range(1, len(df)):
            current_date = df.index[i]
            current_price = close.iloc[i]
            current_signal = signals['signal'].iloc[i]
            prev_signal = signals['signal'].iloc[i-1]
            
            # Check for signal change
            if current_signal != prev_signal and current_signal != 0:
                # Close existing position if any
                if position != 0:
                    exit_price = current_price * (1 - self.commission if position == 1 else 1 + self.commission)
                    
                    if position == 1:
                        pnl = (exit_price - entry_price) * (capital / entry_price)
                    else:
                        pnl = (entry_price - exit_price) * (capital / entry_price)
                    
                    pnl_pct = (pnl / capital) * 100
                    holding_days = (current_date - entry_date).days
                    
                    trades.append(TradeResult(
                        entry_date=entry_date.strftime('%Y-%m-%d'),
                        exit_date=current_date.strftime('%Y-%m-%d'),
                        entry_price=round(entry_price, 2),
                        exit_price=round(exit_price, 2),
                        position_type='LONG' if position == 1 else 'SHORT',
                        pnl=round(pnl, 2),
                        pnl_pct=round(pnl_pct, 2),
                        holding_days=holding_days
                    ))
                    
                    capital += pnl
                    position = 0
                
                # Open new position
                if current_signal == 1:  # Buy
                    position = 1
                    entry_price = current_price * (1 + self.commission)
                    entry_date = current_date
                elif current_signal == -1:  # Sell/Short
                    position = -1
                    entry_price = current_price * (1 - self.commission)
                    entry_date = current_date
            
            # Update equity
            if position == 1:
                unrealized_pnl = (current_price - entry_price) * (capital / entry_price)
                equity.append(capital + unrealized_pnl)
            elif position == -1:
                unrealized_pnl = (entry_price - current_price) * (capital / entry_price)
                equity.append(capital + unrealized_pnl)
            else:
                equity.append(capital)
        
        # Close any remaining position
        if position != 0:
            exit_price = close.iloc[-1]
            if position == 1:
                pnl = (exit_price - entry_price) * (capital / entry_price)
            else:
                pnl = (entry_price - exit_price) * (capital / entry_price)
            capital += pnl
            
            trades.append(TradeResult(
                entry_date=entry_date.strftime('%Y-%m-%d'),
                exit_date=df.index[-1].strftime('%Y-%m-%d'),
                entry_price=round(entry_price, 2),
                exit_price=round(exit_price, 2),
                position_type='LONG' if position == 1 else 'SHORT',
                pnl=round(pnl, 2),
                pnl_pct=round((pnl / capital) * 100, 2),
                holding_days=(df.index[-1] - entry_date).days
            ))
        
        # Create equity curve
        equity_curve = pd.Series(equity, index=df.index[:len(equity)])
        
        # Calculate drawdown
        rolling_max = equity_curve.expanding().max()
        drawdown = equity_curve - rolling_max
        drawdown_pct = (drawdown / rolling_max) * 100
        
        # Calculate metrics
        total_return = capital - self.initial_capital
        total_return_pct = (total_return / self.initial_capital) * 100
        
        # Annualized return
        days = (df.index[-1] - df.index[0]).days
        years = days / 365.25
        annualized_return = ((capital / self.initial_capital) ** (1 / years) - 1) * 100 if years > 0 else 0
        
        # Trade statistics
        total_trades = len(trades)
        winning_trades = len([t for t in trades if t.pnl > 0])
        losing_trades = len([t for t in trades if t.pnl < 0])
        win_rate = (winning_trades / total_trades * 100) if total_trades > 0 else 0
        
        # PnL statistics
        pnls = [t.pnl for t in trades]
        winning_pnls = [t.pnl for t in trades if t.pnl > 0]
        losing_pnls = [t.pnl for t in trades if t.pnl < 0]
        
        avg_trade_pnl = np.mean(pnls) if pnls else 0
        avg_winning_trade = np.mean(winning_pnls) if winning_pnls else 0
        avg_losing_trade = np.mean(losing_pnls) if losing_pnls else 0
        largest_win = max(pnls) if pnls else 0
        largest_loss = min(pnls) if pnls else 0
        
        # Profit factor
        gross_profit = sum(winning_pnls) if winning_pnls else 0
        gross_loss = abs(sum(losing_pnls)) if losing_pnls else 1
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else 0
        
        # Sharpe Ratio
        returns = equity_curve.pct_change().dropna()
        sharpe_ratio = (returns.mean() / returns.std() * np.sqrt(252)) if len(returns) > 0 and returns.std() > 0 else 0
        
        # Sortino Ratio
        negative_returns = returns[returns < 0]
        sortino_ratio = (returns.mean() / negative_returns.std() * np.sqrt(252)) if len(negative_returns) > 0 and negative_returns.std() > 0 else 0
        
        # Average holding period
        avg_holding_period = np.mean([t.holding_days for t in trades]) if trades else 0
        
        # Benchmark return (buy and hold)
        benchmark_return = ((close.iloc[-1] / close.iloc[0]) - 1) * 100
        
        return BacktestResult(
            strategy_name=strategy,
            ticker=ticker,
            start_date=df.index[0].strftime('%Y-%m-%d'),
            end_date=df.index[-1].strftime('%Y-%m-%d'),
            initial_capital=self.initial_capital,
            final_capital=round(capital, 2),
            total_return=round(total_return, 2),
            total_return_pct=round(total_return_pct, 2),
            annualized_return=round(annualized_return, 2),
            total_trades=total_trades,
            winning_trades=winning_trades,
            losing_trades=losing_trades,
            win_rate=round(win_rate, 2),
            max_drawdown=round(drawdown.min(), 2),
            max_drawdown_pct=round(drawdown_pct.min(), 2),
            sharpe_ratio=round(sharpe_ratio, 2),
            sortino_ratio=round(sortino_ratio, 2),
            profit_factor=round(profit_factor, 2),
            avg_trade_pnl=round(avg_trade_pnl, 2),
            avg_winning_trade=round(avg_winning_trade, 2),
            avg_losing_trade=round(avg_losing_trade, 2),
            largest_win=round(largest_win, 2),
            largest_loss=round(largest_loss, 2),
            avg_holding_period=round(avg_holding_period, 1),
            trades=trades,
            equity_curve=equity_curve,
            drawdown_curve=drawdown_pct,
            benchmark_return=round(benchmark_return, 2)
        )
    
    def _run_buy_and_hold(self, df: pd.DataFrame, ticker: str) -> BacktestResult:
        """Special method for Buy and Hold strategy."""
        close = df['Close']
        
        # Simple buy at start, sell at end
        entry_price = close.iloc[0] * (1 + self.commission)
        exit_price = close.iloc[-1] * (1 - self.commission)
        
        # Calculate returns
        total_return_pct = ((exit_price / entry_price) - 1) * 100
        final_capital = self.initial_capital * (1 + total_return_pct / 100)
        total_return = final_capital - self.initial_capital
        
        # Days and annualized return
        days = (df.index[-1] - df.index[0]).days
        years = days / 365.25
        annualized_return = ((final_capital / self.initial_capital) ** (1 / years) - 1) * 100 if years > 0 else 0
        
        # Equity curve (daily portfolio value)
        equity_values = [self.initial_capital]
        for i in range(1, len(df)):
            daily_return = close.iloc[i] / close.iloc[i-1]
            equity_values.append(equity_values[-1] * daily_return)
        equity_curve = pd.Series(equity_values, index=df.index[:len(equity_values)])
        
        # Drawdown
        rolling_max = equity_curve.expanding().max()
        drawdown = equity_curve - rolling_max
        drawdown_pct = (drawdown / rolling_max) * 100
        
        # Sharpe ratio
        returns = equity_curve.pct_change().dropna()
        sharpe_ratio = (returns.mean() / returns.std() * np.sqrt(252)) if len(returns) > 0 and returns.std() > 0 else 0
        
        # Single trade
        trade = TradeResult(
            entry_date=df.index[0].strftime('%Y-%m-%d'),
            exit_date=df.index[-1].strftime('%Y-%m-%d'),
            entry_price=round(entry_price, 2),
            exit_price=round(exit_price, 2),
            position_type='LONG',
            pnl=round(total_return, 2),
            pnl_pct=round(total_return_pct, 2),
            holding_days=days
        )
        
        return BacktestResult(
            strategy_name="Buy and Hold",
            ticker=ticker,
            start_date=df.index[0].strftime('%Y-%m-%d'),
            end_date=df.index[-1].strftime('%Y-%m-%d'),
            initial_capital=self.initial_capital,
            final_capital=round(final_capital, 2),
            total_return=round(total_return, 2),
            total_return_pct=round(total_return_pct, 2),
            annualized_return=round(annualized_return, 2),
            total_trades=1,
            winning_trades=1 if total_return > 0 else 0,
            losing_trades=0 if total_return > 0 else 1,
            win_rate=100.0 if total_return > 0 else 0.0,
            max_drawdown=round(drawdown.min(), 2),
            max_drawdown_pct=round(drawdown_pct.min(), 2),
            sharpe_ratio=round(sharpe_ratio, 2),
            sortino_ratio=round(sharpe_ratio, 2),  # Simplified
            profit_factor=999.0 if total_return > 0 else 0.0,
            avg_trade_pnl=round(total_return, 2),
            avg_winning_trade=round(total_return, 2) if total_return > 0 else 0,
            avg_losing_trade=round(total_return, 2) if total_return < 0 else 0,
            largest_win=round(total_return, 2) if total_return > 0 else 0,
            largest_loss=round(total_return, 2) if total_return < 0 else 0,
            avg_holding_period=float(days),
            trades=[trade],
            equity_curve=equity_curve,
            drawdown_curve=drawdown_pct,
            benchmark_return=round(total_return_pct, 2)
        )
    
    def compare_strategies(self, df: pd.DataFrame, strategies: List[str], ticker: str = "UNKNOWN") -> List[BacktestResult]:
        """Run backtest for multiple strategies and return comparison."""
        results = []
        for strategy in strategies:
            result = self.run_backtest(df, strategy, ticker)
            results.append(result)
        return results


# Available strategies
AVAILABLE_STRATEGIES = [
    "Buy and Hold",
    "SMA Crossover (20/50)",
    "EMA Crossover (12/26)",
    "RSI Mean Reversion",
    "MACD Signal",
    "Bollinger Band Bounce",
    "Golden Cross (50/200)",
    "Triple EMA (5/13/26)",
    "Volume Breakout"
]
