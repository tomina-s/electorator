# electorator
## Сервис доступен по адресу [huvalk.ru](https://huvalk.ru)
### Тестовый пользователь
#### Имя пользователя: huvalk
#### Пароль: 1234

### Требуется для запуска
- docker
- docker-compose
- make
- node
- npm
- pylint

### Запуск 
#### Переменные окружения

```
SECRET_KEY={secret_key}
POSTGRES_USER={postgres_user}
POSTGRES_PASSWORD={postgres_password}
POSTGRES_DB={database}
POSTGRES_HOST={host}
POSTGRES_PORT={port}
ENV=[dev|prod]
```

#### Из исходников
1. Создать файл с переменными окруежения electorator.env
в папке рядом с проектом
2. ```make build-local```
3. ```make build-local-front```
4. ```make start-local```
5. ```python3 manage.py migrate```
#### Из docker hub
1. Создать файл с переменными окруежения electorator.env
в папке рядом с проектом
2. ```make build-local-front```
3. ```make start-latest```
4. ```python3 manage.py migrate```