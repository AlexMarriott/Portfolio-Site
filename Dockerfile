FROM ubuntu
WORKDIR /
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 80
ENV GITHUB_TOKEN 98c7afea9e1241929c2b49d2adf741d99cc96d80
ENV MONGO_INITDB_ROOT_PASSWORD VQeUuc9NmneULQEGdPcEckhg
RUN apt update && apt install -y python3 python3-pip

COPY . .
RUN pip3 install -r requirements.txt
CMD python3 app.py