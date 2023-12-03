from flask import Blueprint
from flask_restful import Api
from .weather import Weather

# API blueprint
api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Routes
api.add_resource(Weather, "/weather")
