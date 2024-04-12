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

The `git_commit_push.py` script simplifies the process of committing changes to your local repository and pushing them to GitHub. This automation script is particularly useful for streamlining your development workflow. Here's how to use it:

### How to Use the git_commit_push.py Script

1. **Prepare Your Changes**: Before running the script, make sure all your changes are ready and saved.

2. **Run the Script**: Open a terminal in your project's root directory and execute the script by running:
   ```
   python git_commit_push.py
   ```

3. **Enter Your Commit Message**: When prompted, enter a meaningful commit message that describes the changes you're making. Press Enter to continue.

4. **Confirm and Push**: The script will automatically stage your changes, commit them to your local repository with the message you provided, and then push the commit to the remote repository on GitHub.

5. **Verify**: To ensure your changes have been successfully pushed, visit your GitHub repository and check the recent commits.

This script requires that you have configured your Git credentials correctly on your system. If you encounter any authentication issues, please verify your Git setup.

### Troubleshooting

- **Authentication Issues**: If the script fails to push changes due to authentication problems, ensure your Git credentials are set up correctly.
- **Permission Denied**: Make sure `git_commit_push.py` has execution permissions. On Linux or macOS, you can set this by running:
  ```
  chmod +x git_commit_push.py
  ```
- **Missing Git Configuration**: The script assumes you have a remote named 'origin' pointing to your GitHub repository. If you haven't set this up, you can do so by running:
  ```
  git remote add origin https://github.com/yourusername/yourrepository.git
  ```

Remember, this script is a helpful tool to automate repetitive Git operations. It's not a substitute for understanding how Git works. Familiarize yourself with Git commands and use the script to make your workflow more efficient.

## License

Copyright (c) 2024.