import pytest
from src import create_app
from datetime import datetime
from src.api.weather_helpers import get_wind_direction, timestamp_to_time, get_current_time,get_wind_speed_description


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


# Test endpoint funcionality
def test_get_weather(client):
    response = client.get("http://localhost:5000/api/weather?city=condoto&country=co")
    # validate response from the endpoint
    assert response.status_code == 200
    
# Test get_wind_direction function
def test_get_wind_direction():
    assert get_wind_direction(90) == "East"

# Test timestamp_to_time function
def test_timestamp_to_time():
    timestamp = 1701428240
    expected_result = "05:57:20"
    assert timestamp_to_time(timestamp) == expected_result

# Test get_wind_speed_description
def test_get_wind_speed_description():
    assert get_wind_speed_description(20) == "Gale"
