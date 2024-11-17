from flask import Blueprint, request, jsonify, current_app
from bson import ObjectId
from .models import mongo
import requests

bp = Blueprint('match', __name__)

@bp.route('/matches', methods=['POST'])
def create_match():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    users = data.get('users')
    game = data.get('game')

    # Validate users
    for user_id in users:
        user_response = requests.get(f"{current_app.config['USER_SERVICE_URL']}/{user_id}")
        if user_response.status_code != 200:
            return jsonify({'error': f"User with ID {user_id} not found"}), 400

    match = {
        'users': users,
        'game': game,
        'status': 'pending'
    }

    result = mongo.db.matches.insert_one(match)
    match['_id'] = str(result.inserted_id)  # Convert ObjectId to string
    return jsonify(match), 201

@bp.route('/matches/<match_id>', methods=['GET'])
def get_match(match_id):
    match = mongo.db.matches.find_one({'_id': ObjectId(match_id)})
    if not match:
        return jsonify({'error': 'Match not found'}), 404

    match['_id'] = str(match['_id'])  # Convert ObjectId to string
    return jsonify(match)