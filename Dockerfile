FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set default latitude and longitude values. These can be overridden at runtime.
ENV LATITUDE=48.8534
ENV LONGITUDE=2.3488

EXPOSE 80

CMD ["python", "./app.py"]