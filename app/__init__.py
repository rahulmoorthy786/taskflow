from flask import Flask
from flask_migrate import Migrate

from .config import Config
from .models import db

# Initialize Flask-Migrate
migrate = Migrate()


def create_app(test_config=None):
    """
    Application Factory

    Args:
        test_config (dict, optional):
            Configuration overrides used during testing.
    """

    app = Flask(__name__)

    # Load default configuration
    app.config.from_object(Config)

    # Override configuration when running tests
    if test_config:
        app.config.update(test_config)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Initialize Flask-Migrate
    migrate.init_app(app, db)

    # Register Blueprints
    from .routes import main

    app.register_blueprint(main)

    return app