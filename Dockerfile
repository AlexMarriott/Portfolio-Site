FROM alpine
WORKDIR /
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 80
RUN apk update && apk add --update \
    python3

COPY . .
RUN pip3 install -r requirements.txt
CMD python3 app.py