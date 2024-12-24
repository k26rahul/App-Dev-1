from flask import Blueprint, redirect
from flask_login import current_user

root_bp = Blueprint('root', __name__)


@root_bp.route('/')
def root():
  if not current_user.is_authenticated:
    return redirect('/login')

  if current_user.type == 'admin':
    return redirect('/admin/home')

  if current_user.type == 'customer':
    return redirect('/customer/home')
