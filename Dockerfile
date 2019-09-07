FROM python:3.6

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y

RUN mkdir /my_app
COPY /my_app /my_app

WORKDIR /my_app
RUN pip install -r _requirements/development.txt

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Django service
EXPOSE 8000
