import sys

if sys.argv[1] == '-s':
  student_id = sys.argv[2]
  print(f'Showing data for student: {student_id}')
elif sys.argv[1] == '-c':
  course_id = sys.argv[2]
  print(f'Showing data for course: {course_id}')
