import os
import requests

# INPUT_REQUIRED {Please set your LATITUDE environment variable}
LATITUDE = os.getenv('LATITUDE')
# INPUT_REQUIRED {Please set your LONGITUDE environment variable}
LONGITUDE = os.getenv('LONGITUDE')
# INPUT_REQUIRED {Please set your OPENWEATHER_API_KEY environment variable}
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

def fetch_weather_data():
    if not LATITUDE or not LONGITUDE or not OPENWEATHER_API_KEY:
        print("Error: Environment variables LATITUDE, LONGITUDE, or OPENWEATHER_API_KEY are not set.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={OPENWEATHER_API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        weather_data = response.json()

        print("Weather data fetched successfully:")
        print(weather_data)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(http_err.response.text)
    except requests.exceptions.RequestException as err:
        print(f"Error fetching weather data: {err}")
        print(err)

if __name__ == "__main__":
    fetch_weather_data()