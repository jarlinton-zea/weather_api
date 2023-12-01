import requests
from flask_restful import Resource, reqparse
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()


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

        # TODO: Add logic to request data from external endpoint
        weather_data = self.get_weather_data(city, country)
        # http-response
        return weather_data

    def get_weather_data(self, city, country):
        try:
            OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
            OPENWEATHERMAP_API_URL = os.getenv("OPENWEATHERMAP_API_URL")

            # Set the external api-url
            api_url = f"{OPENWEATHERMAP_API_URL}?q={city},{country}&appid={OPENWEATHERMAP_API_KEY}"
            # Set a timeout for the request to the external API
            response = requests.get(api_url, timeout=(5, None))
            # Raise an exception for 4xx and 5xx HTTP status codes
            response.raise_for_status()

        except requests.exceptions.Timeout as t_out:
            raise SystemExit(t_out)
        except requests.exceptions.TooManyRedirects as too_m:
            raise SystemExit(too_m)
        except requests.exceptions.HTTPError as http_e:
            raise SystemExit(http_e)
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)
        else:
            # Return data from the external API
            return response.json()
