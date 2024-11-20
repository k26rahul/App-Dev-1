from sqlalchemy import Column, String, Integer, ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Course(db.Model):
  __tablename__ = 'courses'
  course_id = Column(Integer, primary_key=True, autoincrement=True)
  course_name = Column(String, nullable=False)
  course_code = Column(String, nullable=False, unique=True)
  course_description = Column(String)

  def serialize(self):
    return {
        "course_id": self.course_id,
        'course_name': self.course_name,
        "course_code": self.course_code,
        "course_description": self.course_description
    }


class Student(db.Model):
  __tablename__ = 'students'
  student_id = Column(Integer, primary_key=True, autoincrement=True)
  roll_number = Column(String, nullable=False, unique=True)
  first_name = Column(String, nullable=False)
  last_name = Column(String)

  def serialize(self):
    return {
        "student_id": self.student_id,
        'roll_number': self.roll_number,
        "first_name": self.first_name,
        "last_name": self.last_name
    }


class Enrollment(db.Model):
  __tablename__ = 'enrollments'
  enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
  student_id = Column(Integer, ForeignKey('students.student_id'), nullable=False)
  course_id = Column(Integer, ForeignKey('courses.course_id'), nullable=False)

  def serialize(self):
    return {
        'enrollment_id': self.enrollment_id,
        'student_id': self.student_id,
        'course_id': self.course_id,
    }
