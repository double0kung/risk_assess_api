from app import db

class Report(db.Model):
    __tablename__ = "reports"

    report_id = db.Column(db.Integer(), primary_key=True)
    asset_name = db.Column(db.String(), nullable=False)
    asset_type = db.Column(db.String())
    owner = db.Column(db.String())
    location = db.Column(db.String())
    value = db.Column(db.Float())
    description = db.Column(db.String())
    threat_name = db.Column(db.String(), nullable=False)
    threat_type = db.Column(db.String())
    threat_description = db.Column(db.String())
    likelihood = db.Column(db.Integer(), nullable=False)
    impact = db.Column(db.Integer(), nullable=False)
    risk_score = db.Column(db.Integer(), nullable=False)
    risk_rating = db.Column(db.String(), nullable=False)

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    user = db.relationship('User', backref='reports')
