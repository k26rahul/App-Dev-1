from flask import Flask, request, render_template, redirect

app = Flask(__name__)
todos = {
    1: 'drink water',
    2: 'eat coconut'
}
last_id = 3


@app.route('/add', methods=['POST'])
def add_todo():
  global last_id
  text = request.form['todo_text']
  todos[last_id] = text
  last_id += 1
  return redirect('/')


@app.route('/remove', methods=['GET'])
def remove_todo():
  id = int(request.args['todo_id'])
  if id in todos:
    del todos[id]
  return redirect('/')


@app.route('/')
def index():
  return render_template('index.html', todos=reversed(todos.items()))


if __name__ == "__main__":
  app.run(debug=True)