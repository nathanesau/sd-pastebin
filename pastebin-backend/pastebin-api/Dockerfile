FROM python:3.6-alpine

RUN apk update && apk add libpq
RUN apk add python3-dev
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
#COPY migrations migrations
COPY pastebin-api.py ./
COPY boot.sh ./
# COPY config.py ./

RUN chmod +x boot.sh

ENV FLASK_APP pastebin-api.py

#RUN chown -R pastebin-api:pastebin-api ./
#USER pastebin-api

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]