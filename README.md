# DEVOPS_TP3

DEVOPS_TP3 is an innovative project aimed at automating DevOps tasks through the integration of Docker, GitHub, and Azure technologies. It focuses on streamlining environment configurations, managing Docker images, deploying containers, and implementing continuous integration and deployment with GitHub Actions. Additionally, it monitors API requests using Prometheus, providing a comprehensive solution for application deployment and monitoring.

## Overview

The project utilizes a Python-based application, leveraging Flask for serving web requests, Docker for containerization, GitHub for source control and CI/CD workflows, and Azure Container Instances for deployment. Prometheus is integrated for real-time monitoring of API request metrics, enhancing observability.

## Features

- **Environment Configuration Update:** Ensures application environment configurations are up-to-date.
- **Docker Image Management:** Automates the building and updating of Docker images.
- **Automated Container Deployment:** Uses GitHub Actions for seamless container deployment to Azure Container Instances.
- **Continuous Integration and Deployment:** Streamlines development workflows with GitHub Actions.
- **API Request Monitoring:** Monitors and tracks API request metrics with Prometheus.

## Getting started

### Requirements

- Docker
- Python 3.8+
- Flask
- An OpenWeather API key
- GitHub account
- Azure Container Registry and Azure Container Instances access

### Quickstart

1. Clone the repository and navigate to the project directory.
2. Rename `.env.devopstp3` to `.env` and populate it with your OpenWeather API key.
3. Build the Docker image using `docker build -t devops_tp3:latest .`
4. Run the container with `docker run --network host -e OPENWEATHER_API_KEY=YOUR_API_KEY devops_tp3:latest`
5. Configure GitHub Actions to automate CI/CD workflows.

## License

Copyright (c) 2024.