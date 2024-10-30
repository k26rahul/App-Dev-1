from flask import Flask, request, render_template, redirect
from models import *

app = Flask(__name__)


@app.route('/add-product', methods=['POST'])
def add_product_route():
  name = request.form['name']
  type = request.form['type']
  product = Product(name, type)
  add_product(product)
  return redirect('/')


@app.route('/add-stock', methods=['POST'])
def add_stock_route():
  product_id = int(request.form['product_id'])
  qty = int(request.form['qty'])
  price = int(request.form['price'])
  expiry = int(request.form['expiry'])
  stock = Stock(product_id, qty, price, expiry)
  add_stock(stock)
  return redirect('/')


@app.route('/')
def index():
  return render_template('index.html', products=products, stocks=stocks)


if __name__ == '__main__':
  app.run(debug=True)
