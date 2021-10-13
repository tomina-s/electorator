# Dockerfile relative to docker-compose.yml

FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /electorator
COPY ./electorator/requirements.txt /electorator/
RUN pip install -r requirements.txt
COPY . /electorator/