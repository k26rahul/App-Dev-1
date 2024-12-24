from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user
from models import User
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')

  elif request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
      login_user(user)  # <<< this line does login process
      return redirect('/')

    return render_template('login.html', error=True)


@auth_bp.route('/logout')
def logout():
  logout_user()
  return redirect('/login')
