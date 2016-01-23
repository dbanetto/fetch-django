#!/bin/bash

# prevent postgres race
nc -z db 5432
n=$?
while [ $n -ne 0 ]; do
    sleep 1
    nc -z db 5432
    n=$?
done

# Collect static files
echo "Collect static files"
python /code/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python /code/manage.py migrate

# Start server
echo "Starting server"
if [ "$DJANGO_SETTINGS_MODULE" = "settings.production"]; then
    # todo: change to uwsgi
    python /code/manage.py runserver 0.0.0.0:8000
else
    python /code/manage.py runserver 0.0.0.0:8000
fi
