from flask import Flask
from models import db, Student
from populate_db import populate
from routes import bp


def create_app():
  app = Flask(__name__)
  app.register_blueprint(bp)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  db.init_app(app)
  with app.app_context():
    db.create_all()
    populate()

  return app


if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)
