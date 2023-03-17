from app import ma

class ThreatSchema(ma.Schema): # Create a new schema for Threat model
    class Meta: # Define the fields that should be included in the serialized output (convert to json)
        fields = ("threat_id", "name", "threat_type", "description")

threat_schema = ThreatSchema()
threats_schema = ThreatSchema(many=True)
