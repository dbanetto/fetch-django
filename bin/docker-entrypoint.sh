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

chown 997:33 -R /web-media
chown 997:33 -R /static
chown 997:33 -R /components
chmod 775 -R /code
chmod 775 -R /web-media
chmod 775 -R /static
chmod 775 -R /components

# Start server
echo "Starting server"
if [ "$DJANGO_SETTINGS_MODULE" = "settings.production" ]; then
    # todo: change to uwsgi
    uwsgi /code/settings/uwsgi.ini
else
    python manage.py runserver 0.0.0.0:8000
fi
