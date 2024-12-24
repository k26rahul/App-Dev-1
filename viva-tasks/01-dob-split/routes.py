from flask import Blueprint, render_template, request, redirect
from models import User, db
from datetime import date

default_bp = Blueprint('default', __name__)


@default_bp.route('/')
def index():
  user = User.query.filter_by(id=1).first()
  return render_template('index.html', user=user)


@default_bp.route('/update-dob', methods=['GET', 'POST'])
def update_dob():
  user = User.query.filter_by(id=1).first()

  if request.method == 'GET':
    return render_template('update_dob.html', user=user)

  elif request.method == 'POST':
    dob = request.form.get('dob')

    y, m, d = dob.split('-')
    user.dob = date(int(y), int(m), int(d))

    db.session.commit()
    return redirect('/')
