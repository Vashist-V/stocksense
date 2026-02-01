from flask import Blueprint, request, jsonify
from services.portfolio_service import fetch_user_portfolio
from services.portfolio_analysis import analyze_portfolio

portfolio_bp = Blueprint("portfolio", __name__)

@portfolio_bp.route("/portfolio/analyze")
def analyze():
    user_id = request.args.get("user_id")
    holdings = fetch_user_portfolio(user_id)
    analysis = analyze_portfolio(holdings)
    return jsonify(analysis)
