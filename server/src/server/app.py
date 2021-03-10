from flask import Flask, jsonify

import server

app = Flask(__name__)


@app.route("/version")
def version():
    return jsonify(Version=server.__version__)


@app.route("/classify")
def classify():
    return jsonify(Survived=0)


@app.route("/")
def hello():
    return "Hi!"
