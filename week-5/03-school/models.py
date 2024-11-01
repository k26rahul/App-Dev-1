from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()


class Student(Base):
  __tablename__ = 'students'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  place = Column(String)
  age = Column(Integer)

  courses = relationship('Course', secondary='enrolls', back_populates='students')

  def __repr__(self):
    return f'<Student {self.name}>'


class Course(Base):
  __tablename__ = 'courses'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  credits = Column(Integer)

  students = relationship('Student', secondary='enrolls', back_populates='courses')

  def __repr__(self):
    return f'<Course {self.name}>'


class Enroll(Base):
  __tablename__ = 'enrolls'

  id = Column(Integer, primary_key=True)

  student_id = Column(Integer, ForeignKey('students.id'))
  course_id = Column(Integer, ForeignKey('courses.id'))
  term = Column(String)
  year = Column(Integer)

  def __repr__(self):
    return f'<Enroll {self.student_id} {self.course_id}>'


engine = create_engine('sqlite:///database.sqlite3', connect_args={
    'check_same_thread': False
})
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
