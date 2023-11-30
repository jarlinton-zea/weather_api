from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for test demostration
sample_data = {
    "message": "This is a test API!",
    "query_params": {"city": "Quibdo", "country": "Colombia"},
}


# Define a route for the root endpoint
@app.route("/")
def hello():
    return jsonify(sample_data)


# Run the app in debug mode.
if __name__ == "__main__":
    app.run(debug=True)
