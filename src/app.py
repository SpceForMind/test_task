
from flask import Flask, jsonify
import models

app = Flask(__name__)


@app.route("/api/v1.0/fib/<int:num>/", methods = ["GET"])
def fib(num):
    return jsonify({"result" : models.Fib(num).calculate()})


@app.route("/api/v1.0/fact/<int:num>/", methods = ["GET"])
def fact(num):
    return jsonify({"result" : models.Fact(num).calculate()})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)