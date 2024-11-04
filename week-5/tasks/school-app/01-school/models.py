class Student:
  _idx = 1

  def __init__(self, name, place, age):
    self.id = Student._idx
    Student._idx += 1

    self.name = name
    self.place = place
    self.age = age

  def __repr__(self):
    return f'<Student {self.name}>'


class Course:
  _idx = 1

  def __init__(self, name, credits):
    self.id = Course._idx
    Course._idx += 1

    self.name = name
    self.credits = credits

  def __repr__(self):
    return f'<Course {self.name}>'


class Enroll:
  _idx = 1

  def __init__(self, student_id, course_id, term, year):
    self.id = Enroll._idx
    Enroll._idx += 1

    self.student_id = student_id
    self.course_id = course_id
    self.term = term
    self.year = year

  def __repr__(self):
    return f'<Enroll {self.student_id} {self.course_id}>'


""" tables as dicts """
students = {}
courses = {}
enrolls = {}


def add_student(student):
  students[student.id] = student


def add_course(course):
  courses[course.id] = course


def add_enroll(enroll):
  enrolls[enroll.id] = enroll


# demo data
add_student(Student('vidu', 'hbh', 22))
add_course(Course('maths1', 4))
add_course(Course('maths2', 4))
add_enroll(Enroll(1, 1, 't3', 2024))
