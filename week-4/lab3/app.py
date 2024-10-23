import sys

if sys.argv[1] == '-s':
  student_id = sys.argv[2]
  print('we generate student data for:', student_id)
elif sys.argv[1] == '-c':
  course_id = sys.argv[2]
  print('we generate course data for:', course_id)
else:
  print('error')
