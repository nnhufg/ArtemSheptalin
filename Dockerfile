# Создаем кастомный image для Django.
# Кастомный, так как нам надо перекинуть локальные файлы в образ.
# Для PostgreSQL мы возьмем готовый образ и соберем его сразу в docker-compose.yml.
# Docker-compose.yml файл, при помощи которого мы объединяем images и создаем полный сервис для Docker.

# копируем готовый образ python из dockerhub
FROM python:3.10.0-alpine

# установка необходимых пакетов для работы с MongoDB
RUN apk add --no-cache gcc musl-dev libffi-dev \
    && apk add --no-cache jpeg-dev zlib-dev \
    && apk add --no-cache bash \
    && apk add --no-cache mariadb-dev \
    && apk add --no-cache libpq

# устанавливаем рабочую директорию внутри docker контейнера
WORKDIR /website

# копируем файлы зависимостей и проекта Django в образ
COPY requirements.txt .

# устанавливаем зависимости для проекта, не кешируя их
RUN pip install -r requirements.txt --no-cache-dir

# устанавливаем порт, на котором будет работать Docker
EXPOSE 8000

# в рабочую директорию копируем папку с Django вне контейнера
COPY website .

# cобираем статику для Django
RUN python3 manage.py collectstatic --no-input

# запускаем через uwsgi
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD [ "uwsgi", "--ini", "/movies_admin/uwsgi.ini" ]