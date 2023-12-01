from datetime import datetime, timezone, timedelta


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
