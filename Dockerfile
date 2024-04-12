FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV LATITUDE=48.8534 

ENV LONGITUDE=2.3488 

EXPOSE 8081

CMD ["python", "./app.py"]