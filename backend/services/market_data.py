import yfinance as yf

def get_stock_price(symbol, market):
    if market == "IN":
        symbol = f"{symbol}.NS"

    stock = yf.Ticker(symbol)
    hist = stock.history(period="1d")

    if hist.empty:
        return {"error": "Invalid symbol"}

    return {
        "symbol": symbol,
        "price": round(hist["Close"][0], 2)
    }
