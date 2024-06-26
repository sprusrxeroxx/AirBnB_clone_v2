#!/usr/bin/python3
"""Start a Flask web application with a route that displays 'Hello HBNB!'"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'  # Return the desired string

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return 'HBNB'  # Return the desired string


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)