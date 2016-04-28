from dj_static import Cling, MediaCling
from django.core.wsgi import get_wsgi_application

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")

application = Cling(MediaCling(get_wsgi_application()))
