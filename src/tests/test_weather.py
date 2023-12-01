from flask import Flask


def test_get_weather():
    # Test to validate the GET - weather endpoint
    app = Flask(__name__)
    app.config["TESTING"] = True
    client = app.test_client()

    # validate response from the endpoint
    response = client.get("localhost:5000/weather?city=Quibdo&country=CO")
    assert response.status_code == 200
