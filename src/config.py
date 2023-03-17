import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        db_url = os.environ.get("DATABASE_URL")

        if not db_url:
            raise ValueError("DATABASE_URL is not set")

        return db_url

    # JWT configuration to retrieve from the environment variable
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'coderacademy'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass


app_environment = os.environ.get("FLASK_DEBUG")

if app_environment:
    app_config = DevelopmentConfig()
else:
    app_config = ProductionConfig()
