#!/bin/sh

coverage run --omit="settings/*","*/migrations/*","*/tests/*" --source='.' manage.py test --settings=settings.test
coverage html
