from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'


@app.route('/')
def index():
  if 'name' in session:
    return f'Hello, {session['name']}'
  else:
    return 'Hello, guest!'


@app.route('/know-me/<my_name>')
def know_me(my_name):
  session['name'] = my_name
  return f'Hello, {my_name}! Now i know u 👍'


@app.route('/forget-me')
def forget_me():
  del session['name']
  return f'Hello, u! Now i forget u 👍'


app.run(debug=True)
