### Requirements
> [Docker Desktop](https://docs.docker.com/)

>**Note**: You can use tools like: [Postman](https://www.postman.com/), and [curl](https://curl.se/) for test the response from the API or any case, use your own web browser, and pass the query parameters by hand. :)


## [Flask RESTful API challenge](https://www.globant.com/) 👽

This project contains a small API implementation that shows one of the many possible ways to implement a RESTful API using Flask and Flask-restful libraries.

**Main libraries used:**
0. [Flask framework](https://flask.palletsprojects.com/en/3.0.x/) - build light-way web apps.
1. [Flask Blueprints](https://flask.palletsprojects.com/en/3.0.x/blueprints/) - for build modular web apps.
2. [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/index.html) - restful API library.
3. [requests](https://pypi.org/project/requests/) - handle requests to external APIs.
4. [pytest](https://docs.pytest.org/en/7.4.x/) / [pytest-flask](https://pytest-flask.readthedocs.io/en/latest/) - Adds unit-test functionalities to the APIs.
5. [python-dotenv](https://pypi.org/project/python-dotenv/) - handle enviroments variables.



**Project structure:**
```
.
├── README.md
├── src
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── resources.py
│   │   └── weather_helpers.py
│   └── main.py      
├── tests
│   ├── __init__.py
│   ├── test_weather.py   
├── .gitignore
├── docker-compse.yml
├── Dockerfile 
├── requirements.txt
├── Pipfile
└── Pipfile.lock

```

* src/api 
    - `src/api/resources.py` holds the resource for define the unique API endpoint, and their internal logic. 
    - `src/api/weather_helpers.py` Where we define the helper functions to format comming from the external API.

* tests/ 
    - `src/test/test_weather.py` define test-suits for the endpoint
    - *TODO: 🛠️* 
        - we have a single unit-test, that was skiped on the last version of the API.
        - need to add more test unit-test cases on the entry

**Build**

1. `Clone repository`
2.  Set env variables : `cd root_directory & touch .env`
3.  Define env variables:
    ```
    OPENWEATHERMAP_API_KEY=1508a9a4840a5574c822d70ca2132032

    OPENWEATHERMAP_API_URL='https://api.openweathermap.org/data/2.5/weather'
    ```
3.  Build and Run : `docker-compose up --build`
- Note: Only required on the first build

**Running** 
4.  Run Docker container after build use: `docker-compose up weather`


### USAGE

### weather endpoint
[GET] http://127.0.0.1:5000/api/weather?city=istmina&country=co

RESPONSE
```json
{
    "location_name": "Istmina, CO",
    "temperature": "23.43 °C / -163.09 °F",
    "wind": "Light Air, 0.29 m/s, South-Southwest",
    "cloudiness": "moderate rain",
    "pressure": "1009 hpa",
    "humidity": "98%",
    "sunrise": "06:00:34",
    "sunset": "17:51:13",
    "geo_coordinates": "[5.16, -76.68]",
    "requested_time": "2023-12-01 09:01:37",
    "forecast": {}
}
```


## Geek resources:

Some interesting posts that teach how to make some of the calculations. That I implement to format the data coming from the external API.

- 💨 [Wind description by speed ](https://www.weather.gov/pqr/wind)

- 💨 [Wind directions](https://windy.app/blog/what-is-wind-direction.html)
- 💨 [Another Wind directions formula](https://www.ncl.ucar.edu/Document/Functions/Contributed/wind_direction.shtml#:~:text=Wind%20direction%20is%20measured%20in,the%20east%20is%2090%20degrees.)

- [Kelvin to Fahrenheit conversion](https://www.calculatorsoup.com/calculators/conversions/kelvin-to-fahrenheit.php)

- [Kelvin to Celsius conversion](https://www.rapidtables.com/convert/temperature/kelvin-to-celsius.html)

- [Linux timestamp conversion to UTC](https://www.epochconverter.com/)