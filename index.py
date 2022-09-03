from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    supports_credentials = True
)

app.config["JSON_AS_ASCII"] = False

from api import blueprint as api_bp
app.register_blueprint(api_bp)

@app.route("/")
def index():
    return render_template("index.html")