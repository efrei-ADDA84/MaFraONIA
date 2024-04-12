# DEVOPS_TP2 Project

This project, DEVOPS_TP2, is a comprehensive solution designed to fetch and display weather data using the OpenWeather API. It encapsulates a Python application, leveraging Flask for the web framework, and is containerized with Docker for ease of deployment and consistency across different environments.

## Overview

The project utilizes Python 3.8 and Flask as its core technologies, with Docker for containerization. The application structure includes a `.gitignore` file for version control, a `Dockerfile` for Docker configurations, `weather_api_wrapper.py` for interfacing with the OpenWeather API, and `app.py` for the Flask web application. Configuration is managed through environment variables, allowing for flexible deployment options.

## Features

- Fetches weather data based on latitude and longitude from the OpenWeather API.
- Flask web application for easy interface and accessibility.
- Docker containerization for consistent deployment and scalability.
- Utilizes environment variables for secure and flexible configuration.
- Automated CI/CD pipeline with GitHub Actions for streamlined development and deployment.

## Getting started

### Requirements

- Docker
- Python 3.8
- An OpenWeather API key
- Flask

### Quickstart

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Build the Docker image: `docker build -t devops_tp2:latest .`
4. Run the Docker container: `docker run --network host devops_tp2:latest`

## License

Copyright (c) 2024.