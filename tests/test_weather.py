import pytest
from src import create_app
import json


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


# @pytest.mark.skip(reason="Skip at to complete API functionality")
def test_get_weather(client):
    response = client.get("http://localhost:5000/api/weather?city=condoto&country=co")
    # validate response from the endpoint
    assert response.status_code == 200
    # load data from the response
    data = json.loads(response.get_data(as_text=True))
    assert "location_name" in data
    """
    TODO: Modify after complete endpoint functionality
        assert "country" in data
        assert data["city"] == "condoto"
        assert data["country"] == "co"
    """
