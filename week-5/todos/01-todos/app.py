from flask import Flask, request, render_template, redirect

app = Flask(__name__)
todos = ['drink water', 'eat cake']


@app.route('/add', methods=['POST'])
def add_todo():
  text = request.form['todo_text']
  todos.append(text)
  return redirect('/')


@app.route('/remove', methods=['POST'])
def remove_todo():
  text = request.form['todo_text']
  todos.remove(text)
  return redirect('/')


@app.route('/')
def root():
  return render_template('index.html', todos=reversed(todos))


if __name__ == '__main__':
  app.run(debug=True)
