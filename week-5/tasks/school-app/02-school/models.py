import sqlite3

conn = sqlite3.connect('database.sqlite3', check_same_thread=False)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                place TEXT,
                age INTEGER
            )""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY,
                name TEXT,
                credits INTEGER
            )""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS enrolls (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                course_id INTEGER,
                term TEXT,
                year INTEGER,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id)
            )""")
conn.commit()
