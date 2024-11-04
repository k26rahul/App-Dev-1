from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

Base = declarative_base()


class Student(Base):
  __tablename__ = 'student'

  student_id = Column(Integer, primary_key=True, autoincrement=True)
  roll_number = Column(String, unique=True, nullable=False)
  first_name = Column(String, nullable=False)
  last_name = Column(String)

  def __repr__(self):
    return f'<Student {self.first_name}>'


class Course(Base):
  __tablename__ = 'course'

  course_id = Column(Integer, primary_key=True, autoincrement=True)
  course_code = Column(String, unique=True, nullable=False)
  course_name = Column(String, nullable=False)
  course_description = Column(String)

  def __repr__(self):
    return f'<Course {self.course_code}>'


class Enroll(Base):
  __tablename__ = 'enrollments'

  enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
  estudent_id = Column(Integer, ForeignKey('student.student_id'), nullable=False)
  ecourse_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)

  def __repr__(self):
    return f'<Enroll {self.estudent_id} {self.ecourse_id}>'


# https://stackoverflow.com/questions/21766960/operationalerror-no-such-table-in-flask-with-sqlalchemy
engine = create_engine('sqlite:///:memory:', connect_args={'check_same_thread': False},
                       poolclass=StaticPool)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()
