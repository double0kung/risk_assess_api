from app import ma

class RiskSchema(ma.Schema):
    class Meta:
        fields = ("risk_id", "impact", "likelihood", "risk_score", "risk_rating", "user_id", "asset_id", "threat_id")

class RiskRequestSchema(ma.Schema):
    class Meta:
        fields = ("impact", "likelihood", "user_id", "asset_id", "threat_id")

risk_schema = RiskSchema()
risks_schema = RiskSchema(many=True)

risk_request_schema = RiskRequestSchema()
risks_request_schema = RiskRequestSchema(many=True)

