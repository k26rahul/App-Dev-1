from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
  __tablename__ = 'student'

  student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  roll_number = db.Column(db.String, unique=True, nullable=False)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String)

  def __repr__(self):
    return f'<Student {self.first_name}>'


class Course(db.Model):
  __tablename__ = 'course'

  course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  course_code = db.Column(db.String, unique=True, nullable=False)
  course_name = db.Column(db.String, nullable=False)
  course_description = db.Column(db.String)

  def __repr__(self):
    return f'<Course {self.course_code}>'


class Enroll(db.Model):
  __tablename__ = 'enrollments'

  enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  estudent_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
  ecourse_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

  def __repr__(self):
    return f'<Enroll {self.estudent_id} {self.ecourse_id}>'
