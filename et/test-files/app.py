from flask import Flask, request

app = Flask(__name__)


@app.route('/calculate')
def calc():
  a = request.args.get('a')
  b = request.args.get('b')
  operator = request.args.get('operator')

  if a and b and operator:
    if operator == 'one':
      return f'{a} + {b} = {a+b}'
    elif operator == 'two':
      ...
  else:
    return 'not ok'


app.run(debug=True)
