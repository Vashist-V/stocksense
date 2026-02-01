from services.market_data import get_stock_analysis
from datetime import date

def analyze_portfolio(holdings):
    analysis = []

    for stock in holdings:
        data = get_stock_analysis(stock["symbol"], stock["market"])
        current_price = data["price"]

        invested = stock["buy_price"] * stock["quantity"]
        current_value = current_price * stock["quantity"]
        pnl = current_value - invested
        return_pct = (pnl / invested) * 100

        holding_days = (date.today() - date.fromisoformat(stock["buy_date"])).days

        analysis.append({
            "symbol": stock["symbol"],
            "market": stock["market"],
            "quantity": stock["quantity"],
            "buy_price": stock["buy_price"],
            "current_price": current_price,
            "invested": round(invested, 2),
            "current_value": round(current_value, 2),
            "pnl": round(pnl, 2),
            "return_pct": round(return_pct, 2),
            "holding_days": holding_days
        })

    return analysis
