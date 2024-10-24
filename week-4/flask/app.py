from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def root():
  return f'hello from root, datetime is {datetime.now()}'


@app.route('/greet')
def greet():
  return 'good morning!'


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
