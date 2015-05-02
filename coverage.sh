#!/bin/sh

coverage run --omit='settings/*','*/migrations/*','*/tests/*','components/*' --source='.' manage.py test --settings=settings.test
coverage html
