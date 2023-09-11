"""
This file provides the API for this project. It's a simple API that
returns a HTTP 200 (OK) code when requested.

To execute this file, first start a pipenv by issuing `pipenv shell`,
and then download all dependencies with `pipenv sync`. After that you
can run it as usual: `python api.py`
"""

__author__ = "Lucas de Ataides"

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """ Return a simple message """
    return "The server is working!"

@app.route('/square-root')
def get_square_root():
    """ Return the cube root of numbers between 1, and 1000 """
    new_list = [x**2 for x in range(0, 1001)]
    return f'{new_list}'

@app.route('/cube-root')
def get_cube_root():
    """ Return the square root of numbers between 1, 1000 """
    new_list = [x**3 for x in range(0, 1001)]
    return f'{new_list}'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
