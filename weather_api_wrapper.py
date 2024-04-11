import os
import requests
import logging

# INPUT_REQUIRED {config_description}: Set your OpenWeather API key here
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', '73798258221c6dcc94a6b4283fb75734')
# INPUT_REQUIRED {config_description}: Set your default latitude here
LATITUDE = os.getenv('LATITUDE', '48.8534')
# INPUT_REQUIRED {config_description}: Set your default longitude here
LONGITUDE = os.getenv('LONGITUDE', '2.3488')

def fetch_weather_data():
    """
    Fetches weather data from the OpenWeather API using the provided latitude and longitude.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?lat={LATITUDE}&lon={LONGITUDE}&appid={OPENWEATHER_API_KEY}"
    
    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        weather_data = response.json()
        
        logging.info("Successfully fetched weather data.")
        return {
            "country_code": weather_data.get("sys", {}).get("country", "N/A"),
            "temperature": weather_data.get("main", {}).get("temp", "N/A"),
            "cloud_cover": weather_data.get("clouds", {}).get("all", "N/A"),
            "humidity": weather_data.get("main", {}).get("humidity", "N/A"),
            "pressure": weather_data.get("main", {}).get("pressure", "N/A"),
            "wind_direction": weather_data.get("wind", {}).get("deg", "N/A"),
            "wind_speed": weather_data.get("wind", {}).get("speed", "N/A"),
        }
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")

if __name__ == "__main__":
    weather_info = fetch_weather_data()
    if weather_info:
        print(weather_info)
    else:
        print("Failed to fetch weather data.")