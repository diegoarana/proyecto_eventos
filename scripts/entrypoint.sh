#!/bin/bash

if [[ -z "${DJANGO_TEST}" ]]; then
  python /scripts/wait_for_postgres.py
  python manage.py collectstatic --noinput
  python manage.py makemigrations 
  python manage.py migrate
  python manage.py runserver 0.0.0.0:8080
else
  coverage run --source='.' manage.py test app.test
  coverage report --fail-under=80
fi
