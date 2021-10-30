FROM python:3.9-slim

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt


CMD ["sanic", "server.sanic_app.app", "--host", "0.0.0.0", "--port", "$PORT"]

