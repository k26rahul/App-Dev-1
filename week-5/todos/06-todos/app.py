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
  if 'show' in request.args:
    show = request.args['show']
  else:
    show = 'all'

  if show == 'done':
    new_todos = [(id, todo_item) for id, todo_item in reversed(todos.items()) if todo_item.status == 'done']
  elif show == 'pending':
    new_todos = [(id, todo_item) for id, todo_item in reversed(todos.items()) if todo_item.status == 'pending']
  else:
    new_todos = reversed(todos.items())
  return render_template('index.html', todos=new_todos)


if __name__ == "__main__":
  app.run(debug=True)
