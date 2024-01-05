#!/usr/bin/python3
"""script that starts a Flask web application:
listens on 0.0.0.0, port 5000"""
from flask import Flask
from models import storage
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_app(exc):

    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities():
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
