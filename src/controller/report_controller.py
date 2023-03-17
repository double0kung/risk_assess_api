from flask import Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from model.assets_model import Asset
from model.threats_model import Threat
from model.risks_model import Risk
from schema.assets_schema import AssetSchema
from schema.threats_schema import ThreatSchema
from schema.risks_schema import RiskSchema

report = Blueprint("report", __name__, url_prefix="/report")

# Define schemas
asset_schema = AssetSchema()
threat_schema = ThreatSchema()
risk_schema = RiskSchema()

# Table function
def tabulate_data(assets):
    table_data = []
    for asset in assets:
        for risk in asset.risks:
            threat = risk.threat
            row = {
                "Asset": asset.name,
                "Type": asset.asset_type,
                "Owner": asset.owner,
                "Location": asset.location,
                "Value": asset.value,
                "Description": asset.description,
                "Threat": threat.name,
                "Likelihood": risk.likelihood,
                "Impact": risk.impact,
                "Score": risk.risk_score,
                "Rating": risk.risk_rating,
            }
            table_data.append(row)
    return table_data


# Generate Table Report
@report.route("/", methods=["GET"])
@jwt_required()
def get_report():
    # Get user_id from JWT token
    user_id = get_jwt_identity()

    # Get all assets belonging to user and their associated risks
    assets = Asset.query.filter_by(user_id=user_id).all()

    # Tabulate the data and return as JSON
    table_data = tabulate_data(assets)
    return jsonify(table_data), 200
