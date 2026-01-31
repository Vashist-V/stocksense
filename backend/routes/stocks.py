from flask import Blueprint, request, jsonify
from services.market_data import get_stock_analysis

stocks_bp = Blueprint("stocks", __name__)

@stocks_bp.route("/price")
def price():
    symbol = request.args.get("symbol")
    market = request.args.get("market")  
    data = get_stock_analysis(symbol, market)
    return jsonify(data)

@stocks_bp.route("/analysis")
def analysis():
    symbol = request.args.get("symbol")
    market = request.args.get("market")

    result = get_stock_analysis(symbol, market)
    return jsonify(result)