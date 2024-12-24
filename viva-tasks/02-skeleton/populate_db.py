from models import *
from werkzeug.security import generate_password_hash


def populate():
  db.session.add(Admin(
      user=User(
          email='admin1@example.com',
          password=generate_password_hash('12345'),
          name='vidu',
          type='admin'
      )
  ))
  db.session.add(Customer(
      user=User(
          email='customer1@example.com',
          password=generate_password_hash('12345'),
          name='muskan',
          type='customer'
      )
  ))
  db.session.commit()
