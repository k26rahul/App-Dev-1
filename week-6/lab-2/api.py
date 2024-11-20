from flask_restful import Resource, Api, request
from models import *

api = Api()

ERROR_CODES = {
    "COURSE001": 'Course Name is required',
    "COURSE002": 'Course Code is required',
    "STUDENT001": 'Roll Number required',
    "STUDENT002": 'First Name is required',
    "ENROLLMENT001": 'Course does not exist',
    "ENROLLMENT002": 'Student does not exist.',
    "RESOURCE_NOT_FOUND": 'Resource not found',
    "RESOURCE_ALREADY_EXISTS": 'Resource already exists',
    "BAD_REQUEST": 'Bad request',
}


def error(code):
  return {
      'error_code': code,
      'error_message': ERROR_CODES[code]
  }


class CourseAPI(Resource):
  def get(self, course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if not course:
      return error('RESOURCE_NOT_FOUND'), 404
    return course.serialize()

  def put(self, course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if not course:
      return error('RESOURCE_NOT_FOUND'), 404
    try:
      data = request.get_json()
    except:
      return error('BAD_REQUEST'), 400
    course.course_name = data.get('course_name', course.course_name)
    course.course_code = data.get('course_code', course.course_code)
    course.course_description = data.get('course_description', course.course_description)
    db.session.commit()
    return course.serialize()

  def delete(self, course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if not course:
      return error('RESOURCE_NOT_FOUND'), 404
    db.session.delete(course)
    db.session.commit()
    return 'Successfully deleted'

  def post(self):
    try:
      data = request.get_json()
    except:
      return error('BAD_REQUEST'), 400
    if not data.get('course_name'):
      return error('COURSE001'), 400
    if not data.get('course_code'):
      return error('COURSE002'), 400

    if Course.query.filter_by(course_code=data.get('course_code')).first():
      return error('RESOURCE_ALREADY_EXISTS'), 409
    new_course = Course(
        course_name=data.get('course_name'),
        course_code=data.get('course_code'),
        course_description=data.get('course_description'),
    )
    db.session.add(new_course)
    db.session.commit()
    return new_course.serialize(), 201


class StudentAPI(Resource):
  def get(self, student_id):
    student = Student.query.filter_by(student_id=student_id).first()
    if not student:
      return error('RESOURCE_NOT_FOUND'), 404
    return student.serialize()

  def put(self, student_id):
    student = Student.query.filter_by(student_id=student_id).first()
    if not student:
      return error('RESOURCE_NOT_FOUND'), 404
    try:
      data = request.get_json()
    except:
      return error('BAD_REQUEST'), 400
    student.roll_number = data.get('roll_number', student.roll_number)
    student.first_name = data.get('first_name', student.first_name)
    student.last_name = data.get('last_name', student.last_name)
    db.session.commit()
    return student.serialize()

  def delete(self, student_id):
    student = Student.query.filter_by(student_id=student_id).first()
    if not student:
      return error('RESOURCE_NOT_FOUND'), 404
    db.session.delete(student)
    db.session.commit()
    return 'Successfully deleted'

  def post(self):
    try:
      data = request.get_json()
    except:
      return error('BAD_REQUEST'), 400
    if not data.get('roll_number'):
      return error('STUDENT001'), 400
    if not data.get('first_name'):
      return error('STUDENT002'), 400

    if Student.query.filter_by(roll_number=data.get('roll_number')).first():
      return error('RESOURCE_ALREADY_EXISTS'), 409
    new_student = Student(
        roll_number=data.get('roll_number'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name')
    )
    db.session.add(new_student)
    db.session.commit()
    return new_student.serialize(), 201


class EnrollmentAPI(Resource):
  def get(self, student_id):
    if not Student.query.filter_by(student_id=student_id).first():
      return error('ENROLLMENT002'), 400
    enrollments = Enrollment.query.filter_by(student_id=student_id).all()
    if enrollments == []:
      return 'Student is not enrolled in any courses', 404
    return [enrollment.serialize() for enrollment in enrollments]

  def post(self, student_id):
    try:
      data = request.get_json()
    except:
      return error('BAD_REQUEST'), 400
    if not Student.query.filter_by(student_id=student_id).first():
      return error('ENROLLMENT002'), 400
    db.session.add(Enrollment(
        student_id=student_id,
        course_id=data.get('course_id')
    ))
    db.session.commit()
    enrollments = Enrollment.query.filter_by(student_id=student_id).all()
    return [enrollment.serialize() for enrollment in enrollments]

  def delete(self, student_id, course_id):
    if not Student.query.filter_by(student_id=student_id).first():
      return error('ENROLLMENT002'), 400
    if not Course.query.filter_by(course_id=course_id).first():
      return error('ENROLLMENT001'), 400
    enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
    if not enrollment:
      return 'Enrollment for the student not found', 404
    db.session.delete(enrollment)
    db.session.commit()
    return 'Successfully deleted'


api.add_resource(CourseAPI, '/api/course/<int:course_id>',
                 '/api/course')
api.add_resource(StudentAPI, '/api/student/<int:student_id>',
                 '/api/student')
api.add_resource(EnrollmentAPI, '/api/student/<int:student_id>/course',
                 '/api/student/<int:student_id>/course/<int:course_id>')
