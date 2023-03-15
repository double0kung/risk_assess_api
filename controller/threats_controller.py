from flask import Blueprint, request, jsonify
from model.threats_model import Threat
from schema.threats_schema import threat_schema, threats_schema
from app import db

threat = Blueprint('threat', __name__, url_prefix="/threats")


# Retrieve all threats
@threat.get("/")
def get_threats():
    threats = Threat.query.all()
    if not threats:
        return jsonify({"message": "No threats found."}), 404
    return threats_schema.dump(threats)


# get a specific threat by id
@threat.route("/<int:threat_id>", methods=["GET"])
def get_threat(threat_id):
    threat = Threat.query.get(threat_id)
    if not threat:
        return jsonify({'error': 'Threat not found'}), 404
    return threat_schema.dump(threat)


# create a new threat
@threat.route("/", methods=["POST"])
def create_threat():
    data = request.json
    name = data.get('name')
    threat_type = data.get('threat_type')
    description = data.get('description')

    threat = Threat(
        name=name,
        threat_type=threat_type,
        description=description
    )

    db.session.add(threat)
    db.session.commit()

    response = {
        "message": "Threat successfully created",
        "threat": threat_schema.dump(threat)
    }
    return jsonify(response), 201


# update a specific threat by id
@threat.route("/<int:threat_id>", methods=["PUT"])
def update_threat(threat_id):
    try:
        threat = Threat.query.get_or_404(threat_id)
        data = request.json
        threat.name = data.get('name', threat.name)
        threat.threat_type = data.get('threat_type', threat.threat_type)
        threat.description = data.get('description', threat.description)

        db.session.commit()

        response = {
            "message": "Threat successfully updated",
            "threat": threat_schema.dump(threat)
        }
        return jsonify(response), 200
    except:
        return jsonify({'message': 'Threat not found'}), 404


# delete a specific threat by id
@threat.route("/<int:threat_id>", methods=["DELETE"])
def delete_threat(threat_id):
    try:
        threat = Threat.query.get_or_404(threat_id)
        db.session.delete(threat)
        db.session.commit()
        return jsonify({'message': 'Threat deleted successfully'}), 204
    except:
        return jsonify({'message': 'Threat not found'}), 404

