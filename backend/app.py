from flask import Flask
from flask_cors import CORS
from routes.stocks import stocks_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(stocks_bp, url_prefix="/api")

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
