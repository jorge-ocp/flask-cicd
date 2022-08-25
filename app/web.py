from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/aboutus")
def aboutus():
    return "About Us"