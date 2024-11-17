from flask import Blueprint, request, jsonify
from bson import ObjectId
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

    try:
        result = mongo.db.users.insert_one(user)
        user['_id'] = str(result.inserted_id)  # Convert ObjectId to string
        return jsonify(user), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if not user:
            return jsonify({'error': 'User not found'}), 404

        user['_id'] = str(user['_id'])  # Convert ObjectId to string
        return jsonify(user)
    except Exception as e:
        return jsonify({'error': str(e)}), 500