#!/bin/sh

coverage run --source='.' manage.py test --settings=settings.test
coverage html
