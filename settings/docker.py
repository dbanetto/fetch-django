from .defaults import *
import dj_database_url

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config()
    DEBUG = False
    TEMPLATES[0]['OPTIONS']['debug'] = False

if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['SECRET_KEY']

if 'FETCHER_URL' in os.environ:
    FETCHER_URL = os.environ['FETCHER_URL'].strip()
