from flask import Blueprint, request, jsonify
from .models import mongo

bp = Blueprint('user', __name__)

@bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    user = {
        'username': data.get('username'),
        'email': data.get('email'),
        'password': data.get('password')
    }

    mongo.db.users.insert_one(user)
    return jsonify(user), 201

@bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo.db.users.find_one({'_id': user_id})
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user)