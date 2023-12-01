from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# https://api.openweathermap.org/data/2.5/weather?q={city name},{country code}&appid={API key}


@app.route("/weather", methods=["GET"])
def get_weather():
    # get query parameters
    city = request.args.get("city").capitalize()
    country = request.args.get("country").capitalize()

    return jsonify({"location_name": f"{city}, {country}"})


# Run the app in debug mode.
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
