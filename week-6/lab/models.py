from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Course(db.Model):
  __tablename__ = 'course'
  course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  course_name = db.Column(db.String, nullable=False)
  course_code = db.Column(db.String, unique=True, nullable=False)
  course_description = db.Column(db.String)

  def serialize(self):
    return {
        'course_id': self.course_id,
        'course_name': self.course_name,
        'course_code': self.course_code,
        'course_description': self.course_description
    }


class Student(db.Model):
  __tablename__ = 'student'
  student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  roll_number = db.Column(db.String, unique=True, nullable=False)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String)

  def serialize(self):
    return {
        'student_id': self.student_id,
        'roll_number': self.roll_number,
        'first_name': self.first_name,
        'last_name': self.last_name
    }


class Enrollment(db.Model):
  __tablename__ = 'enrollment'
  enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
  course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

  def serialize(self):
    return {
        'enrollment_id': self.enrollment_id,
        'student_id': self.student_id,
        'course_id': self.course_id
    }
