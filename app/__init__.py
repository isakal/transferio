import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig
# blueprints
from app.errors.handlers import errors
from app.home.routes import home


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy()

app.register_blueprint(errors)
app.register_blueprint(home)


def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig if os.environ.get(
        "PRODUCTION").lower() == 'true' else DevelopmentConfig)

    db.init_app()

    from app.errors.handlers import errors
    from app.home.routes import home

    app.register_blueprint(errors)
    app.register_blueprint(home)

    return app
