from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from model.assets_model import Asset
from schema.assets_schema import asset_schema, assets_schema

asset = Blueprint('asset', __name__, url_prefix="/assets")

# Retrieve all assets
@asset.get("/")
@jwt_required()
def get_assets():
    current_user_id = get_jwt_identity()
    assets = Asset.query.filter_by(user_id=current_user_id).all()
    if not assets:
        return jsonify({'message': 'No assets found.'}), 404
    return assets_schema.dump(assets)


# Get a specific asset by id
@asset.route("/<int:asset_id>", methods=["GET"])
@jwt_required()
def get_asset(asset_id):
    current_user_id = get_jwt_identity()
    asset = Asset.query.filter_by(id=asset_id, user_id=current_user_id).first()
    if not asset:
        return jsonify({'error': 'Asset not found or unauthorized'}), 404
    return asset_schema.dump(asset)

# Create a new asset
@asset.route("/", methods=["POST"])
@jwt_required()
def create_asset():
    data = request.json
    name = data.get('name')
    asset_type = data.get('asset_type')
    owner = data.get('owner')
    location = data.get('location')
    value = data.get('value')
    description = data.get('description')
    user_id = data.get('user_id')

    current_user_id = get_jwt_identity()
    if user_id != current_user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    asset = Asset(
        name=name,
        asset_type=asset_type,
        owner=owner,
        location=location,
        value=value,
        description=description,
        user_id=user_id
    )

    db.session.add(asset)
    db.session.commit()

    response = {
        "message": "Asset successfully created",
        "asset": asset_schema.dump(asset)
    }
    return jsonify(response), 201

# Update a specific asset by id
@asset.route("/<int:asset_id>", methods=["PUT"])
@jwt_required()
def update_asset(asset_id):
    current_user_id = get_jwt_identity()
    asset = Asset.query.filter_by(id=asset_id, user_id=current_user_id).first()
    if not asset:
        return jsonify({'message': 'Asset not found or unauthorized'}), 404

    data = request.json
    asset.name = data.get('name', asset.name)
    asset.asset_type = data.get('asset_type', asset.asset_type)
    asset.owner = data.get('owner', asset.owner)
    asset.location = data.get('location', asset.location)
    asset.value = data.get('value', asset.value)
    asset.description = data.get('description', asset.description)

    db.session.commit()

    response = {
        "message": "Asset successfully updated",
        "asset": asset_schema.dump(asset)
    }
    return jsonify(response), 200


# Delete a specific asset by id
@asset.route("/<int:asset_id>", methods=["DELETE"])
@jwt_required()
def delete_asset(asset_id):
    current_user_id = get_jwt_identity()
    asset = Asset.query.filter_by(id=asset_id, user_id=current_user_id).first()
    if not asset:
        return jsonify({'message': 'Asset not found or unauthorized'}), 404

    db.session.delete(asset)
    db.session.commit()
    return jsonify({'message': 'Asset deleted successfully'}), 204
