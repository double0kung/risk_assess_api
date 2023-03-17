from flask import Blueprint, request, jsonify
from model.risks_model import Risk
from model.assets_model import Asset
from model.threats_model import Threat
from schema.risks_schema import risk_schema, risks_schema, risk_request_schema, RiskRequestSchema
from app import db

risk = Blueprint('risk', __name__, url_prefix="/risks")


# Create new risk
@risk.route("/", methods=["POST"])
def create_risk():
    data = request.get_json()

    # Get asset by ID
    asset_id = data['asset_id']
    asset = Asset.query.get(asset_id)
    if not asset:
        return jsonify({'message': 'Asset not found'}), 404

    # Get threat by ID
    threat_id = data['threat_id']
    threat = Threat.query.get(threat_id)
    if not threat:
        return jsonify({'message': 'Threat not found'}), 404

    # Calculate risk score and rating
    impact = data['impact']
    likelihood = data['likelihood']
    asset_importance = asset.importance_rating
    risk_score = (impact + likelihood + asset_importance) / 3
    if risk_score <= 2:
        risk_rating = 'Very Low'
    elif risk_score <= 4:
        risk_rating = 'Low'
    elif risk_score <= 6:
        risk_rating = 'Medium'
    elif risk_score <= 8:
        risk_rating = 'High'
    else:
        risk_rating = 'Very High'

    # Create new risk
    new_risk = Risk(
        impact=impact,
        likelihood=likelihood,
        asset_importance=asset_importance,
        risk_score=risk_score,
        risk_rating=risk_rating,
        user_id=data['user_id'],
        asset_id=asset_id,
        threat_id=threat_id
    )

    # Add new risk to database
    db.session.add(new_risk)
    db.session.commit()

    # Return new risk
    return risk_schema.jsonify(new_risk), 201

# Retrieve all risks
@risk.route("/", methods=["GET"])
def get_risks():
    # Get all risks
    risks = Risk.query.all()

    # Serialize the queryset
    result = risks_schema.dump(risks)

    # Return the serialized data
    return jsonify(result)

# Update Risks
@risk.route("/<int:risk_id>", methods=["PUT"])
def update_risk(risk_id):
    data = request.get_json()

    # Validate the incoming request data against the schema
    errors = RiskRequestSchema().validate(data, partial=True)
    if errors:
        # Return a 422 Unprocessable Entity and the validation errors
        return jsonify(errors), 422

    # Try to get the risk with the given id
    risk = Risk.query.get(risk_id)
    if not risk:
        # Return a 404 Not Found if the risk with the given id does not exist
        return jsonify({'message': 'Risk not found'}), 404

    # Update the existing risk object
    for key, value in data.items():
        if hasattr(risk, key): # returns True if an object has a given attribute
            setattr(risk, key, value)

    try:
        # Check if asset_id exists
        if 'asset_id' in data:
            asset_id = data['asset_id']
            asset = Asset.query.get(asset_id)
            if not asset:
                raise ValueError(f"Asset not found for asset_id {asset_id}")
            risk.asset_id = asset_id

        # Check if threat_id exists
        if 'threat_id' in data:
            threat_id = data['threat_id']
            threat = Threat.query.get(threat_id)
            if not threat:
                raise ValueError(f"Threat not found for threat_id {threat_id}")
            risk.threat_id = threat_id

        # Recalculate risk score and rating
        asset = Asset.query.get(risk.asset_id)
        if not asset:
            raise ValueError(f"Asset not found for asset_id {risk.asset_id}")
        risk.risk_score = (risk.impact + risk.likelihood + asset.importance_rating) / 3
        if risk.risk_score <= 2:
            risk.risk_rating = 'Very Low'
        elif risk.risk_score <= 4:
            risk.risk_rating = 'Low'
        elif risk.risk_score <= 6:
            risk.risk_rating = 'Medium'
        elif risk.risk_score <= 8:
            risk.risk_rating = 'High'
        else:
            risk.risk_rating = 'Very High'

        # Save the changes to the database
        db.session.commit()

        # Serialize the updated risk data
        result = risk_schema.dump(risk)

        # Return the serialized data
        return jsonify(result), 200

    except ValueError as e:
        # Rollback the changes and return a 404 Not Found with error message
        db.session.rollback()
        return jsonify({'message': str(e)}), 404

    except:
        # Rollback the changes and return a 500 Internal Server Error
        db.session.rollback()
        return jsonify({'message': 'An error occurred while updating the risk.'}), 500




# Delete Risk
@risk.route("/<int:risk_id>", methods=["DELETE"])
def delete_risk(risk_id):
    # Get the risk to delete
    risk = Risk.query.get(risk_id)

    # Check if risk exists
    if not risk:
        return jsonify({'message': 'Risk not found'}), 404

    # Delete risk from database
    db.session.delete(risk)
    db.session.commit()

    # Return success message
    return jsonify({'message': 'Risk deleted successfully'}), 200





