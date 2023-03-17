from app import db

class Threat(db.Model):
    __tablename__ = "threats"

    threat_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False) # name of threat
    threat_type = db.Column(db.String()) # type of threat
    description = db.Column(db.String()) # brief description of the threat
