from flask import Blueprint, render_template

customer_bp = Blueprint('customer', __name__)


@customer_bp.route('/customer/home')
def customer_home():
  return render_template('customer_home.html')
