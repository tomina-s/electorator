run:
	python3 electorator/manage.py runserver

build-local:
	docker build -t huvalk/electorator:local -f docker/electorator.Dockerfile .

start-latest:
	ENV=dev REPO=huvalk TAG=latest docker-compose up

start-local:
	ENV=dev REPO=huvalk TAG=local docker-compose up

start-local-db:
	ENV=dev REPO=huvalk TAG=local docker-compose -f docker-compose.db.yml up -d

