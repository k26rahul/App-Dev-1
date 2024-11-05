from flask import Blueprint, render_template
from models import Student

root_bp = Blueprint('root', __name__)


@root_bp.route('/')
def index():
  # Student.query ~ session.query(Student)
  students = Student.query.all()
  return render_template('index.html', students=students)
