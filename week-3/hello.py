import sys
print(sys.argv)

if sys.argv[1] == '-s':
  student_id = sys.argv[2]
  print(student_id)
elif sys.argv[1] == '-c':
  course_id = sys.argv[2]
  print(course_id)
