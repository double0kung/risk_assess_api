from flask import Blueprint, request, jsonify
from app import db
from model.assets_model import Asset
from schema.assets_schema import asset_schema, assets_schema

asset = Blueprint('asset', __name__, url_prefix="/assets")

# Retrieve all assets
@asset.get("/")
def get_assets():
    assets = Asset.query.all()
    if not assets:
        return jsonify({'message': 'No assets found.'}), 404
    return assets_schema.dump(assets)


# Get a specific asset by id
@asset.route("/<int:asset_id>", methods=["GET"])
def get_asset(asset_id):
    asset = Asset.query.get(asset_id)
    if not asset:
        return jsonify({'error': 'Asset not found'}), 404
    return asset_schema.dump(asset)

# Create a new asset
@asset.route("/", methods=["POST"])
def create_asset():
    data = request.json
    name = data.get('name')
    asset_type = data.get('asset_type')
    owner = data.get('owner')
    location = data.get('location')
    value = data.get('value')
    importance_rating = data.get('importance_rating')
    description = data.get('description')
    user_id = data.get('user_id')

    asset = Asset(
        name=name,
        asset_type=asset_type,
        owner=owner,
        location=location,
        value=value,
        importance_rating=importance_rating,
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
def update_asset(asset_id):
    try:
        asset = Asset.query.get_or_404(asset_id)
        data = request.json
        asset.name = data.get('name', asset.name)
        asset.asset_type = data.get('asset_type', asset.asset_type)
        asset.owner = data.get('owner', asset.owner)
        asset.location = data.get('location', asset.location)
        asset.value = data.get('value', asset.value)
        asset.importance_rating = data.get('importance_rating', asset.importance_rating)
        asset.description = data.get('description', asset.description)
        asset.user_id = data.get('user_id', asset.user_id)

        db.session.commit()

        response = {
            "message": "Asset successfully updated",
            "asset": asset_schema.dump(asset)
        }
        return jsonify(response), 200
    except:
        return jsonify({'message': 'Asset not found'}), 404


# Delete a specific asset by id
@asset.route("/<int:asset_id>", methods=["DELETE"])
def delete_asset(asset_id):
    try:
        asset = Asset.query.get_or_404(asset_id)
        db.session.delete(asset)
        db.session.commit()
        return jsonify({'message': 'Asset deleted successfully'}), 204
    except:
        return jsonify({'message': 'Asset not found'}), 404
