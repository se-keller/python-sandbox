# to run this > python3 -m flask run
from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello Web-World"
