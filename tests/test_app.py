import unittest
import os
from unittest.mock import patch
from app import app
from dotenv import load_dotenv

load_dotenv()  

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fetch_weather_data_success(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('temperature', data)
        self.assertIn('country_code', data)
        self.assertIn('cloud_cover', data)
        self.assertIn('humidity', data)
        self.assertIn('pressure', data)
        self.assertIn('wind_direction', data)
        self.assertIn('wind_speed', data)
        print("Test for successful weather data fetch passed.")

    def test_fetch_weather_data_failure(self):
        response = self.app.get('/?lat=&lon=')
        self.assertEqual(response.status_code, 400)
        print("Test for weather data fetch failure due to missing parameters passed.")

    def test_environment_variables(self):
        api_key = os.getenv('OPENWEATHER_API_KEY')
        self.assertIsNotNone(api_key)
        self.assertNotEqual(api_key, 'INPUT_REQUIRED {Provide your OpenWeather API key as an environment variable}')
        self.assertEqual(os.getenv('LATITUDE', '48.8534'), '48.8534')
        self.assertEqual(os.getenv('LONGITUDE', '2.3488'), '2.3488')
        print("Environment variables test passed.")

if __name__ == '__main__':
    unittest.main()