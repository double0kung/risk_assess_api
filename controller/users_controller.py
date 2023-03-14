from flask import Blueprint, request
from model.users_model import User
from schema.users_schema import user_schema, users_schema
from app import db

user = Blueprint('user', __name__, url_prefix="/users")

@user.get("/")
def get_users():
    users = User.query.all()
    return users_schema.dump(users)

@user.get("/<int:id>")
def get_user(id):
    user = User.query.get(id)

    if not user:
        return { "message": "Don't try to hack me" }

    return user_schema.dump(user)

@user.post("/")
def create_user():
    try:
        user_fields = user_schema.load(request.json)
        user = User(**user_fields)

        db.session.add(user)
        db.session.commit()
    except:
        return { "message": "Your information is incorrect" }

    return user_schema.dump(user)