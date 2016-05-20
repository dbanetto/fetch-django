#!/bin/bash

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
    chmod 755 -R $(find /static -type d)
    chmod 755 -R $(find /web-media -type d)

    chmod 644 -R $(find /static -type f)
    chmod 644 -R $(find /web-media -type f)

    chown 997:33 -R /web-media
    chown 997:33 -R /static

    if [ "$DJANGO_USE_GUNICORN" = "true" ]; then 
        gunicorn app.wsgi --bind=0.0.0.0:8000 --log-file -
    else
        uwsgi /code/settings/uwsgi.ini
    fi
else
    gunicorn app.wsgi --bind=0.0.0.0:8000 --log-file -
fi
