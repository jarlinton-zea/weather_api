from flask import Flask
from src.api import api_bp


def create_app():
    """
    Returns:
        main app
    """
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix="/api")
    return app
