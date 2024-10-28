from flask import Flask, request, render_template, url_for, redirect
from datetime import datetime

app = Flask(__name__)


@app.route('/if_hello')
def this_if_big_if():
  return render_template('if_wala.html')


@app.route('/for_hello')
def this_is_big_for():
  return render_template('for_wala.html')


@app.route('/choice/<pick>')
def choice_page(pick):
  if pick == 'if':
    print('😱', url_for('this_if_big_if') == '/if')
    return url_for('this_if_big_if')
  elif pick == 'for':
    print('😱', url_for('this_is_big_for') == '/for')
    return url_for('this_is_big_for')


if __name__ == '__main__':
  app.run(debug=True)

# @app.route('/')
# def root():
#   return f'hello from root, datetime is {datetime.now()}'


# @app.route('/home/<string:student_id>/<int:course_id>')
# def get_info(student_id, course_id):
#   print(type(student_id))
#   print(type(course_id))
#   return f'u want info: {student_id}, {course_id}'


# from flask import Flask, request, render_template

# app = Flask(__name__)


# # @app.route('/')
# # def root():
# #   return 'hello from root'


# # @app.route('/song')
# # def song():
# #   name = request.args.get('name')
# #   type = request.args.get('type')
# #   year = request.args.get('year')
# #   return f'i need to give u {name} song of {type} type of year {year}'

# @app.route('/home/<student_id>/<course_id>')
# def info(student_id, course_id):
#   return 'some info about this student-course'


# app.run(debug=True)
