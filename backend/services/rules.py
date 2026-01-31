def decision_engine(rsi, trend):
    if rsi < 30 and trend == "up":
        return "BUY"
    if rsi > 70:
        return "SELL"
    return "HOLD"
