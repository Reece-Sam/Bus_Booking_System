from flask import Blueprint, request, jsonify
from extensions import db
from models import User

user_bp = Blueprint('user_bp', __name__)


# This route creates users
@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    user = User(
        name=data['name'],
        phone_number=data['phone_number']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created", "user_id": user.id})


# #This routes gets users
# @user_bp.route('/users', methods=['GET'])
# def get_user():
#   all_user=User.query.all()
#   return jsonify([user.to_dict() for user in all_user]), 200

# Improved version of get users
@user_bp.route('/users', methods=['GET'])
def get_users():
    all_user = User.query.all()
    return jsonify([{
        "id": user.id,
        "name": user.name,
        "phone_number": user.phone_number
    } for user in all_user])


#Gets user by Id
@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = db.session.get(User, id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "phone_number": user.phone_number
    }), 200