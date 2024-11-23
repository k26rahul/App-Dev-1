from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
  __tablename__ = 'students'
  id = Column(Integer, primary_key=True, autoincrement=True)
  roll_number = Column(String, nullable=False, unique=True)
  first_name = Column(String, nullable=False)
  last_name = Column(String)
  enrollments = relationship('Enrollment', back_populates='student', cascade='all, delete')


class Course(db.Model):
  __tablename__ = 'courses'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  code = Column(String, nullable=False, unique=True)
  description = Column(String)
  enrollments = relationship('Enrollment', back_populates='course', cascade='all, delete')


class Enrollment(db.Model):
  __tablename__ = 'enrollments'
  id = Column(Integer, primary_key=True, autoincrement=True)
  student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
  course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
  student = relationship('Student', back_populates='enrollments')
  course = relationship('Course', back_populates='enrollments')
