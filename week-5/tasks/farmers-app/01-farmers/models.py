""" bases on test2 """


class Product:
  _idx = 1

  def __init__(self, name, type):
    self.id = Product._idx
    Product._idx += 1

    self.name = name
    self.type = type

  def __repr__(self):
    return f'<Product {self.name}>'


class Stock:
  _idx = 1

  def __init__(self, product_id, qty, price, expiry):
    self.id = Stock._idx
    Stock._idx += 1

    self.product_id = product_id
    self.qty = qty
    self.price = price
    self.expiry = expiry

  def __repr__(self):
    return f'<Stock {self.product_id}>'


products = {
    #: Product (as rows)
    1: Product('potato', 'veg'),
    2: Product('tomato', 'veg'),
    3: Product('milk', 'diary'),
    4: Product('honey', 'others'),
}

stocks = {
    #: Stock (as rows)
    1: Stock(product_id=1, qty=50, price=40, expiry=20),
    2: Stock(product_id=1, qty=150, price=20, expiry=5),
    3: Stock(product_id=3, qty=10, price=50, expiry=2),
    4: Stock(product_id=4, qty=100, price=500, expiry=500),
}


def add_product(product):
  products[product.id] = product


def add_stock(stock):
  stocks[stock.id] = stock
