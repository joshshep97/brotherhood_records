from flask_login import UserMixin
import datetime

from . import db

user_product = db.Table('user_product',
                        db.Column('user_id', db.Integer,
                                  db.ForeignKey('user.id')),
                        db.Column('product_id', db.Integer,
                                  db.ForeignKey('product.id'))
                        )


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
        db.Text,
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
    favorite_genres = db.relationship('FavoriteGenre',
                                      backref='user',
                                      lazy=True
                                      )
    is_admin = db.Column(
        db.Boolean,
        default=False
    )
    date_created = db.Column(
        db.Date,
        default=datetime.datetime.now()
    )
    collection = db.relationship(
        'Product', secondary=user_product, backref='collection', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'is_admin': self.is_admin,
            'date_created': self.date_created,
            'favorite_genres': [genre.to_dict() for genre in self.favorite_genres],
            'collection': [product.to_dict() for product in self.collection]
        }


class FavoriteGenre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'user_id': self.user_id
        }
