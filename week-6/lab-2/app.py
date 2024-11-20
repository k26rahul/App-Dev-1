from flask import Flask
from models import db, Course
from populate_db import populate
from api import api
from flask_cors import CORS


def create_app():
  app = Flask(__name__)
  CORS(app, origins=['https://onlinedegree.gitlab.io'])

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  db.init_app(app)
  with app.app_context():
    db.create_all()
    populate()

  api.init_app(app)
  return app


if __name__ == '__main__':
  app = create_app()

  @app.route('/')
  def index():
    return f'hello from root, we have {Course.query.count()} courses available'

  app.run(debug=True)
