from flask import Blueprint, request, render_template, redirect
from models import *

student_bp = Blueprint('student', __name__)


@student_bp.route('/student/<int:student_id>')
def student_profile(student_id):
  student = Student.query.filter_by(student_id=student_id).first()
  return render_template('student_profile.html', student=student)


@student_bp.route('/student/create', methods=['GET', 'POST'])
def add_student():
  if request.method == 'GET':
    return render_template('add_student.html', error=False)

  elif request.method == 'POST':
    # check if a student with this roll no. exists
    student = Student.query.filter_by(roll_number=request.form.get('roll')).first()
    if student:
      return render_template('add_student.html', error=True)

    enrolls = []
    courses = request.form.getlist('courses')
    for course in courses:
      course_id = int(course[-1])
      enrolls.append(Enroll(
          ecourse_id=course_id
      ))

    new_student = Student(
        roll_number=request.form.get('roll'),
        first_name=request.form.get('f_name'),
        last_name=request.form.get('l_name'),
        enrolls=enrolls
    )
    db.session.add(new_student)
    db.session.commit()
    return redirect('/')


@student_bp.route('/student/<int:student_id>/update', methods=['GET', 'POST'])
def update_student(student_id):
  student = Student.query.filter_by(student_id=student_id).first()
  if request.method == 'GET':
    taken = {
        1: False,
        2: False,
        3: False,
        4: False
    }
    for enroll in student.enrolls:
      taken[enroll.course.course_id] = True
    return render_template('update_student.html', student=student, taken=taken)

  elif request.method == 'POST':
    # clear current enrolls
    for enroll in student.enrolls:
      db.session.delete(enroll)

    # add new enrolls
    courses = request.form.getlist('courses')
    for course in courses:
      course_id = int(course[-1])
      db.session.add(Enroll(
          estudent_id=student_id,
          ecourse_id=course_id
      ))

    student.roll_number = request.form.get('roll')
    student.first_name = request.form.get('f_name')
    student.last_name = request.form.get('l_name')
    db.session.commit()
    return redirect('/')


@student_bp.route('/student/<int:student_id>/delete')
def delete_student(student_id):
  student = Student.query.filter_by(student_id=student_id).first()
  db.session.delete(student)
  db.session.commit()
  return redirect('/')
