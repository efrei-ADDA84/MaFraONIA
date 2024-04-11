const fetch = require('node-fetch');

const fetchWeatherByCityName = async (cityName) => {
  try {
    const apiKey = process.env.OPENWEATHER_API_KEY; // INPUT_REQUIRED {Your OpenWeather API key}
    const url = `http://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apiKey}`;
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Failed to fetch weather data');
    }
    const data = await response.json();
    console.log(`Weather data fetched for city: ${cityName}`);
    return {
      countryCode: data.sys.country,
      temperature: data.main.temp,
      cloudCover: data.clouds.all,
      humidity: data.main.humidity,
      pressure: data.main.pressure,
      windDirection: data.wind.deg,
      windSpeed: data.wind.speed,
    };
  } catch (error) {
    console.error(`Error fetching weather by city name: ${error.message}`, error);
    throw error;
  }
};

const fetchWeatherByCoordinates = async (latitude, longitude) => {
  try {
    const apiKey = process.env.OPENWEATHER_API_KEY; // INPUT_REQUIRED {Your OpenWeather API key}
    const url = `http://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${apiKey}`;
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Failed to fetch weather data');
    }
    const data = await response.json();
    console.log(`Weather data fetched for coordinates: ${latitude}, ${longitude}`);
    return {
      countryCode: data.sys.country,
      temperature: data.main.temp,
      cloudCover: data.clouds.all,
      humidity: data.main.humidity,
      pressure: data.main.pressure,
      windDirection: data.wind.deg,
      windSpeed: data.wind.speed,
    };
  } catch (error) {
    console.error(`Error fetching weather by coordinates: ${error.message}`, error);
    throw error;
  }
};

module.exports = {
  fetchWeatherByCityName,
  fetchWeatherByCoordinates,
};