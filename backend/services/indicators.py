import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

def calculate_indicators(df: pd.DataFrame):
    close = df["Close"]

    rsi = RSIIndicator(close, window=14).rsi().iloc[-1]

    sma50 = SMAIndicator(close, window=50).sma_indicator().iloc[-1]
    sma200 = SMAIndicator(close, window=200).sma_indicator().iloc[-1]

    trend = "up" if sma50 > sma200 else "down"

    return {
        "rsi": round(rsi, 2),
        "sma50": round(sma50, 2),
        "sma200": round(sma200, 2),
        "trend": trend
    }
