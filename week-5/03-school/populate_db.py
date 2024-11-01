from models import session, Student, Course, Enroll

session.add(Student(name='harikesh', place='albd', age=22))
session.add(Student(name='cmd', place='albd', age=19))

session.add(Course(name='maths1', credits=8))
session.add(Course(name='stats1', credits=4))

session.add(Enroll(student_id=2, course_id=2, term='t2', year=2024))
session.add(Enroll(student_id=2, course_id=1, term='t1', year=2022))
session.add(Enroll(student_id=1, course_id=1, term='t3', year=2024))

session.commit()
