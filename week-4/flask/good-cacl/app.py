from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


# @app.route('/alien')
# def alien():
#   name = request.args['name']
#   place = request.args['place']
#   age = request.args['age']
#   return f'i think u are {name}, and u live in {place}, ur age is {age}'
  # what_to_do = request.args['what_to_do']
  # a = int(request.args['first_num'])
  # b = int(request.args['second_num'])
  # return f'ok, so, i think you want to do: {what_to_do} for {a} and {b}; do u think i am smart enough to do this??????????'


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
