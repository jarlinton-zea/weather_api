from flask import Flask
from src.api import api_bp


def create_app():
    """_summary_

    Returns:
        _type_: _description_
    """
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix="/api")
    return app
