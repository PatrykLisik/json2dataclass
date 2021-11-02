FROM node:17
#RUN apt-get update || : && apt-get install python3-pip python -y
WORKDIR /usr/app
#COPY server server
COPY json2dataclass_client .
#RUN pip install -r server/requirements.txt
RUN npm install
#RUN sanic server.sanic_app.app --host 0.0.0.0 --port 5001 &
EXPOSE 5000


