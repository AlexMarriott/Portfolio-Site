FROM ubuntu:20.04
WORKDIR /

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 80
ENV GITHUB_TOKEN $BUILD_GITHUB_TOKEN
ENV MONGO_INITDB_ROOT_PASSWORD $MONGO_INITDB_ROOT_PASSWORD

RUN apt update && apt install -y python3 python3-pip

COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py"]