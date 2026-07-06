from dotenv import load_dotenv
import os

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "dev-secret"

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "../instance/taskflow.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
