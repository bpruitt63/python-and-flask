from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)



@app.route('/math/<operation>')
def math(operation):
    a = request.args['a']
    b = request.args['b']
    a = int(a)
    b = int(b)
    ops = {'add': add(a, b), 'sub': sub(a, b), 'mult': mult(a, b), 'div': div(a, b)}
    result = ops[operation]
    html = f"<h1>{result}</h1>"
    return html