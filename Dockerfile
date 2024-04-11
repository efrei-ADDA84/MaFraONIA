# Use Python 3.8-slim as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy requirements file first to leverage Docker cache
COPY requirements.txt ./

# Install Flask and requests libraries without caching to minimize the image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Set environment variables
ENV OPENWEATHER_API_KEY=73798258221c6dcc94a6b4283fb75734
ENV LATITUDE=48.8534
ENV LONGITUDE=2.3488

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]