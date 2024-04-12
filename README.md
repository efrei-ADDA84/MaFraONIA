# DEVOPS_TP2 Project

This project encapsulates a Python application designed to fetch weather data using the OpenWeather API, packaged within a Docker container for easy deployment and scaling. It's a demonstration of integrating various DevOps practices and tools, including version control, containerization, and continuous integration/continuous deployment (CI/CD) workflows.

## Overview

The architecture leverages Python 3.8 as the programming language and Docker for containerization, ensuring the application runs consistently across different environments. The project includes essential configuration files such as `.gitignore` for Git, `Dockerfile` for Docker, and `weather_api_wrapper.py` for the application logic. Environment variables are used to configure the OpenWeather API key and the geographical coordinates for fetching weather data.

## Features

- Fetches weather data based on latitude and longitude from the OpenWeather API.
- Utilizes Docker for packaging and deploying the application, facilitating easy scalability and consistent execution across different environments.
- Employs environment variables for configuration, enhancing security and flexibility.

## Getting started

### Requirements

- Docker installed on your system.
- Python 3.8.
- An OpenWeather API key (specified as an environment variable).

### Quickstart

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Build the Docker image with the command: `docker build -t devops_tp2:latest .`
4. Run the Docker container: `docker run devops_tp2:latest`

## License

Copyright (c) 2024.