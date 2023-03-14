from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "verified", "mobile_number", "post_code", "pets")

    pets = ma.List(ma.Nested("PetSchema", exclude=("user",)))

user_schema = UserSchema()
users_schema = UserSchema(many=True)