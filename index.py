from flask import Flask, jsonify, url_for, render_template

app = Flask(__name__)

from api import blueprint as api_bp
app.register_blueprint(api_bp)

@app.route("/")
def index():
    return render_template("index.html")