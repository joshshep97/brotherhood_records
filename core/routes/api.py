from flask import Blueprint, jsonify, redirect, url_for, flash, request
from ..models import User, Product

from .. import db

from flask_login import current_user, login_required

api = Blueprint('api', __name__)

@api.route('/user/<int:id>/', methods=['GET'])
@login_required
def get_user(id):
    if not current_user.is_admin:
        flash('You are not authorised to view this page', 'error')
        return redirect(url_for('main.index'))
    else:
        user = User.query.filter_by(id=id).first()

        return jsonify(user.to_dict())

@api.route('/user/all', methods=['GET'])
@login_required
def get_all_users():
    if not current_user.is_admin:
        flash('You are not authorised to view this page', 'error')
        return redirect(url_for('main.index'))
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@api.route('/products/<int:id>/', methods=['GET'])
def get_product(id):
    product = Product.query.filter_by(id=id).first()
    return jsonify(product.to_dict())

@api.route('/products/all', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@api.route('/product/add', methods=['GET', 'POST'])
def add_product():
    if not current_user.is_admin:
        flash('You are not authorised to view this page', 'error')
        return redirect(url_for('main.index'))
    data = request.get_json()
    product = Product(
        title=data['title'],
        artist=data['artist'],
        img_url=data['img_url'],
        price=data['price'],
        price_id=data['price_id'],
        release_year=data['release_year'],
        genre=data['genre']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict())

# curl -X POST \
#      -H "Content-Type: application/json" \
#      -d '{"title": "New Product", "artist": "New Artist", "img_url": "https://example.com/image.jpg", "price": 9.99, "price_id": "p123", "release_year": 2022, "genre": "Rock"}' \
#      http://localhost:5000/product/add