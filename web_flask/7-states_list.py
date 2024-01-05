#!/usr/bin/python3
"""starts a Flask web application:
listens on 0.0.0.0, port 5000"""
from flask import Flask
from models import storage
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_app(exc):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
