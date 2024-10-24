from jinja2 import Template
import csv
import sys


def get_data():
  col_names = ['student_id', 'course_id', 'marks']
  data = list(csv.DictReader(open('data.csv'), fieldnames=col_names))
  return data[1:]


def get_student_data(student_id):
  data = get_data()
  student_data = [row for row in data if row['student_id'] == student_id]
  if len(student_data) == 0:
    raise Exception('invalid student_id')

  total_marks = sum([int(row['marks']) for row in student_data])
  return student_data, total_marks


def get_course_data(course_id):
  data = get_data()
  course_data = [row for row in data if row['course_id'] == course_id]
  marks = [int(row['marks']) for row in course_data]
  avg_marks = sum(marks)/len(marks)
  max_marks = max(marks)
  return marks, avg_marks, max_marks


def generate_error_html():
  html = open('./templates/error.html').read()
  open('output.html', 'w+').write(html)


def generate_student_html(student_id):
  try:
    student_data, total_marks = get_student_data(student_id)
  except:
    return generate_error_html()
  template_string = open('./templates/student.html').read()
  html = Template(template_string).render(student_data=student_data, total_marks=total_marks)
  open('output.html', 'w+').write(html)


def generate_histogram(course_id, marks):
  import matplotlib
  matplotlib.use('Agg')
  import matplotlib.pyplot as plt
  plt.hist(marks)
  plt.title(f'Marks vs Freq for Course ID: {course_id}')
  plt.xlabel('Marks')
  plt.ylabel('Freq')
  plt.savefig('histogram.png')


def generate_course_html(course_id):
  try:
    marks, avg_marks, max_marks = get_course_data(course_id)
  except:
    return generate_error_html()
  template_string = open('./templates/course.html').read()
  html = Template(template_string).render(avg_marks=avg_marks, max_marks=max_marks)
  open('output.html', 'w+').write(html)
  generate_histogram(course_id, marks)


if sys.argv[1] == '-s':
  student_id = sys.argv[2]
  generate_student_html(student_id)
elif sys.argv[1] == '-c':
  course_id = sys.argv[2]
  generate_course_html(f' {course_id}')
else:
  generate_error_html()
