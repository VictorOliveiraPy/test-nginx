FROM python:3.9.5
# install dependency manager
RUN pip install poetry
# create main application folder
WORKDIR /var/www
COPY . /var/www/
RUN poetry config virtualenvs.create false && poetry install
ENV PORT=8000
EXPOSE $PORT
ENTRYPOINT poetry run python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT