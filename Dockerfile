FROM ubuntu
WORKDIR /
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 80
RUN apt-get update
RUN apt install python3 python3-pip -y
COPY . .
RUN pip3 install -r requirements.txt
CMD python3 app.py