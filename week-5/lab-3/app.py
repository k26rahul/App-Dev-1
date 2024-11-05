from flask import Flask
from models import db
from routes.root_bp import root_bp
from routes.student_bp import student_bp
import populate_db


def create_app():
  # make app
  app = Flask(__name__)

  # register blueprints
  app.register_blueprint(root_bp)
  app.register_blueprint(student_bp)

  # database setup
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
  db.init_app(app)

  # make db tables and populate
  with app.app_context():
    db.create_all()
    populate_db.populate()

  return app


if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)
