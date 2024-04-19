import os
import requests
import logging
from prometheus_client import start_http_server, Counter

try:
    from flask import Flask, jsonify, request
    from dotenv import load_dotenv
except ImportError as e:
    logging.basicConfig(level=logging.ERROR)
    logging.error("Failed to import Flask or dotenv. Please ensure they are installed and compatible with Python 3.12.")
    logging.error("Error details: %s", e)
    raise

load_dotenv('.env.devopstp3')

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')  

if not OPENWEATHER_API_KEY:
    logging.error("No OpenWeather API key found. Please set the OPENWEATHER_API_KEY environment variable.")
    raise ValueError("No OpenWeather API key found. Please set the OPENWEATHER_API_KEY environment variable.")

# Prometheus metrics setup
REQUESTS = Counter('weather_requests_total', 'Total web requests for weather data')

@app.route('/', methods=['GET'])
def fetch_weather_data():
    REQUESTS.inc()  # Increment the counter
    latitude = request.args.get('lat', default='48.8534')  
    longitude = request.args.get('lon', default='2.3488')

    if not latitude or not longitude:
        logging.error("Latitude or longitude not provided")
        return jsonify({"error": "Latitude and longitude are required query parameters"}), 400

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?lat={latitude}&lon={longitude}&appid={OPENWEATHER_API_KEY}"
    
    logging.info(f"Fetching weather data with URL: {complete_url} and API Key: {OPENWEATHER_API_KEY}")  # Log the request URL and API key

    try:
        response = requests.get(complete_url)
        response.raise_for_status()  
        weather_data = response.json()
        
        logging.info("Successfully fetched weather data for lat: %s, lon: %s", latitude, longitude)
        return jsonify({
            "country_code": weather_data.get("sys", {}).get("country", "N/A"),
            "temperature": weather_data.get("main", {}).get("temp", "N/A"),
            "cloud_cover": weather_data.get("clouds", {}).get("all", "N/A"),
            "humidity": weather_data.get("main", {}).get("humidity", "N/A"),
            "pressure": weather_data.get("main", {}).get("pressure", "N/A"),
            "wind_direction": weather_data.get("wind", {}).get("deg", "N/A"),
            "wind_speed": weather_data.get("wind", {}).get("speed", "N/A"),
        })
    except requests.exceptions.HTTPError as http_err:
        logging.error("HTTP error occurred: %s", http_err, exc_info=True)
        return jsonify({"error": "Failed to fetch weather data"}), 500
    except Exception as err:
        logging.error("An error occurred: %s", err, exc_info=True)
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == "__main__":
    start_http_server(8080)
    app.run(host='0.0.0.0', port=80, debug=True)