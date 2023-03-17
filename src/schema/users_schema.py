from app import ma

class UserSchema(ma.Schema): # Define the fields to include in the schema
    class Meta:
        fields = ("user_id", "email", "first_name", "last_name", "password")


user_schema = UserSchema() # Create an instance of the UserSchema for a single user
users_schema = UserSchema(many=True) # Create an instance of the UserSchema for a collection of users