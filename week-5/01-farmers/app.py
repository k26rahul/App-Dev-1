from flask import Flask, request, render_template, redirect
from models import *

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html', products=products, stocks=stocks)


if __name__ == '__main__':
  app.run(debug=True)
