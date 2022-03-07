from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80),)
    lastname = db.Column(db.String(80),)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, firstname, lastname, email, username, password, date_created):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'User {self.username}'