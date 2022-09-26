FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="${PATH}:/root/.poetry/bin"
EXPOSE 8000/tcp
RUN mkdir /app
WORKDIR /app/
# Установка пакетов python и зависимостей необходимых для их сборки
RUN apk add --no-cache --virtual \
    curl  \
    make gcc g++  \
    libjpeg-turbo-dev zlib libffi-dev cairo-dev libwebp-dev
COPY poetry.lock pyproject.toml /app/
RUN pip3 install poetry
RUN poetry install --no-interaction --no-ansi
COPY / /app/
