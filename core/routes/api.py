from flask import Blueprint, jsonify
from ..models import User


api = Blueprint('api', __name__)

@api.route('/user/<int:id>/', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()

    return jsonify(user.to_dict())
