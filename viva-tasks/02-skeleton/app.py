from flask import Flask
from flask_login import LoginManager
from routes import root_bp, auth_bp, admin_bp, customer_bp
from models import db, User
from populate_db import populate


def create_app():
  app = Flask(__name__)
  app.secret_key = '12345'

  app.register_blueprint(root_bp)
  app.register_blueprint(auth_bp)
  app.register_blueprint(admin_bp)
  app.register_blueprint(customer_bp)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
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
  app.run(debug=True, port=8080)
