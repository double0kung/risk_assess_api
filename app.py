from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Global Intances

db = SQLAlchemy()
ma = Marshmallow()


def create_app(): # Having a function allows for better separation of concerns between the application initialization and the application logic
    app = Flask(__name__)

    # add config from object
    app.config.from_object("config.app_config")

    db.init_app(app)
    ma.init_app(app)

    from commands.db import db_cmd
    app.register_blueprint(db_cmd)

    from controller import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    return app
