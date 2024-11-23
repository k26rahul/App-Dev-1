from flask import Blueprint, render_template, request, redirect
from models import *

bp = Blueprint('default', __name__)


@bp.route('/')
def index():
  students = Student.query.all()
  return render_template('index.html', students=students)


@bp.route('/student/create', methods=['GET', 'POST'])
def student_create():
  if request.method == 'GET':
    courses = Course.query.all()
    return render_template('student_create.html', courses=courses)
  elif request.method == 'POST':
    new_student = Student(
        roll_number=request.form.get('roll_number'),
        first_name=request.form.get('first_name'),
        last_name=request.form.get('last_name')
    )
    db.session.add(new_student)
    db.session.commit()

    courses = request.form.getlist('courses')
    for course_id in courses:
      db.session.add(Enrollment(
          student_id=new_student.id,
          course_id=course_id
      ))
    db.session.commit()
    return redirect('/')


@bp.route('/student/<int:student_id>/update', methods=['GET', 'POST'])
def student_update(student_id):
  student = Student.query.filter_by(id=student_id).first()
  if request.method == 'GET':
    courses = Course.query.all()
    taken_courses = [enroll.course for enroll in student.enrollments]
    return render_template('student_update.html', student=student, courses=courses,
                           taken_courses=taken_courses)
  elif request.method == 'POST':
    student.roll_number = request.form.get('roll_number')
    student.first_name = request.form.get('first_name')
    student.last_name = request.form.get('last_name')
    for enroll in student.enrollments:
      db.session.delete(enroll)
    courses = request.form.getlist('courses')
    for course_id in courses:
      db.session.add(Enrollment(
          student_id=student_id,
          course_id=course_id
      ))
    db.session.commit()
    return redirect('/')


@bp.route('/student/<int:student_id>/delete')
def student_delete(student_id):
  student = Student.query.filter_by(id=student_id).first()
  db.session.delete(student)
  db.session.commit()
  return redirect('/')


@bp.route('/student/<int:student_id>')
def student_details(student_id):
  student = Student.query.filter_by(id=student_id).first()
  return render_template('student_details.html', student=student)


# ====== courses ======


@bp.route('/courses')
def courses_index():
  courses = Course.query.all()
  return render_template('courses_index.html', courses=courses)


@bp.route('/course/create', methods=['GET', 'POST'])
def courses_create():
  if request.method == 'GET':
    return render_template('courses_create.html')
  elif request.method == 'POST':
    db.session.add(Course(
        name=request.form.get('name'),
        code=request.form.get('code'),
        description=request.form.get('description'),
    ))
    db.session.commit()
    return redirect('/courses')


@bp.route('/course/<int:course_id>/update', methods=['GET', 'POST'])
def course_update(course_id):
  course = Course.query.filter_by(id=course_id).first()
  if request.method == 'GET':
    return render_template('course_update.html', course=course)
  elif request.method == 'POST':
    course.name = request.form.get('name')
    course.code = request.form.get('code')
    course.description = request.form.get('description')
    db.session.commit()
    return redirect('/courses')


@bp.route('/course/<int:course_id>/delete')
def course_delete(course_id):
  course = Course.query.filter_by(id=course_id).first()
  db.session.delete(course)
  db.session.commit()
  return redirect('/courses')


@bp.route('/course/<int:course_id>')
def course_details(course_id):
  course = Course.query.filter_by(id=course_id).first()
  return render_template('course_details.html', course=course)
