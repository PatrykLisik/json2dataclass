FROM node

WORKDIR /usr/app

#RUN apt-get update || : && apt-get install python3-pip python -y
#COPY server server
#RUN pip install -r server/requirements.txt
#RUN sanic server.sanic_app.app --host 0.0.0.0 --port 5001 &

COPY client .
RUN npm install
RUN npm install -g serve
RUN NODE_OPTIONS=--openssl-legacy-provider npm run build

EXPOSE 5000

