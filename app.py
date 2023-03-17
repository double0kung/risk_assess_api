from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

# Global Instances
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Add config from object
    app.config.from_object("config.app_config")

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    # Import and register custom commands
    from commands.db import db_cmd
    app.register_blueprint(db_cmd)

    # Import and register controllers
    from controller import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app
