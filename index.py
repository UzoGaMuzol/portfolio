from flask import Flask, render_template

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False

from api import blueprint as api_bp
app.register_blueprint(api_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.after_request
def after_request(response):
    response.headers.update({'Access-Control-Allow-Origin': '*'})
    return response