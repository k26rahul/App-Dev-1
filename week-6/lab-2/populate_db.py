from models import *


def populate():
  if Course.query.count() == 0:
    db.session.add(Course(course_name='Maths', course_code='MA001'))
    db.session.add(Course(course_name='Stats', course_code='ST001'))
    db.session.add(Student(roll_number='S001', first_name='Vidu'))
    db.session.add(Student(roll_number='S002', first_name='Rahul'))
    db.session.add(Student(roll_number='S003', first_name='Muskan'))
    db.session.add(Enrollment(student_id=1, course_id=1))
    db.session.add(Enrollment(student_id=1, course_id=2))
    db.session.add(Enrollment(student_id=2, course_id=2))
    db.session.commit()
