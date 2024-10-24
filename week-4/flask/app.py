from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def root():
  return f'hello from root, datetime is {datetime.now()}'


@app.route('/greet/<name>')
def greet(name):
  return f'good morning {name}!'


# @app.route('/greet/divya')
# def greet_divya():
#   return 'good morning divya!'


# @app.route('/greet/vidu')
# def greet_vidu():
#   return 'good morning vidu! this route is especially for u'


# @app.route('/greet/harikesh')
# def greet_harikesh():
#   return 'good morning harikesh! enjoy your route!!'

@app.route('/add/<a>/<b>')
def add(a, b):
  return str(int(a) + int(b))


@app.route('/calc/<op>/<a>/<b>')
def calc(op, a, b):
  if op == 'add':
    return str(int(a) + int(b))
  elif op == 'minus':
    return str(int(a) - int(b))
  elif op == 'mult':
    return str(int(a) * int(b))
  elif op == 'div':
    return str(int(a) / int(b))


@app.route('/quiz/1')
def quiz1():
  return '<h1>quiz 1 is on <span style="color: red">27th oct</span></h1>'


@app.route('/quiz/2')
def quiz2():
  return render_template('quiz2.html')


@app.route('/html-test')
def html():
  return render_template('html-test.html')


if __name__ == '__main__':
  app.run(debug=True)
