from flask import Flask, request, render_template, redirect
from models import db, Student, Enroll
import populate_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db.init_app(app)


@app.route('/')
def index():
  # students = session.query(Student).all()
  students = Student.query.all()
  return render_template('index.html', students=students)


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
