FROM python:3.7.2-stretch

WORKDIR /app

ADD . /app

EXPOSE 5000 

RUN pip install -r requirements.txt && flask initdb

CMD flask run --host 0.0.0.0
