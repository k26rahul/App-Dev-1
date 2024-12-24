from sqlalchemy import Column, Integer, Date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  dob = Column(Date, nullable=False)
