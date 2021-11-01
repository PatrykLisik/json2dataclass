FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000:8000
CMD ["python", "./server/sanic_app.py"]