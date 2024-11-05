from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
  __tablename__ = 'student'
  student_id = Column(Integer, primary_key=True, autoincrement=True)
  roll_number = Column(String, unique=True, nullable=False)
  first_name = Column(String, nullable=False)
  last_name = Column(String)

  enrolls = relationship('Enroll', back_populates='student', cascade='all, delete')


class Course(db.Model):
  __tablename__ = 'course'
  course_id = Column(Integer, primary_key=True, autoincrement=True)
  course_code = Column(String, unique=True, nullable=False)
  course_name = Column(String, nullable=False)
  course_description = Column(String)

  enrolls = relationship('Enroll', back_populates='course', cascade='all, delete')


class Enroll(db.Model):
  __tablename__ = 'enrollments'
  enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
  estudent_id = Column(Integer, ForeignKey('student.student_id'), nullable=False)
  ecourse_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)

  student = relationship('Student', back_populates='enrolls')
  course = relationship('Course', back_populates='enrolls')
