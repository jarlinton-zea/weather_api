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
            # format the weather data
            formatted_weather_data = self.format_weather_data(response.json())
            # Return data from the external API
            return formatted_weather_data

    def format_weather_data(self, weather_data):
        # import helper functions, only when needed
        import json
        from flask import jsonify, Response
        from .weather_helpers import (
            get_wind_direction,
            get_wind_speed_description,
            timestamp_to_time,
            get_current_time,
        )

        # Format data from the external API
        location_name = f"{weather_data['name']}, {weather_data['sys']['country']}"
        temperature = f"{weather_data['main']['temp'] - 273.15:.2f} °C / {weather_data['main']['temp'] - 459.67:.2f} °F"

        wind_speed = f"{get_wind_speed_description(weather_data['wind']['speed'])}, {weather_data['wind']['speed']} m/s, {get_wind_direction(weather_data['wind']['deg'])}"

        cloudiness = weather_data["weather"][0]["description"]
        pressure = f"{weather_data['main']['pressure']} hpa"
        humidity = f"{weather_data['main']['humidity']}%"

        sunrise = timestamp_to_time(weather_data["sys"]["sunrise"])
        sunset = timestamp_to_time(weather_data["sys"]["sunset"])

        geo_coordinates = (
            f"[{weather_data['coord']['lat']:.2f}, {weather_data['coord']['lon']:.2f}]"
        )

        requested_time = get_current_time()

        formatted_data = {
            "location_name": location_name,
            "temperature": temperature,
            "wind": wind_speed,
            "cloudiness": cloudiness,
            "pressure": pressure,
            "humidity": humidity,
            "sunrise": sunrise,
            "sunset": sunset,
            "geo_coordinates": geo_coordinates,
            "requested_time": requested_time,
            "forecast": {},
        }

        response_data = json.dumps(formatted_data, ensure_ascii=False)

        response_with_headers = Response(
            response=response_data,
            status=200,
            content_type="application/json",
        )

        return response_with_headers
