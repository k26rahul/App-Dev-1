import sys
import csv
from jinja2 import Template


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
  markup = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Error</title>
</head>

<body>
  <h1>Error</h1>
  <p>Invalid inputs</p>
</body>

</html>
"""
  open('output.html', 'w+').write(markup)


def generate_student_output(student_id):
  try:
    student_data, total_marks = get_student_data(student_id)
  except:
    return generate_error_output()
  template_string = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Student Details</title>
  <style>
    table,
    th,
    td {
      border: 1px solid black;
    }
  </style>
</head>

<body>
  <h1>Student Details</h1>
  <table>
    <tr>
      <th>Student ID</th>
      <th>Course ID</th>
      <th>Marks</th>
    </tr>
    {% for row in student_data %}
    <tr>
      <td>{{row.student_id}}</td>
      <td>{{row.course_id}}</td>
      <td>{{row.marks}}</td>
    </tr>
    {% endfor %}
    <tr>
      <td>Total Marks</td>
      <td>{{total_marks}}</td>
    </tr>
  </table>
</body>

</html>
"""
  template = Template(template_string)
  markup = template.render(student_data=student_data, total_marks=total_marks)
  open('output.html', 'w+').write(markup)


def generate_histogram(marks, course_id):
  import matplotlib.pyplot as plt
  plt.hist(marks)
  plt.title(f'Marks vs Frequency for Course ID: {course_id}')
  plt.xlabel('Marks')
  plt.ylabel('Frequency')
  plt.savefig('histogram.png')


def generate_course_output(course_id):
  try:
    course_data, marks, avg_marks, max_marks = get_course_data(course_id)
  except:
    return generate_error_output()
  template_string = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Student Details</title>
  <style>
    table,
    th,
    td {
      border: 1px solid black;
    }
  </style>
</head>

<body>
  <h1>Course Details</h1>
  <table>
    <tr>
      <th>Average Marks</th>
      <th>Maximum Marks</th>
    </tr>
    <tr>
      <td>{{avg_marks}}</td>
      <td>{{max_marks}}</td>
    </tr>
  </table>
  <img src="histogram.png" alt="Marks vs Frequency">
</body>

</html>
"""
  template = Template(template_string)
  markup = template.render(avg_marks=avg_marks, max_marks=max_marks)
  open('output.html', 'w+').write(markup)
  generate_histogram(marks, course_id)


# here it begins 👇
if sys.argv[1] == '-s':
  student_id = sys.argv[2]
  generate_student_output(student_id)
elif sys.argv[1] == '-c':
  course_id = sys.argv[2]
  generate_course_output(f' {course_id}')
else:
  generate_error_output()
