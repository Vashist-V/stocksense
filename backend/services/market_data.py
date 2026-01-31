from services.decision_engine import generate_decision
from services.indicators import calculate_indicators
import yfinance as yf

def get_stock_analysis(symbol, market):
    if market == "IN":
        symbol = f"{symbol}.NS"

    stock = yf.Ticker(symbol)
    df = stock.history(period="6mo")

    if df.empty:
        return {"error": "Invalid symbol"}

    indicators = calculate_indicators(df)
    decision = generate_decision(indicators)

    latest_price = round(df["Close"].iloc[-1], 2)

    return {
        "symbol": symbol,
        "price": latest_price,
        "indicators": indicators,
        "decision": decision
    }
