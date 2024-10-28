#!/usr/bin/env python3

from flask import Flask
from flatburger.html import flatburger_html_code
from flatburger.data import burgers
from flask_cors import CORS

app = Flask(__name__)

# This should allow us to enable CORS
CORS(app)

@app.route('/')
def index():
    return """
        <div>
            <h1>Welcome to Flatiron School!</h1>
            <h2>It's time to learn Flask!</h2>
        </div>
    """

@app.route('/hello')
def greeting_view():
    return "<h1>Hello World!</h1>"

# @app.route('/greetings/<first_name>/<last_name>')
# def name_view(first_name, last_name):
#     return f"<h1>Hello {first_name} {last_name}!</h1>"

@app.route('/sum/<int:num1>/<int:num2>')
def sum_view(num1, num2):
    # print(num1)
    # print(type(num1))
    # print(num2)
    # print(type(num2))
    # return f"<h1>{num1} + {num2} = {int(num1) + int(num2)}</h1>"
    return f"<h1>{num1} + {num2} = {num1 + num2}</h1>"

@app.route('/<float:number>')
def float_example(number):
    return f"<h1>The number is {number}</h1>"

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