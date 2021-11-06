# Dockerfile relative to docker-compose.yml

FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /electorator
COPY ./electorator/requirements.txt /electorator/
COPY ./docs/Tik_table.sql /electorator/
RUN pip install -r requirements.txt
RUN cat Tik_table.sql >> /etc/crontab
COPY . /electorator/