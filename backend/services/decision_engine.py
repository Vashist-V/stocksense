def generate_decision(indicators):
    rsi = indicators["rsi"]
    trend = indicators["trend"]

    if rsi < 30 and trend == "up":
        return {
            "signal": "BUY",
            "confidence": "high",
            "reason": "Stock is oversold with an overall upward trend"
        }

    if rsi > 70 and trend == "down":
        return {
            "signal": "SELL",
            "confidence": "high",
            "reason": "Stock is overbought in a downward trend"
        }

    return {
        "signal": "HOLD",
        "confidence": "medium",
        "reason": "No strong momentum imbalance detected"
    }
