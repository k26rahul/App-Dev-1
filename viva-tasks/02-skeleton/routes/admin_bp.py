from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin/home')
@login_required  # <<< ensure authentication
def admin_home():
  if current_user.type != 'admin':  # <<< ensure authorization
    return 'YOU ARE NOT PERMITTED TO ENTER THIS SECTION OF WEBSITE', 403

  return render_template('admin_home.html')
