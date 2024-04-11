<<<<<<< HEAD
# DEVOPS_TP2 Project

This project is designed to demonstrate a practical application of DevOps practices by deploying a Python-based weather API wrapper inside a Docker container. The application fetches weather data using the OpenWeather API, leveraging environment variables for configuration and is accessible via HTTP requests.

## Overview

The application is built on Python 3.8 and packaged with Docker to ensure a consistent, isolated environment for deployment. The project structure includes a `.gitignore` file to exclude unnecessary files from version control, a `Dockerfile` for container configuration, a `README.md` for documentation, an `app.py` script that serves as the application's core, and a `weather_api_wrapper.py` script for fetching weather data.

## Features

- Fetch weather data for a specific location using the OpenWeather API.
- Dockerized application for easy deployment and scalability.
- Environment variable-based configuration.
- Accessible via HTTP requests with Flask.

## Getting started

### Requirements

- Docker
- Python 3
- An OpenWeather API key `73798258221c6dcc94a6b4283fb75734`

### Quickstart

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Build the Docker image with `docker build -t devops_tp2:latest .`
4. Run the application with `docker run -p 5000:5000 devops_tp2:latest`
5. Access the application via `http://localhost:5000/weather` to fetch weather data.

## Using the API

To fetch weather data, send a GET request to `/weather`. The response will include details such as country code, temperature, cloud cover, humidity, pressure, wind direction, and wind speed.

Example request:
```
GET http://localhost:5000/weather
```

Example response:
```json
{
  "country_code": "FR",
  "temperature": "285.15",
  "cloud_cover": "90",
  "humidity": "77",
  "pressure": "1013",
  "wind_direction": "220",
  "wind_speed": "3.6"
}
```

## CI/CD with GitHub Actions

This project uses GitHub Actions for continuous integration and deployment. On every push to the main branch, the CI/CD pipeline runs unit tests, builds the Docker image, and publishes it to Docker Hub using GitHub secrets for Docker Hub credentials.

## Automatic Publishing to Docker Hub

The GitHub Actions workflow includes steps to automatically publish the Docker image to Docker Hub on every successful push to the main branch. The image is tagged with `latest` and the commit SHA.

## Running Tests Locally

To run tests locally, navigate to the project directory and execute:
```
python -m unittest
```

Ensure you have all dependencies installed by running `pip install -r requirements.txt`.

### License

Copyright (c) 2024.
=======
# DEVOPS_TP1 Project

## 1. Construction de l'image Docker
Pour conteneuriser l'application Python, j'ai suivi ces étapes suivnates :

1. Je m'assure que Docker est installé sur mon système.
2. Je vais au répertoire racine du projet.
3. Je construis l'image Docker avec la commande suivante :
```
docker build -t devops_tp1:latest .
```

## 2. Exécution de l'image Docker
Après avoir construit l'image, je peux exécuter l'application à l'aide de Docker avec la commande suivante :
```
docker run devops_tp1:latest
```

## 3. Publication sur DockerHub
Pour partager mon image Docker, je suis ces étapes :
1. Je me connecte à DockerHub à partir de la ligne de commande :
```
docker login
```
2. J'étiquette mon image Docker pour correspondre au nom de mon référentiel DockerHub :
```
docker tag devops_tp1:latest mafraonia/devops_tp1:latest  

```
3. Je pousse l'image Docker vers DockerHub :
```
docker push mafraonia/devops_tp1:latest  

```

## 4. Disponibilité sur GitHub
Pour partager mon code, je peux le pousser vers un dépôt GitHub :
1. J'initialise un dépôt Git dans le répertoire du projet :
```
git init
```
2. J'ajoute mes fichiers au dépôt :
```
git add .
```
3. Je valide les modifications :
```
git commit -m "Commit initial avec wrapper Python, Dockerfile et .gitignore"

```
4. Je crée un dépôt sur GitHub et je pousse mon code :
```
git remote add origin https://github.com/efrei-ADDA84/MaFraONIA  

git push -u origin master

```

## Dépendances
- Python 3
- La bibliothèque `requests` pour effectuer des requêtes API. Je l'installe avec `pip install requests`.
- Docker pour la conteneurisation.

>>>>>>> 467485d7cf7f1622c14cd8016ee40ef410e41c5f
