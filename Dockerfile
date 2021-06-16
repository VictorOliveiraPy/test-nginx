FROM python:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /application
COPY . /application

RUN pip install poetry
RUN poetry config virtualenvs.create false 
RUN poetry install

