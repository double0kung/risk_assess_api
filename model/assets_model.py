from app import db

class Asset(db.Model):
    __tablename__ = "assets"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False) # name of asset
    asset_type = db.Column(db.String()) #classification of the asset based on its characteristics or attributes
    owner = db.Column(db.String()) # name of owner of asset
    location = db.Column(db.String()) # location of asset ie cloud or physical address
    value = db.Column(db.Float()) # value in dollars
    importance_rating = db.Column(db.Float()) # Importance rating of the asset on a scale of 1-10
    description = db.Column(db.String()) # short description of asset's purpose or use case
    
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    user = db.relationship('User', backref='assets')
