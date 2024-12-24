from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  email = Column(String, unique=True)
  password = Column(String)
  name = Column(String)
  type = Column(String)  # admin, customer
  customer = relationship('Customer', back_populates='user', uselist=False)
  admin = relationship('Admin', back_populates='user', uselist=False)


class Admin(db.Model):
  __tablename__ = 'admins'
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship('User', back_populates='admin')


class Customer(db.Model):
  __tablename__ = 'customers'
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship('User', back_populates='customer')
