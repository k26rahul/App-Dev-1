from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Father(db.Model):
  __tablename__ = 'fathers'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  child = relationship('Child', back_populates='father', uselist=False)


class Child(db.Model):
  __tablename__ = 'childs'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  father_id = Column(Integer, ForeignKey('fathers.id'))
  father = relationship('Father', back_populates='child')
