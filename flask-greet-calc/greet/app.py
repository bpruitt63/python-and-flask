from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    html = """<h1>welcome</h1>"""
    return html

@app.route('/welcome/home')
def home():
    html = """<h1>welcome home</h1>"""
    return html

@app.route('/welcome/back')
def back():
    html = """<h1>welcome back</h1>"""
    return html