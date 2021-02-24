import os
import string
import random


class BaseConfig():
    """base config"""
    SECRET_KEY = os.environ.get("secret_key", "".join(
        [random.choice(string.ascii_letters + string.digits) for n in range(16)]))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI", "postgres://root:transferio@postgres/transferio")


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
