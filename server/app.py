#!/usr/bin/env python3

from flask import Flask
from flatburger.html import flatburger_html_code
from flatburger.data import burgers
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Deliverable # 1 solution code
@app.route('/greeting/<first_name>/<last_name>')
def greeting(first_name, last_name):
    return f"<h1>Greetings, {first_name} {last_name}!</h1>"

# Deliverable # 2 solution code
@app.route('/count_and_square/<int:number>')
def count_and_square(number):
    squared_numbers_string = ""
    for i in range(1, number + 1):
        squared_numbers_string += f"{i ** 2}\n"
    return squared_numbers_string

# Deliverable # 3 solution code
@app.route('/flatburger_page')
def flatburger():
    return flatburger_html_code

# Deliverable # 4 solution code
@app.route('/burgers')
def get_burgers():
    return burgers

if __name__ == "__main__":
    app.run(port=7777, debug=True)