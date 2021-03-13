import os
import googlemaps
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy()

gmaps = googlemaps.Client(key=os.environ.get("GOOGLE_API_KEY"))

from app.errors.handlers import errors
from app.home.routes import home

app.register_blueprint(errors)
app.register_blueprint(home)


def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig if os.environ.get(
        "PRODUCTION", "false").lower() == 'true' else DevelopmentConfig)

    db.init_app(app)

    from app.errors.handlers import errors
    from app.home.routes import home

    app.register_blueprint(errors)
    app.register_blueprint(home)

    return app
