#!/usr/bin/python3
from flask import flask

app = flask(__name__)

@app.route('/')
def hello_hbnb():
    """
    A simple Flask route.

    Returns:
    str: A string contains a greeting message
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
