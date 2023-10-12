from . import db 
from flask_login import UserMixin

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    price = db.Column(db.Double(20, 2))

    #how we can associate a note with a user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    #defining layout for object in our database
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    #link them to notes
    notes = db.relationship('Item') #can think of this like a list of note we can access by name