from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)

    email = db.Column(db.String(), nullable=False, unique=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    password = db.Column(db.String())
