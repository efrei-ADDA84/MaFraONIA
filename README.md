# DEVOPS_TP3

DEVOPS_TP3 is an innovative project designed to automate DevOps tasks for applications through a seamless integration of Docker, GitHub, and Azure technologies. It focuses on simplifying environment configurations, Docker image management, container deployment, and implementing continuous integration and deployment pipelines. Additionally, it incorporates Prometheus for monitoring API requests, providing a comprehensive solution for application deployment and monitoring.

## Overview

The project is built on a Python-based application framework, utilizing Flask for serving web requests. Docker is used for creating lightweight, portable container images, allowing for consistent deployment experiences across different environments. GitHub Actions facilitate automated workflows for continuous integration and deployment (CI/CD), pushing Docker images to Azure Container Registry, and deploying containers to Azure Container Instances (ACI) for scalable and managed application hosting. Prometheus integration offers real-time monitoring capabilities, enhancing the observability of the application.

## Features

- **Environment Configuration Update:** Streamlines the process of updating application environments to match development progress.
- **Docker Image Management:** Automates the creation and updating of Docker images for consistent and reliable deployments.
- **Automated Container Deployment:** Utilizes GitHub Actions for deploying Docker containers to Azure Container Instances, simplifying deployment processes.
- **Continuous Integration and Deployment:** Implements CI/CD pipelines through GitHub Actions, enhancing development efficiency and reliability.
- **API Request Monitoring:** Incorporates Prometheus for tracking and monitoring API request metrics, providing insights into application usage.

## Getting started

### Requirements

- Docker
- Python 3.8 or higher
- Flask
- An OpenWeather API key
- A GitHub account
- Access to Azure Container Registry (ACR) and Azure Container Instances (ACI)

### Quickstart

1. Clone the repository to your local development environment.
2. Rename the `.env.devopstp3` file to `.env` and include your OpenWeather API key.
3. Build the Docker image with the command `docker build -t devops_tp3:latest .`
4. Run the Docker container using `docker run --network host -e OPENWEATHER_API_KEY=YOUR_API_KEY devops_tp3:latest`
5. Follow the GitHub Actions workflow to deploy the application to Azure Container Instances.

## License

Copyright (c) 2024.