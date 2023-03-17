from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from model.users_model import User
from schema.users_schema import user_schema, users_schema
from app import db

user = Blueprint('user', __name__, url_prefix="/users")


# Retrieve all users (testing only)
@user.get("/")
def get_users():
    users = User.query.all()
    return users_schema.dump(users)


# get a specific user by id (testing only)
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

# User login for access token
@user.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        access_token = create_access_token(identity=user.id)
        return jsonify(message='Login succeeded.', access_token=access_token)
    else:
        return jsonify(message='Invalid email or password.'), 401



# update a specific user by id
@user.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    current_user_id = get_jwt_identity()
    if user_id != current_user_id:
        return jsonify({'message': 'Unauthorised request'}), 401

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
@jwt_required()
def delete_user(user_id):
    current_user_id = get_jwt_identity()
    if current_user_id != user_id:
        return jsonify({'message': 'Not authorised to delete this user'}), 403

    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 204
    except:
        return jsonify({'message': 'User not found'}), 404

