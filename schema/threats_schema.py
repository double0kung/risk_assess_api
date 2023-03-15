from app import ma

class ThreatSchema(ma.Schema):
    class Meta:
        fields = ("threat_id", "name", "threat_type", "description")

threat_schema = ThreatSchema()
threats_schema = ThreatSchema(many=True)
