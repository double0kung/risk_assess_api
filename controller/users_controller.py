from flask import Blueprint, request, jsonify
from model.users_model import User
from schema.users_schema import user_schema, users_schema
from app import db

user = Blueprint('user', __name__, url_prefix="/users")


# Retrieve all users
@user.get("/")
def get_users():
    users = User.query.all()
    return users_schema.dump(users)


# get a specific user by id
@user.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return user_schema.dump(user)


# create a new user
@user.route("/", methods=["POST"])
def create_user():
    data = request.json
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')

    # Check if user with email already exists
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error': 'User with email already exists'}), 409

    user = User(email=email, first_name=first_name, last_name=last_name, password=password)
    db.session.add(user)
    db.session.commit()
    response = {
        "message": "User successfully created",
        "user": user_schema.dump(user)
    }
    return jsonify(response), 201



# update a specific user by id
@user.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        data = request.json
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.password = data.get('password', user.password)
        db.session.commit()
        return jsonify({'message': 'User successfully updated'}), 200
    except:
        return jsonify({'message': 'User not found'}), 404


# delete a specific user by id
@user.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 204
    except:
        return jsonify({'message': 'User not found'}), 404
