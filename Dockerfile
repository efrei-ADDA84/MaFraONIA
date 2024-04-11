# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir requests

# Use environment variables for configuration
ENV OPENWEATHER_API_KEY=73798258221c6dcc94a6b4283fb75734

# Run weather_api_wrapper.py when the container launches
CMD ["python", "./weather_api_wrapper.py"]