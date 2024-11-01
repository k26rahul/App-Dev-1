from models import conn, cur


def add_student(name, place, age):
  cur.execute("INSERT INTO students (name, place, age) VALUES (?, ?, ?)", (name, place, age))
  conn.commit()


def add_course(name, credits):
  cur.execute('INSERT INTO courses (name, credits) VALUES (?, ?)', (name, credits))
  conn.commit()


def add_enroll(student_id, course_id, term, year):
  cur.execute('INSERT INTO enrolls (student_id, course_id, term, year) VALUES (?, ?, ?, ?)',
              (student_id, course_id, term, year))
  conn.commit()


add_student('vidu', 'hbh', 22)
add_student('rahul', 'albd', 21)
add_student('harikesh', 'bhadohi', 26)
add_course('maths1', 4)
add_course('stats1', 8)
add_enroll(3, 1, 't1', 2024)
add_enroll(2, 2, 't2', 2024)
