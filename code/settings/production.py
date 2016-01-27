import os

from .defaults import *

DEBUG = False
TEMPLATE_DEBUG = False

URL_ROOT = os.environ['DJANGO_FETCH_URL_ROOT']
SECRET_KEY = os.environ['DJANGO_FETCH_SECRET_KEY']

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DJANGO_FETCH_POSTGRES_DB_NAME'],
        'USER': os.environ['DJANGO_FETCH_POSTGRES_USER'],
        'PASSWORD': os.environ['DJANGO_FETCH_POSTGRES_PASS'],
        'HOST': os.environ['DJANGO_FETCH_POSTGRES_HOST'],
        'PORT': os.environ['DJANGO_FETCH_POSTGRES_PORT'],
    }
}

STATIC_ROOT = os.environ['DJANGO_FETCH_STATIC_ROOT']
BOWER_COMPONENTS_ROOT = os.environ['DJANGO_FETCH_BOWER_COMPONENTS_ROOT']
MEDIA_ROOT = os.environ['DJANGO_FETCH_MEDIA_ROOT']
FETCHER_URL = os.environ['DJANGO_FETCHER_URL']
