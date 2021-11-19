# Dockerfile relative to docker-compose.yml

FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /electorator
COPY . /electorator/
RUN pip install -r ./electorator/requirements.txt
RUN cat ./config/cron/crontab >> /etc/crontab