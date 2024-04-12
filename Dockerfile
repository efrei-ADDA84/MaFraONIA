FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# INPUT_REQUIRED {Provide your OpenWeather API key here}
ENV OPENWEATHER_API_KEY=73798258221c6dcc94a6b4283fb75734
# INPUT_REQUIRED {Set your desired latitude here}
ENV LATITUDE=48.8534 
# INPUT_REQUIRED {Set your desired longitude here}
ENV LONGITUDE=2.3488 

EXPOSE 8081

CMD ["python", "./app.py"]