from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://username:passwd!@127.0.0.1:5434/blog",
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"

    SECRET_KEY = "oiuweohfewbvkdsfkewrjrkwrnnqwertyasdfgsupersecret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class TestingConfig(Config):
    TESTING = False
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"
    SECRET_KEY = "prodoiuwfkewrjrkwrnrtyasdfgsupersecret"
