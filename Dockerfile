# FROM python:3.11-slim-buster
FROM tiangolo/uvicorn-gunicorn:python3.11-slim

COPY ./app /app/app

COPY ./migration /app/migration

COPY ./alembic.ini /app/alembic.ini

COPY ./start.sh /app/start.sh

COPY ./requirements.txt /app/requirements.txt

EXPOSE 5432

RUN pip install -r requirements.txt

RUN chmod +x start.sh

ENTRYPOINT [ "/bin/sh", "/app/start.sh" ]
