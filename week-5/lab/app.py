from flask import Flask, request, render_template, redirect
from models import session, Student

app = Flask(__name__)


@app.route('/')
def index():
  students = session.query(Student).all()
  return render_template('index.html', students=students)


if __name__ == '__main__':
  app.run(debug=True)
