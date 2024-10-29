from flask import Flask, request, render_template, redirect
from models import TodoItem


app = Flask(__name__)
todos = {
    1: TodoItem('drink water'),
    2: TodoItem('eat cake')
}


@app.route('/add', methods=['POST'])
def add_todo():
  text = request.form['todo_text']
  todo_item = TodoItem(text)
  todos[todo_item.id] = todo_item
  return redirect('/')


@app.route('/remove', methods=['GET'])
def remove_todo():
  id = int(request.args['todo_id'])
  if id in todos:
    del todos[id]
  return redirect('/')


@app.route('/done', methods=['GET'])
def mark_done():
  id = int(request.args['todo_id'])
  if id in todos:
    todos[id].status = 'done'
  return redirect('/')


@app.route('/')
def index():
  return render_template('index.html', todos=reversed(todos.items()))


if __name__ == "__main__":
  app.run(debug=True)
