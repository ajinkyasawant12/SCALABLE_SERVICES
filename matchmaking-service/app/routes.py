from flask import Blueprint, request, jsonify
from .models import mongo
import requests

bp = Blueprint('match', __name__)

@bp.route('/', methods=['POST'])
def create_match():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    users = data.get('users')
    game = data.get('game')

    # Validate users
    for user_id in users:
        user_response = requests.get(f"{app.config['USER_SERVICE_URL']}/{user_id}")
        if user_response.status_code != 200:
            return jsonify({'error': f"User with ID {user_id} not found"}), 400

    match = {
        'users': users,
        'game': game,
        'status': 'pending'
    }

    mongo.db.matches.insert_one(match)
    return jsonify(match), 201

@bp.route('/<match_id>', methods=['GET'])
def get_match(match_id):
    match = mongo.db.matches.find_one({'_id': match_id})
    if not match:
        return jsonify({'error': 'Match not found'}), 404

    return jsonify(match)