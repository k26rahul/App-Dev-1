from models import db, Course, Student, Enroll


def populate():
  db.session.add(Course(course_code='CSE01', course_name='MAD 1', course_description='...'))
  db.session.add(Course(course_code='CSE02', course_name='DBMS', course_description='...'))
  db.session.add(Course(course_code='CSE03', course_name='PDSA', course_description='...'))
  db.session.add(Course(course_code='BST13', course_name='BDM', course_description='...'))

  db.session.add(Student(roll_number='1', first_name='Harikesh', last_name='Shukla'))

  db.session.add(Enroll(estudent_id=1, ecourse_id=1))
  db.session.add(Enroll(estudent_id=1, ecourse_id=3))

  db.session.commit()
  print('populate db done ✅')
