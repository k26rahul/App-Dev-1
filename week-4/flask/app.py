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
  return """<h1>quiz 2 is on <span style="color: green">3rd nov</span></h1>"""


@app.route('/html-test')
def html():
  return """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello Vidu</title>
</head>

<body>
  <h1 style="text-align: center; color: cyan">This is some big html doc</h1>

  <table border='1'>
    <tr>
      <th>Day</th>
    </tr>
    <tr>
      <td style="color: green">Thursday</td>
    </tr>
  </table>
</body>

</html>"""


if __name__ == '__main__':
  app.run(debug=True)
