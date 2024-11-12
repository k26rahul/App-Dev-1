from flask import Flask, request, jsonify
from flask_restful import Api, Resource
# from flask_cors import CORS
from models import db, Course, Student, Enrollment


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_database.sqlite3'
api = Api(app)
db.init_app(app)

# allow cors [https://onlinedegree.gitlab.io]
# CORS(app, resources={r"/*": {"origins": "*"}})


ERROR_CODES = {
    # course
    "COURSE001": "Course Name is required",
    "COURSE002": "Course Code is required",
    # student
    "STUDENT001": "Roll Number required",
    "STUDENT002": "First Name is required",
    # enrollment
    "ENROLLMENT001": "Course does not exist",
    "ENROLLMENT002": "Student does not exist",
    # general
    "RESOURCE_ALREADY_EXISTS": "Resource already exists",
    "RESOURCE_NOT_FOUND": "Resource not found",
    "MISSING_REQUIRED_FIELDS": "Missing required fields",
    "BAD_REQUEST": "Bad Request"
}


def error(error_code):
  return {"error_code": error_code, "error_message": ERROR_CODES[error_code]}


class CourseAPI(Resource):
  def get(self, course_id):
    course = Course.query.get(course_id)
    if not course:
      return error("RESOURCE_NOT_FOUND"), 404
    return course.serialize(), 200

  def put(self, course_id):
    try:
      data = request.get_json()
    except Exception:
      return error("BAD_REQUEST"), 400

    course = Course.query.get(course_id)
    if not course:
      return error("RESOURCE_NOT_FOUND"), 404

    course.course_name = data.get("course_name", course.course_name)
    course.course_code = data.get("course_code", course.course_code)
    course.course_description = data.get("course_description", course.course_description)
    db.session.commit()
    return course.serialize(), 200

  def delete(self, course_id):
    course = Course.query.get(course_id)
    if not course:
      return error("RESOURCE_NOT_FOUND"), 404

    db.session.delete(course)
    db.session.commit()
    return {"message": "Course deleted successfully"}, 200


class CourseListAPI(Resource):
  def post(self):
    try:
      data = request.get_json()
    except Exception:
      return error("BAD_REQUEST"), 400

    if not data.get("course_name"):
      return error("COURSE001"), 400
    if not data.get("course_code"):
      return error("COURSE002"), 400

    if Course.query.filter_by(course_code=data["course_code"]).first():
      return error("RESOURCE_ALREADY_EXISTS"), 409

    new_course = Course(
        course_name=data["course_name"],
        course_code=data["course_code"],
        course_description=data.get("course_description"),
    )
    db.session.add(new_course)
    db.session.commit()
    return new_course.serialize(), 201


class StudentAPI(Resource):
  def get(self, student_id):
    student = Student.query.get(student_id)
    if not student:
      return error("RESOURCE_NOT_FOUND"), 404
    return student.serialize(), 200

  def put(self, student_id):
    try:
      data = request.get_json()
    except Exception:
      return error("BAD_REQUEST"), 400

    student = Student.query.get(student_id)
    if not student:
      return error("RESOURCE_NOT_FOUND"), 404

    student.first_name = data.get("first_name", student.first_name)
    student.last_name = data.get("last_name", student.last_name)
    student.roll_number = data.get("roll_number", student.roll_number)
    db.session.commit()
    return student.serialize(), 200

  def delete(self, student_id):
    student = Student.query.get(student_id)
    if not student:
      return error("RESOURCE_NOT_FOUND"), 404
    db.session.delete(student)
    db.session.commit()
    return {"message": "Student deleted successfully"}, 200


class StudentListAPI(Resource):
  def post(self):
    try:
      data = request.get_json()
    except Exception:
      return error("BAD_REQUEST"), 400

    if not data.get("roll_number"):
      return error("STUDENT001"), 400
    if not data.get("first_name"):
      return error("STUDENT002"), 400

    if Student.query.filter_by(roll_number=data["roll_number"]).first():
      return error("RESOURCE_ALREADY_EXISTS"), 409

    new_student = Student(
        roll_number=data["roll_number"],
        first_name=data["first_name"],
        last_name=data.get("last_name"),
    )
    db.session.add(new_student)
    db.session.commit()
    return new_student.serialize(), 201


class EnrollmentAPI(Resource):
  def get(self, student_id):
    enrollments = Enrollment.query.filter_by(student_id=student_id).all()
    if not enrollments:
      return error("RESOURCE_NOT_FOUND"), 404
    return [enrollment.serialize() for enrollment in enrollments], 200

  def post(self, student_id):
    try:
      data = request.get_json()
    except Exception:
      return error("BAD_REQUEST"), 400

    course_id = data.get("course_id")
    student = Student.query.get(student_id)
    course = Course.query.get(course_id)
    if not student:
      return error("ENROLLMENT002"), 404
    if not course:
      return error("ENROLLMENT001"), 404

    if Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first():
      return error("RESOURCE_ALREADY_EXISTS"), 409

    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    return enrollment.serialize(), 201

  def delete(self, student_id, course_id):
    student = Student.query.get(student_id)
    course = Course.query.get(course_id)

    if not student or not course:
      return error("BAD_REQUEST"), 400

    enrollment = Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()
    if not enrollment:
      return error("RESOURCE_NOT_FOUND"), 404

    db.session.delete(enrollment)
    db.session.commit()
    return {"message": "Enrollment deleted successfully"}, 200


# endpoints
api.add_resource(CourseAPI, '/api/course/<int:course_id>')
api.add_resource(CourseListAPI, '/api/course')
api.add_resource(StudentAPI, '/api/student/<int:student_id>')
api.add_resource(StudentListAPI, '/api/student')
api.add_resource(EnrollmentAPI, '/api/student/<int:student_id>/course', endpoint="enroll")
api.add_resource(EnrollmentAPI, '/api/student/<int:student_id>/course/<int:course_id>', endpoint="unenroll")


def populate_db():
  if not Student.query.first():
    # create students
    vidu = Student(roll_number="VIDU001", first_name="Vidu", last_name="")
    rahul = Student(roll_number="RAHUL001", first_name="Rahul", last_name="")
    harikesh = Student(roll_number="HARIKESH001", first_name="Harikesh", last_name="")

    db.session.add_all([vidu, rahul, harikesh])
    db.session.commit()

    # create courses
    maths = Course(course_name="Maths", course_code="MATHS101")
    stats = Course(course_name="Stats", course_code="STATS101")
    pdsa = Course(course_name="PDSA", course_code="PDSA101")
    dbms = Course(course_name="DBMS", course_code="DBMS101")

    db.session.add_all([maths, stats, pdsa, dbms])
    db.session.commit()

    # enrollments
    db.session.add_all([
        Enrollment(student_id=vidu.student_id, course_id=maths.course_id),
        Enrollment(student_id=vidu.student_id, course_id=stats.course_id),
        Enrollment(student_id=rahul.student_id, course_id=pdsa.course_id),
        Enrollment(student_id=rahul.student_id, course_id=dbms.course_id),
        Enrollment(student_id=harikesh.student_id, course_id=maths.course_id)
    ])
    db.session.commit()


if __name__ == '__main__':
  with app.app_context():
    db.create_all()  # create tables if they don't exist
    populate_db()    # populate the database
  app.run(debug=True)
