#!/bin/bash

# echo "Collect static files"
# python manage.py collectstatic --noinput

echo "Apply database migrations"
python my_app/manage.py migrate --noinput
python my_app/manage.py migrate users

echo "Load data"
python my_app/manage.py loaddata my_app/db.json

echo "Starting server"
python my_app/manage.py runserver 0.0.0.0:8000
