from flask import Flask, request, render_template, flash, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes
from currency import Currency
#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
#debug = DebugToolbarExtension(app)

c = Currency()
curr_codes = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/submit')
def handle_submit():
    frm = request.args['frm']
    frm = frm.upper()
    to = request.args['to']
    to = to.upper()
    amount = request.args['amount']   
    try:
        resp = c.check_valid_code(frm, to, amount)
        # conv = c.conversion(frm, to, amount)
        if resp != 'error':
            return render_template('result.html', conv=resp)
        else:
            return redirect('/')
    except:
        if frm not in curr_codes:
            flash(f'Not a valid code: {frm}')
        if to not in curr_codes:
            flash(f'Not a valid code: {to}')
        if amount == '':
            flash('Not a valid amount.')
        return redirect('/')
    

