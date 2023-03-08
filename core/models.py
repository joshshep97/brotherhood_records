from .datebase import db
from flask_login import UserMixin
import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique=True, nullable=False)
    name = db.Column(db.String(55))
    password = db.Column(db.String(55), nullable=False)
    email = db.Column(db.String(55), nullable=False)
    favourite_genre_one = db.Column(db.String(255))
    favourite_genre_two = db.Column(db.String(255))
    favourite_genre_three = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Date, default=datetime.datetime.now())

    def to_dict(self):
        return {
            'id': self.id,
            ''
            'name': self.name,

        }

