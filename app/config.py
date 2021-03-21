import os
import string
import random


class BaseConfig():
    """base config"""
    SECRET_KEY = os.environ.get("secret_key", "".join(
        [random.choice(string.ascii_letters + string.digits) for n in range(16)]))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI", "postgresql://root:transferio@postgres/transferio")
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_USERNAME = os.environ.get("transferio_EMAIL")
    MAIL_PASSWORD = os.environ.get("transferio_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("transferio_EMAIL")


class TestingConfig(BaseConfig):
    """testing config"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """dev config"""
    DEBUG = True


class ProductionConfig(BaseConfig):
    """production config"""
