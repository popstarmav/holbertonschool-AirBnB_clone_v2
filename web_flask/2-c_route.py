#!/usr/bin/python3
"""Import flask module"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_variable(text):
    """ Replace underscores with space with urllib.parse.unquote """
    text = unquote(text.replace('_', ' '))
    return f"C {text}"


""" sever only starts script if direclty activted """
if __name__ == "__main__":
    # Network interface
    app.run(host="0.0.0.0", port=5000)
