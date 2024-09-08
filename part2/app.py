from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index page"

@app.route("/about")
def about():
    return "about page"

@app.route("/account/<int:id>")
def account(id):
    return f"account id {id}"