from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended.exceptions import JWTDecodeError
from model.risks_model import Risk
from model.assets_model import Asset
from model.threats_model import Threat
from model.users_model import User
from schema.risks_schema import risk_schema, risks_schema, risk_request_schema, RiskRequestSchema
from app import db

risk = Blueprint('risk', __name__, url_prefix="/risks")


# Create new risk
@risk.route("/", methods=["POST"])
@jwt_required()
def create_risk():
    current_user_id = get_jwt_identity()
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

    # Validate impact and likelihood values
    impact = data.get('impact')
    likelihood = data.get('likelihood')
    if not 1 <= impact <= 5:
        return jsonify({'message': 'Invalid impact value. Impact must be between 1 and 5.'}), 422
    if not 1 <= likelihood <= 5:
        return jsonify({'message': 'Invalid likelihood value. Likelihood must be between 1 and 5.'}), 422

    # Calculate risk score and rating
    risk_score = impact * likelihood
    if risk_score <= 5:
        risk_rating = 'Very Low'
    elif risk_score <= 10:
        risk_rating = 'Low'
    elif risk_score <= 15:
        risk_rating = 'Medium'
    elif risk_score <= 20:
        risk_rating = 'High'
    else:
        risk_rating = 'Very High'

    # Create new risk
    new_risk = Risk(
        impact=impact,
        likelihood=likelihood,
        risk_score=risk_score,
        risk_rating=risk_rating,
        user_id=current_user_id,
        asset_id=asset_id,
        threat_id=threat_id
    )

    # Add new risk to database
    db.session.add(new_risk)
    db.session.commit()

    # Return new risk
    message = f"Risk rating has been registered for the asset \"{asset.name}\" and threat \"{threat.name}\""
    return jsonify({'message': message, 'data': risk_schema.dump(new_risk)}), 201


# Retrieve the user's risk list
@risk.route("/", methods=["GET"])
@jwt_required()
def get_risks():
    try:
        # Get user_id from JWT token
        user_id = get_jwt_identity()

        # Filter risks by user_id
        risks = Risk.query.filter_by(user_id=user_id).all()

        # Serialize the query
        result = risks_schema.dump(risks)

        # Get user name
        user = User.query.get(user_id)
        first_name = user.first_name

        message = f"{first_name}'s risk register"

        # Return the data and message
        return jsonify({"message": message, "data": result}), 200

    except Exception as e:
        return jsonify({"message": "Unauthorised request", "error": str(e)}), 401


# Update Risks
@risk.route("/<int:risk_id>", methods=["PUT"])
@jwt_required()
def update_risk(risk_id):
    data = request.get_json()

    # Validate the incoming request data against the schema
    errors = RiskRequestSchema().validate(data, partial=True)
    if errors:
        # Errors in the data sent in the request, and can't be processed
        return jsonify(errors), 422

    # Try to get the risk with the given id
    risk = Risk.query.get(risk_id)
    if not risk:
        # Return a 404 Not Found if the risk with the given id does not exist
        return jsonify({'message': 'Risk not found'}), 404

    # Get user_id from JWT token
    user_id = get_jwt_identity()
    if user_id != risk.user_id:
        # Return a 401 Unauthorized if the user does not have permission to update the risk
        return jsonify({'message': 'You are not authorized to update this risk.'}), 401

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

        # Validate likelihood and impact values
        if 'likelihood' in data:
            likelihood = data['likelihood']
            if likelihood < 1 or likelihood > 5:
                raise ValueError('Invalid likelihood value')

        if 'impact' in data:
            impact = data['impact']
            if impact < 1 or impact > 5:
                raise ValueError('Invalid impact value')

        # Recalculate risk score and rating
        asset = Asset.query.get(risk.asset_id)
        if not asset:
            raise ValueError(f"Asset not found for asset_id {risk.asset_id}")
        impact = data['impact']
        likelihood = data['likelihood']
        risk_score = impact * likelihood
        if risk_score <= 5:
            risk_rating = 'Very Low'
        elif risk_score <= 10:
            risk_rating = 'Low'
        elif risk_score <= 15:
            risk_rating = 'Medium'
        elif risk_score <= 20:
            risk_rating = 'High'
        else:
            risk_rating = 'Very High'
        risk.risk_score = risk_score
        risk.risk_rating = risk_rating

        # Save the changes to the database
        db.session.commit()

        # Serialize the updated risk data
        result = risk_schema.dump(risk)

        # Return the serialized data
        return jsonify(result), 200

    except ValueError as e:
        # Rollback the changes and return a 400 Bad Request with error message
        db.session.rollback()
        return jsonify({'message': str(e)}), 400

    except:
        # Rollback the changes and return a 500 Internal Server Error
        db.session.rollback()
        return jsonify({'message': 'An error occurred while updating the risk.'}), 500




# Delete Risk
@risk.route("/<int:risk_id>", methods=["DELETE"])
@jwt_required()
def delete_risk(risk_id):
    # Get the current user's id
    current_user_id = get_jwt_identity()

    # Get the risk to delete
    risk = Risk.query.get(risk_id)

    # Check if risk exists
    if not risk:
        return jsonify({'message': 'Risk not found'}), 404

    # Check if the risk belongs to the current user
    if risk.user_id != current_user_id:
        return jsonify({'message': 'Unauthorized to delete this risk'}), 401

    # Delete risk from database
    db.session.delete(risk)
    db.session.commit()

    # Return success message
    return jsonify({'message': 'Risk deleted successfully'}), 200