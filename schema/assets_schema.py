from app import ma

class AssetSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "asset_type", "owner", "location", "value", "weight", "description", "user_id")


asset_schema = AssetSchema()
assets_schema = AssetSchema(many=True)