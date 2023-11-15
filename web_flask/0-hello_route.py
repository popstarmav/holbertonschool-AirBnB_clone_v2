#!/usr/bin/python3
"""Import flask module"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB """
    return "Hello HBNB!"


""" sever only starts script if direclty activted """
if __name__ == "__main__":
    # Network interface
    app.run(host="0.0.0.0", port=5000)
