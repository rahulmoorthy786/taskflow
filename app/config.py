import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-secret-key")

    SQLALCHEMY_DATABASE_URI = "sqlite:///taskflow.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
