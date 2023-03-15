from flask_login import UserMixin
import datetime

from .import db

class User(UserMixin, db.Model):
    # required
    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    username = db.Column(
        db.String(55), 
        unique=True, 
        nullable=False
    )
    password = db.Column(
        db.String(55), 
        nullable=False
    )
    email = db.Column(
        db.String(55), 
        nullable=False
    )

    # not required attributes set to a default value
    name = db.Column(
        db.String(55), 
        default='User'
    )
    favourite_genre_one = db.Column(
        db.String(255), 
        default='Not Set'
    )
    favourite_genre_two = db.Column(
        db.String(255), 
        default='Not Set'
    )
    favourite_genre_three = db.Column(
        db.String(255), 
        default='Not Set'
    )
    is_admin = db.Column(
        db.Boolean, 
        default=False
    )
    date_created = db.Column(
        db.Date, 
        default=datetime.datetime.now()
    )

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'favourite_genre_one': self.favourite_genre_one,
            'favourite_genre_two': self.favourite_genre_two,
            'favourite_genre_three': self.favourite_genre_three,
            'is_admin': self.is_admin,
            'date_created': self.date_created,
        }

