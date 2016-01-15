#!/bin/sh

( cd code && python manage.py test --settings=settings.test )
