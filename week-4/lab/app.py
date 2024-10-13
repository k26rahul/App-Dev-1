from flask import Flask, request, render_template
from jinja2 import Template
import csv

app = Flask(__name__)


def get_data():
  col_names = ['student_id', 'course_id', 'marks']
  data = list(csv.DictReader(open('data.csv'), fieldnames=col_names))
  data = data[1:]
  return data


def get_student_data(student_id):
  data = get_data()
  student_data = [row for row in data if row['student_id'] == student_id]
  if len(student_data) == 0:
    raise Exception('invalid student_id')
  marks = [int(row['marks']) for row in student_data]
  total_marks = sum(marks)
  return student_data, total_marks


def get_course_data(course_id):
  data = get_data()
  course_data = [row for row in data if row['course_id'] == course_id]
  if len(course_data) == 0:
    raise Exception('invalid course_id')
  marks = [int(row['marks']) for row in course_data]
  avg_marks = sum(marks)/len(marks)
  max_marks = max(marks)
  return course_data, marks, avg_marks, max_marks


def generate_error_output():
  return render_template('error_output.j2')


def generate_student_output(student_id):
  try:
    student_data, total_marks = get_student_data(student_id)
  except:
    return generate_error_output()

  # https://stackoverflow.com/a/55176881
  return render_template('student_output.j2', student_data=student_data, total_marks=total_marks)


def generate_histogram(marks, course_id):
  import matplotlib
  # https://stackoverflow.com/questions/49921721/runtimeerror-main-thread-is-not-in-main-loop-with-matplotlib-and-flask
  matplotlib.use('Agg')
  import matplotlib.pyplot as plt
  plt.hist(marks)
  plt.title(f'Marks vs Frequency for Course ID: {course_id}')
  plt.xlabel('Marks')
  plt.ylabel('Frequency')
  plt.savefig('./static/histogram.png')


def generate_course_output(course_id):
  try:
    course_data, marks, avg_marks, max_marks = get_course_data(course_id)
  except:
    return generate_error_output()

  return render_template('course_output.j2', avg_marks=avg_marks, max_marks=max_marks)


@app.route('/', methods=['GET', 'POST'])
def root():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    student_or_course = request.form.get('student_or_course')
    id = request.form.get('id')
    if student_or_course == 'student':
      return generate_student_output(id)
    elif student_or_course == 'course':
      return generate_course_output(f' {id}')
    else:
      return generate_error_output()


if __name__ == '__main__':
  app.run(debug=True)
