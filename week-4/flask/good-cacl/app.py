from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/calc', methods=['POST'])
def calc():
  what_to_do = request.form['what_to_do']
  a = int(request.form['first_num'])
  b = int(request.form['second_num'])
  if what_to_do == 'add':
    result = a + b
  elif what_to_do == 'minus':
    result = a - b
  elif what_to_do == 'mult':
    result = a * b
  elif what_to_do == 'div':
    result = a / b
  elif what_to_do == 'power':
    result = a ** b
  return render_template('result.html', what_to_do=what_to_do, first_num=a, second_num=b, result=result)


if __name__ == '__main__':
  app.run(debug=True)
