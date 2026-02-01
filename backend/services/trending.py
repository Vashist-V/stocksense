import yfinance as yf
from data.universe import INDIA_STOCKS, US_STOCKS

def fetch_trending(market, period="5d"):
    stocks = INDIA_STOCKS if market == "IN" else US_STOCKS
    results = []

    for symbol in stocks:
        ticker = f"{symbol}.NS" if market == "IN" else symbol
        data = yf.Ticker(ticker).history(period=period)

        if data.empty:
            continue

        start_price = data["Close"].iloc[0]
        end_price = data["Close"].iloc[-1]

        change_pct = ((end_price - start_price) / start_price) * 100

        results.append({
            "symbol": symbol,
            "price": round(end_price, 2),
            "change_pct": round(change_pct, 2)
        })

    gainers = sorted(results, key=lambda x: x["change_pct"], reverse=True)[:5]
    losers = sorted(results, key=lambda x: x["change_pct"])[:5]

    return {
        "gainers": gainers,
        "losers": losers
    }
