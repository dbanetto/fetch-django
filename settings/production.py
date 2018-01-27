import os
import dj_database_url

from .defaults import *

DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = False

URL_ROOT = os.environ['URL_ROOT']
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_DB_NAME'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASS'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ['POSTGRES_PORT'],
    }
}

if 'DATABASE_URL' in os.environ:
    DATABASE['default'] = dj_database_url.config()

STATIC_ROOT = os.environ['STATIC_ROOT']
MEDIA_ROOT = os.environ['MEDIA_ROOT']
FETCHER_URL = os.environ['FETCHER_URL']
