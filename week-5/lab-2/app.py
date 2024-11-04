from flask import Flask, request, render_template, redirect
from models import db, Student, Course, Enroll
import populate_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db.init_app(app)


@app.route('/')
def index():
  # students = session.query(Student).all()
  students = Student.query.all()
  return render_template('index.html', students=students)


@app.route('/student/<int:student_id>')
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
  print(courses)

  return render_template('student_profile.html', student=student, courses=courses)


@app.route('/student/create', methods=['GET', 'POST'])
def add_student():
  if request.method == 'GET':
    return render_template('add_student.html')
  else:
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


if __name__ == '__main__':
  with app.app_context():
    db.create_all()
    # populate_db.populate()
  app.run(debug=True)
