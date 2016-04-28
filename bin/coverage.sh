#!/bin/sh


coverage run --omit='settings/*','*/migrations/*','*/tests/*','components/*','*/wsgi.py' --source='.' manage.py test --settings=settings.test
# coverage html
