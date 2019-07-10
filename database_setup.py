import sys, os
from datetime import datetime, timezone
# from time import gmtime, strftime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """ User model """

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    done = db.Column(db.Boolean, default=False)
    # time = db.Column(db.String(250), default=strftime("%a, %d %b %Y %H:%M:%S", gmtime()))
    time = db.Column(db.String(250), default=datetime.now(timezone.utc).astimezone().strftime("%a, %d %b %Y %H:%M:%S"))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

#
# engine = create_engine('sqlite:///todo.db')
# Base.metadata.create_all(engine)
