##Set up db in the __init__.py later, it will share the same directory as this file
##Import db from myproject
from web-practice import db, datetime, est_now, login_manager
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

@login_manager.user_loader ##Loads current user, returns user from db
def load_user(user_id):
    '''Login_manager will load the current user_id from the db'''
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = Bcrypt().generate_password_hash(password=password)

    def check_password(self, password):
        return Bcrypt().check_password_hash(self.password_hash, password)


class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='Puppy', uselist=False)
    date = db.Column(db.DateTime, default=est_now)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    pup_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, pup_id):
        self.name = name
        self.pup_id = pup_id

    def __repr__(self):
        return f'{self.name}'
