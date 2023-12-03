from flask_restful import Resource, reqparse
from .weather_helpers import get_weather_data

class Weather(Resource):
    def __init__(self):
        # parse query parameters from the request
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "city",
            type=str,
            required=True,
            help="City cannot be blank",
            location="args",
        )
        self.parser.add_argument(
            "country",
            type=str,
            required=True,
            help="Country must be 2 character long",
            choices=["co", "br", "us", "ar"],
            location="args",
        )

    def get(self):
        args = self.parser.parse_args()
        city = args["city"]
        country = args["country"]

        # validate city and country length
        if city and len(country) != 2:
            return {"error": "Country must be two characters long"}, 400

        weather_data = get_weather_data(city, country)
        # http-response
        return weather_data
