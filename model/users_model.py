from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)

    username = db.Column(db.String(), nullable=False, unique=True)
    verified = db.Column(db.Boolean())
    mobile_number = db.Column(db.String())
    post_code = db.Column(db.String())