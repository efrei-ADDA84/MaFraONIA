import unittest
import os
from app import app

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
        self.assertTrue(os.getenv('OPENWEATHER_API_KEY'), "Environment variable for API key is not set.")
        self.assertTrue(os.getenv('LATITUDE'), "Environment variable for latitude is not set.")
        self.assertTrue(os.getenv('LONGITUDE'), "Environment variable for longitude is not set.")
        print("Environment variables test passed.")

if __name__ == '__main__':
    unittest.main()