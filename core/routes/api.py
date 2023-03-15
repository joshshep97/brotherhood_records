from flask import Blueprint, jsonify
from ..models import User, Product


api = Blueprint('api', __name__)

@api.route('/user/<int:id>/', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()

    return jsonify(user.to_dict())


@api.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.filter_by(id=id).first()
    return jsonify(product.to_dict())

@api.route('/products/', methods=['GET'])
def get_products():
    all_products = Product.query.all()

    for product in all_products:
        return jsonify(product.to_dict())