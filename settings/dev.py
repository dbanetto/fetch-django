from .defaults import *

URL_ROOT = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.sqlite3'),
    }
}
