from .defaults import *

STATIC_ROOT = '/static'
MEDIA_ROOT = '/web-media'
BOWER_COMPONENTS_ROOT = '/components/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
