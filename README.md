# DEVOPS_TP2 Project

This project encapsulates a Python application designed to fetch weather data using the OpenWeather API, integrated with a Flask web framework, and packaged within a Docker container for easy deployment and scaling. It's a demonstration of integrating various DevOps practices and tools, including version control, containerization, and continuous integration/continuous deployment (CI/CD) workflows.

## Overview

The architecture leverages Python 3.8 and Flask as the web framework, with Docker for containerization, ensuring the application runs consistently across different environments. The project includes essential configuration files such as `.gitignore` for Git, `Dockerfile` for Docker, `weather_api_wrapper.py` for the core application logic, and `app.py` for the Flask application. Environment variables are used to configure the OpenWeather API key and the geographical coordinates for fetching weather data.

## Features

- Fetches weather data based on latitude and longitude from the OpenWeather API through a Flask web application.
- Utilizes Docker for packaging and deploying the application, facilitating easy scalability and consistent execution across different environments.
- Employs environment variables for configuration, enhancing security and flexibility.
- Includes a CI/CD pipeline setup with GitHub Actions for automated testing and Docker image publishing.

## Getting started

### Requirements

- Docker installed on your system.
- Python 3.8.
- An OpenWeather API key (specified as an environment variable).
- Flask for the web framework setup.

### Quickstart

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Build the Docker image with the command: `docker build -t devops_tp2:latest .`
4. Run the Docker container: `docker run --network host devops_tp2:latest`

## Automating Git Operations

To automate the process of committing changes and pushing them to the GitHub repository, you can use the `git_commit_push.py` script included in the project. Here's how to use it:

1. Open a terminal and navigate to the project directory.
2. Run the script with the command: `python git_commit_push.py`
3. When prompted, enter your commit message and press Enter.
4. The script will add all changes, commit them with your message, and push the commit to the remote repository.

Ensure you have configured your Git credentials correctly on your system to avoid any authentication issues during the push operation.

## License

Copyright (c) 2024.