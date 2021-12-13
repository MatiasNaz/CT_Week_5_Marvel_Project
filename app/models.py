from unicodedata import name
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
import uuid



db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.uuid(), primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    MarvelCharacter = db.relationship('MarvelCharacter', backref='author', lazy=True)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        
class MarvelCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.String(300), nullable=False)
    comics_appeared_in = db.Column(db.Integer)
    super_power = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def __init__(self, name, description, comics_appeared_in, super_power, date_created, owner):
        self.name = name 
        self.description = description
        self.comics_appeared_in = comics_appeared_in
        self.super_power = super_power
        self.date_created = date_created
        self.owner = owner

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False, unique=False)
#     price = db.Column(db.Float())
#     image = db.Column(db.String())
#     description = db.Column(db.String())
#     created_on = db.Column(db.DateTime(), default=datetime.utcnow)

#     def __init__(self, name, price, image, description):
#         self.name = name
#         self.price = price
#         self.image = image
#         self.description = description

#     def to_dict(self):
#         return {
#             'id' : self.id,
#             'name': self.name,
#             'price': self.price,
#             "image": self.image,
#             'description': self.description,
#             "created_on": self.created_on
#         }