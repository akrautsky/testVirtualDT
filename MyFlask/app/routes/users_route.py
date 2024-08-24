from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, from users route!'})