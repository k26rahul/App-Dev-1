from flask import Blueprint, request, render_template, redirect
from models import *

student_bp = Blueprint('student', __name__)


@student_bp.route('/student/<int:student_id>')
def student_profile(student_id):
  student = Student.query.filter_by(student_id=student_id).first()
  # enrolls = Enroll.query.filter_by(estudent_id=student_id).all()
  # courses = []
  # for enroll in enrolls:
  #   course = Course.query.filter_by(course_id=enroll.ecourse_id).first()
  #   courses.append(course)
  courses = (
      Course.query
      .join(Enroll, Enroll.ecourse_id == Course.course_id)
      .filter(Enroll.estudent_id == student_id)
      .all()
  )

  return render_template('student_profile.html', student=student, courses=courses)


@student_bp.route('/student/create', methods=['GET', 'POST'])
def add_student():
  if request.method == 'GET':
    return render_template('add_student.html', error=False)
  else:
    student = Student.query.filter_by(roll_number=request.form.get('roll')).first()
    if student is not None:
      return render_template('add_student.html', error=True)

    new_student = Student(
        roll_number=request.form.get('roll'),
        first_name=request.form.get('f_name'),
        last_name=request.form.get('l_name')
    )
    db.session.add(new_student)
    db.session.commit()

    courses = request.form.getlist('courses')
    for course in courses:
      course_id = int(course[-1])
      db.session.add(Enroll(
          estudent_id=new_student.student_id,
          ecourse_id=course_id
      ))
    db.session.commit()
    return redirect('/')


@student_bp.route('/student/<int:student_id>/update', methods=['GET', 'POST'])
def update_student(student_id):
  student = Student.query.filter_by(student_id=student_id).first()
  if request.method == 'GET':
    courses = (
        Course.query
        .join(Enroll, Enroll.ecourse_id == Course.course_id)
        .filter(Enroll.estudent_id == student_id)
        .all()
    )
    taken = {
        1: False,
        2: False,
        3: False,
        4: False
    }
    for course in courses:
      taken[course.course_id] = True
    return render_template('update_student.html', student=student, taken=taken)
  else:
    student.roll_number = request.form.get('roll')
    student.first_name = request.form.get('f_name')
    student.last_name = request.form.get('l_name')

    # Remove all current enrolls for the student
    Enroll.query.filter_by(estudent_id=student_id).delete()

    # Add new enrolls based on selected courses
    courses = request.form.getlist('courses')
    for course in courses:
      course_id = int(course[-1])
      db.session.add(Enroll(
          estudent_id=student_id,
          ecourse_id=course_id
      ))
    db.session.commit()
    return redirect('/')


@student_bp.route('/student/<int:student_id>/delete')
def delete_student(student_id):
  # db.session.query(Student).filter_by(student_id=student_id).delete()
  Student.query.filter_by(student_id=student_id).delete()
  Enroll.query.filter_by(estudent_id=student_id).delete()
  db.session.commit()
  return redirect('/')
