# https://betterprogramming.pub/create-a-running-docker-container-with-gunicorn-and-flask-dcd98fddb8e0

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"