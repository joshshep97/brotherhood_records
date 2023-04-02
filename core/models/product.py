from . import db


class Product(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(255),
        nullable=False
    )
    artist = db.Column(
        db.String(255),
        nullable=False
    )
    genre = db.Column(
        db.String(50),
        nullable=False
    )
    price = db.Column(
        db.Float,
        nullable=False
    )

    price_id = db.Column(
        db.String,
        nullable=False
    )

    release_year = db.Column(
        db.Integer,
        nullable=False
    )

    img_url = db.Column(
        db.String,
        default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6MRaoLrXR-f8Gty7eh9R8OnmLJVlX6WPcbw&usqp=CAU'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'genre': self.genre,
            'price': self.price,
            'price_id': self.price_id,
            'release_year': self.release_year,
            'img_url': self.img_url
        }

    def __repr__(self):
        return f'{self.title} - {self.artist}'
