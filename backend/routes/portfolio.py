from flask import Blueprint, request, jsonify
from services.market_data import get_stock_price

portfolio_bp = Blueprint("portfolio", __name__)

@portfolio_bp.route("/analyze")
def analyze():
    holdings = request.json
    results = []

    for h in holdings:
        price = get_stock_price(h["symbol"], h["market"])["price"]
        pnl = (price - h["buy_price"]) * h["quantity"]

        results.append({
            **h,
            "current_price": price,
            "pnl": round(pnl, 2)
        })

    return jsonify(results)
