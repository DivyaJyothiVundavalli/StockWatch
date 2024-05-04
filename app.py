from flask import Flask, render_template, request
from polygon_api import get_stock_prices

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symbol = request.form['symbol']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        api_key = 'C62gpgTWczK4f2Y5iD0AqlfxtYuTZobV'
        stock_prices = get_stock_prices(symbol, start_date, end_date, api_key)
        return render_template('index.html', stock_prices=stock_prices)
    else:
        return render_template('index.html', stock_prices=None)

if __name__ == '__main__':
    app.run(debug=True)
