from flask import render_template, request
from application import app

@app.route('/hello', methods=['GET'])
def hello():
    return render_template('home.html', title="Hello", message="Hello from Flask")


@app.route('/bye', methods=['GET'])
def bye():
    return render_template('home.html', title="Goodbye", message="Bye from Flask")


@app.route('/', methods=['GET'])
def home():
    return "Home page text"

