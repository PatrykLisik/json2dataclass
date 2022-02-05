FROM python:3.9-slim

WORKDIR /app

COPY . /app
ENV FLASK_APP=json2dataclass:app
RUN pip install -r requirements.txt