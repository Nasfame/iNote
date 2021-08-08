from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(128),nullable=False,unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(128),nullable=False)
    notes = db.relationship('Note')

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer,primary_key=True)
    data - db.Column(db.String(pow(10,200)))
    date = db.Column(db.DateTime(timezone=True),default = func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
