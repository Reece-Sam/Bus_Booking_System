from flask import Blueprint, request, jsonify
from extensions import db
from models import User

user_bp = Blueprint('user_bp', __name__)


# This route creates users
@user_bp.route('/users', methods=['POST'])
def create_user():
   """
Create User
---
tags:
  - Users
parameters:
  - name: body
    in: body
    required: true
    schema:
      type: object
      required:
        - name
        - phone_number
      properties:
        name:
          type: string
          example: John Doe
        phone_number:
          type: string
          example: "237612345678"
responses:
  201:
    description: User created successfully
  400:
    description: Missing required fields
"""

   data = request.get_json()

   user = User(
        name=data.get('name'),
        phone_number=data.get('phone_number')
    )

   db.session.add(user)
   db.session.commit()

   return jsonify({"message": "User created", "user_id": user.id})

# #This routes gets users
# @user_bp.route('/users', methods=['GET'])
# def get_user():
#   all_user=User.query.all()
#   return jsonify([user.to_dict() for user in all_user]), 200

# Get all Users
@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Get All Users
    ---
    tags:
      - Users
    responses:
      200:
        description: List of users
    """

    all_user = User.query.all()

    return jsonify([{
        "id": user.id,
        "name": user.name,
        "phone_number": user.phone_number
    } for user in all_user])


#Gets user by Id
@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """
    Get User by ID
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: User ID
    responses:
      200:
        description: User found
      404:
        description: User not found
    """

    user = db.session.get(User, id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "name": user.name,
        "phone_number": user.phone_number
    }), 200


#This routes updates user by Id
@user_bp.route('/users/<int:id>', methods=['PATCH'])
def update_user(id):
    """
    Update User
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: User ID
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
                example: Updated Name
              phone_number:
                type: string
                example: "237699999999"
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
    """

    user = User.query.get(id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()

    if 'name' in data:
        user.name = data['name']
    
    if 'phone_number' in data:
        user.phone_number = data['phone_number']

    db.session.commit()

    return jsonify({
        "message": "User updated successfully",
        "user": {
            "id": user.id,
            "name": user.name,
            "phone_number": user.phone_number
        }
    }), 200



#This route deletes a user based on Id 
@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    Delete User
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: User ID
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """

    user = db.session.get(User, id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"}), 200