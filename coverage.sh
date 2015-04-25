#!/bin/sh

coverage run --omit="settings/*","*/migrations/*" --source='.' manage.py test --settings=settings.test
coverage html
