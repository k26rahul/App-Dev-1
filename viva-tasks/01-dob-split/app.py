from flask import Flask
from routes import default_bp
from models import db, User
from datetime import date


def create_app():
  app = Flask(__name__)
  app.register_blueprint(default_bp)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
  db.init_app(app)
  with app.app_context():
    db.create_all()
    db.session.add(User(dob=date(2020, 1, 1)))
    db.session.commit()

  return app


if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)
