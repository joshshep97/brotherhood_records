from . import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique=True, nullable=False)
    password = db.Column(db.String(55), nullable=False)
    email = db.Column(db.String(55), nullable=False)
    favourite_genre_one = db.Column(db.String(255))
    favourite_genre_two = db.Column(db.String(255))
    favourite_genre_three = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Date, default=datetime.now())

