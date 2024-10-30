from flask import Flask, request, render_template, redirect
from models import *

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html', students=students, courses=courses, enrolls=enrolls)


@app.route('/add/student', methods=['GET', 'POST'])
def add_student_route():
  if request.method == 'POST':
    name = request.form['name']
    place = request.form['place']
    age = int(request.form['age'])
    student = Student(name, place, age)
    add_student(student)
    return redirect('/')
  elif request.method == 'GET':
    return render_template('add-student.html')


if __name__ == '__main__':
  app.run(debug=True)
