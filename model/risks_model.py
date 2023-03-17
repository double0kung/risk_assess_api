from app import db

class Risk(db.Model):
    __tablename__ = "risks"

    risk_id = db.Column(db.Integer(), primary_key=True)
    impact = db.Column(db.Integer()) # impact rating of risk on a scale of 1-10
    likelihood = db.Column(db.Integer()) # likelihood rating of risk on a scale of 1-10
    asset_importance = db.Column(db.Float()) # Importance rating of the asset on a scale of 1-10
    risk_score = db.Column(db.Float()) # risk score based on impact, likelihood, asset importance, threat impact, and threat likelihood
    risk_rating = db.Column(db.String()) # risk rating from very low, low, medium, high, very high based on score

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    asset_id = db.Column(db.Integer(), db.ForeignKey('assets.asset_id'))
    threat_id = db.Column(db.Integer(), db.ForeignKey('threats.threat_id'))

    user = db.relationship('User', backref='risks')
    asset = db.relationship('Asset', backref='risks')
    threat = db.relationship('Threat', backref='risks')