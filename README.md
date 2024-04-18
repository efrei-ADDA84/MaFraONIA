# DEVOPS_TP3

DEVOPS_TP3 is an automation project focused on streamlining DevOps tasks for an application using Docker, GitHub, and Azure. This project aims to automate environment configuration updates, Docker image management, container deployment, and continuous integration/deployment through GitHub Actions to Azure Container Instances (ACI), with a feature for monitoring API requests using Prometheus.

## Overview

The project utilizes a Python-based application with Flask for the web framework, Docker for containerization, GitHub for source control and CI/CD through GitHub Actions, and Azure ACIs for deployment. The system is designed to be robust and scalable, integrating Prometheus for monitoring, thereby ensuring a comprehensive DevOps solution.

## Features

- Automated environment configuration updates.
- Docker image creation and management.
- Automated container deployment to Azure Container Instances.
- Continuous Integration and Deployment with GitHub Actions.
- API request monitoring using Prometheus.

## Getting started

### Requirements

- Docker
- Python 3.8
- An OpenWeather API key
- Flask
- A GitHub account
- Access to Azure Container Registry (ACR) and Azure Container Instances (ACI)

### Quickstart

1. Clone the repository to your local machine.
2. Rename `.env.devopstp3` to `.env` and update `OPENWEATHER_API_KEY` with your key.
3. Build the Docker image using `docker build -t devops_tp3:latest .`
4. Run the container with `docker run -p 80:80 -p 8081:8081 -e OPENWEATHER_API_KEY=YOUR_API_KEY devops_tp3:latest`
5. Check the GitHub repository for CI/CD configurations and adjust as necessary for your environment.

## Deployment

The application is deployed to Azure Container Instances (ACI) through GitHub Actions. Upon a commit to the main branch, the CI/CD pipeline automatically builds the Docker image, pushes it to Azure Container Registry (ACR), and deploys it to ACI.

### Custom DNS Name

The application is accessible via a custom DNS name following the pattern `devops-20230583.westeurope.azurecontainer.io`. This DNS name is configured during the deployment process in GitHub Actions.

### Azure Resources

This deployment process requires the following Azure resources to be configured:
- Azure Container Registry (ACR) to store the Docker images.
- Azure Container Instance (ACI) for deploying and running the containerized application.
- An Azure Resource Group where ACI will be deployed.

Ensure these resources are created and configured correctly in your Azure account. The required secrets (`AZURE_CREDENTIALS`, `ACR_LOGIN_SERVER`, and `OPENWEATHER_API_KEY`) should be stored in the GitHub repository's Secrets for the CI/CD pipeline to function properly.

## Prometheus Monitoring

This application is configured to expose metrics that can be scraped by Prometheus at the `/metrics` endpoint. To access these metrics, navigate to `http://<host>:80/metrics`, where `<host>` is the host or IP address where the application is running.

### Interpreting Metrics

- `weather_requests_total`: This counter metric tracks the total number of requests made to the main API endpoint. Incremented each time the `/` endpoint is accessed to fetch weather data.

## License

Copyright (c) 2024.