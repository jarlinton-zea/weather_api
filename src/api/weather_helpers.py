import json
from flask import Response
from datetime import datetime, timezone, timedelta
import requests
import os
from dotenv import load_dotenv


# load env variables
load_dotenv()

def format_wind(wind_data):
    """
    Format wind information.

    Args:
    - wind_data (dict): Wind data containing 'speed' and 'deg'.

    Returns:
    - str: Formatted wind information.
    """
    if "speed" in wind_data and "deg" in wind_data:
        speed = wind_data["speed"]
        deg = wind_data["deg"]
        wind_direction = get_wind_direction(deg)

        return f"{wind_direction}, {speed} m/s"
    else:
        return "Unknown"


def get_wind_direction(degrees):
    """
    Get wind direction based on degrees.

    Args:
    - degrees (float): Wind direction in degrees.

    Returns:
    - str: Wind direction as a cardinal direction (e.g., 'North', 'South', etc.).

    """
    directions = [
        "North",
        "North-Northeast",
        "Northeast",
        "East-Northeast",
        "East",
        "East-Southeast",
        "Southeast",
        "South-Southeast",
        "South",
        "South-Southwest",
        "Southwest",
        "West-Southwest",
        "West",
        "West-Northwest",
        "Northwest",
        "North-Northwest",
    ]

    index = round(degrees / 22.5) % 16
    return directions[index]


def get_wind_speed_description(wind_speed):
    """
    Get wind speed description based on degrees.

    Args:
    - wind_speed (float): Wind direction in degrees.

    Returns:
    - str: Wind description (e.g., 'Light Breeze', 'Near Gale', etc.).

    """
    wind_description = "Calm"
    # convert m/s to mph, 1 m/s = 2.24 mph, and round the next integer
    wind_speed_mph = round(wind_speed * 2.24)

    if wind_speed_mph in range(1, 4):
        wind_description = "Light Air"
    if wind_speed_mph in range(4, 8):
        wind_description = "Light Breeze"
    if wind_speed_mph in range(8, 13):
        wind_description = "Gentle Breeze"
    if wind_speed_mph in range(13, 19):
        wind_description = "Moderate Breeze"
    if wind_speed_mph in range(19, 25):
        wind_description = "Fresh Breeze"
    if wind_speed_mph in range(25, 32):
        wind_description = "Strong Breeze"
    if wind_speed_mph in range(32, 39):
        wind_description = "Near Gale"
    if wind_speed_mph in range(39, 47):
        wind_description = "Gale"
    if wind_speed_mph in range(47, 55):
        wind_description = "Strong Gale"
    if wind_speed_mph in range(55, 64):
        wind_description = "Whole Gale"
    if wind_speed_mph in range(64, 76):
        wind_description = "Storm Force"
    elif wind_speed_mph > 75:
        wind_description = "Hurricane Force"

    return wind_description


def timestamp_to_time(timestamp):
    """
    Format timestamp to a human-readable string.

    Args:
    - timestamp (int): Unix timestamp.

    Returns:
    - str: Formatted timestamp string.
    """

    sunrise_datetime_utc = datetime.utcfromtimestamp(timestamp).replace(
        tzinfo=timezone.utc
    )
    # Convert to 'America/New_York' timezone is equal to Colombia/Bogota
    sunrise_datetime_local = sunrise_datetime_utc.astimezone(
        timezone(timedelta(hours=-5))
    )

    # Format the datetime object as a 24-hour time string
    sunrise_24h_format = sunrise_datetime_local.strftime("%H:%M:%S")

    return sunrise_24h_format


def get_current_time():
    """
    Returns the current datetime in a human-readable string.

    Args:
    - None.

    Returns:
    - str: Formatted current datetime string.
    """
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_datetime


def get_weather_data(city, country):
    """
    Returns The incoming unformatted data from the external API call.

    Args:
    - city (str): city's name.
    - country (str): country's code, ex: CO, AR, BR, VZ

    Returns:
    - json : Weather data comming from an external APIs call.
    """
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
        formatted_weather_data = format_weather_data(response.json())
        # Return data from the external API
        return formatted_weather_data

def format_weather_data(weather_data):
    """
    Returns The weather data for city and country, initially requested to [GET: weather] endpoint.

    Args:
    - weather_data (dict): Incoming unformatted data from the external API call.
    

    Returns:
    - json : Formatted request weather data in human-readable format..
    """
    
    
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
