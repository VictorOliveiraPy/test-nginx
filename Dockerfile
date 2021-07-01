FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . /code
WORKDIR /code

COPY poetry.lock pyproject.toml /tmp/

RUN pip install poetry
RUN cd /tmp && poetry export -f requirements.txt --output /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


#RUN mkdir /code/static
RUN  adduser --disabled-password user
RUN mkdir -p /code/staticfiles


USER user

COPY . . 

# run gunicorn
#CMD gunicorn setup.wsgi:application --bind 0.0.0.0:8000
