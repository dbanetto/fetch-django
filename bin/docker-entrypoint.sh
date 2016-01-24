#!/bin/bash

# install bower components
python manage.py bower install

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
n=$?
tries=1
while [ $n -ne 0 ]; do
    sleep $((tries*tries))
    python manage.py migrate
    n=$?

    # break out of loop after 5 tries
    tries=$((tries+1))
    if [ $tries -gt 5 ]; then
        echo "Failed trying to migrate"
        exit 1
    fi
done

# Start server
echo "Starting server"
if [ "$DJANGO_SETTINGS_MODULE" = "settings.production" ]; then
    # todo: change to uwsgi
    python manage.py runserver 0.0.0.0:8000
else
    python manage.py runserver 0.0.0.0:8000
fi
