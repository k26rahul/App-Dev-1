from flask import Flask
from flask_login import LoginManager
from models import db, User
from populate_db import populate
from routes import bp


def create_app():
  app = Flask(__name__)
  app.secret_key = '12345'
  app.register_blueprint(bp)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
  db.init_app(app)
  with app.app_context():
    db.create_all()
    if User.query.count() == 0:
      populate()

  login_manager = LoginManager()
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

  return app


if __name__ == '__main__':
  app = create_app()

  @app.route('/')
  def index():
    return 'hello from root'

  app.run(debug=True)
