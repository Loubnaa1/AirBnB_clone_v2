#!/usr/bin/python3
"""script that starts a Flask web application:
listening on 0.0.0.0, port 5000"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_app(exc):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """display a HTML page: (inside the tag BODY)"""
    states_list = storage.all(State)
    return render_template("9-states.html", states=states_list)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """display a HTML page: (inside the tag BODY)"""
    for states in storage.all(State).values():
        if states.id == id:
            return render_template("9-states.html", states=states)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
