from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "email", "first_name", "last_name", "password")


user_schema = UserSchema()
users_schema = UserSchema(many=True)