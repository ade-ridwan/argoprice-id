from flask import Blueprint, request, jsonify
from app.models.user import User
from app.schemas.user_schema import user_schema
from app import db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validasi input
    if not data or not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({"status": "error", "message": "Data tidak lengkap"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"status": "error", "message": "Username sudah ada"}), 409

    new_user = User(
        username=data['username'],
        email=data['email'],
        role=data.get('role', 'user')
    )
    new_user.set_password(data['password'])

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            "status": "success",
            "message": "Registrasi berhasil",
            "data": user_schema.dump(new_user)
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    # Placeholder untuk logic JWT kamu nanti
    return jsonify({"message": "Endpoint login siap dikembangkan"}), 200
