import sys, os
import datetime
from time import gmtime, strftime
# from sqlalchemy import Column, ForeignKey, DateTime, String, Boolean, Integer
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin

db = SQLAlchemy()

# Base = declarative_base()

# class User(UserMixin, db.Model):
#     """ User model """
#
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(25), nullable=False)
#     email = db.Column(db.String(25), unique=True, nullable=False)
#     hashed_pswd = db.Column(db.String(), nullable=False)

class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    done = db.Column(db.Boolean, default=False)
    # time = Column(DateTime, default=datetime.datetime.now)
    time = db.Column(db.String(250), default=strftime("%a, %d %b %Y %H:%M:%S", gmtime()))

#
# engine = create_engine('sqlite:///todo.db')
# Base.metadata.create_all(engine)
