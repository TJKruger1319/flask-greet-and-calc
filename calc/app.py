from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def send_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a,b))

@app.route("/sub")
def send_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a,b))

@app.route("/mult")
def send_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a,b))

@app.route("/div")
def send_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a,b))