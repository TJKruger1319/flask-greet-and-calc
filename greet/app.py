from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def send_welcome():
    return "welcome"

@app.route("/welcome/home")
def send_welcome_home():
    return "welcome home"

@app.route("/welcome/back")
def send_welcome_back():
    return "welcome back"
