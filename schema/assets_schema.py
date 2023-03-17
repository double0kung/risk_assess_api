from app import ma

class AssetSchema(ma.Schema):
    class Meta:
        fields = ("asset_id", "name", "asset_type", "owner", "location", "value", "description", "user_id")

asset_schema = AssetSchema()
assets_schema = AssetSchema(many=True)
