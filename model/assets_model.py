from app import db

class Asset(db.Model):
    __tablename__ = "assets"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    asset_type = db.Column(db.String())
    owner = db.Column(db.String())
    location = db.Column(db.String())
    value = db.Column(db.Float())
    weight = db.Column(db.Float())
    description = db.Column(db.String())
    
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    user = db.relationship('User', backref='assets')
