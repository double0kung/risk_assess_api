from flask import Flask


def create_app(): # Having a function allows for better separation of concerns between the application initialization and the application logic
    app = Flask(__name__)

    # add config from object
    app.config.from_object("config.app_config")

    @app.get("/")
    def hello_world():
        return {"message":"Hi, I'm not learning anything"}
    
    return app
