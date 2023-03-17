from marshmallow import Schema, fields, post_dump
from model.assets_model import Asset
from model.threats_model import Threat
from model.risks_model import Risk


class AssetSchema(Schema):
    name = fields.String()
    asset_type = fields.String()
    owner = fields.String()
    location = fields.String()
    value = fields.Float()
    description = fields.String()


class ThreatSchema(Schema):
    name = fields.String()
    description = fields.String()


class RiskSchema(Schema):
    likelihood = fields.Float()
    impact = fields.Float()
    risk_score = fields.Float()
    risk_rating = fields.String()


class ReportSchema(Schema):
    asset = fields.Nested(AssetSchema)
    threat = fields.Nested(ThreatSchema)
    risk = fields.Nested(RiskSchema)

    @post_dump
    def remove_null(self, data, **kwargs):
        return {key: value for key, value in data.items() if value is not None}
