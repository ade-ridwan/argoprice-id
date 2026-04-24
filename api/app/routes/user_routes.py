from flask import Blueprint, jsonify
from app.models.user import User
from app.schemas.user_schema import users_schema

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify({
        "status": "success",
        "data": users_schema.dump(users)
    }), 200
