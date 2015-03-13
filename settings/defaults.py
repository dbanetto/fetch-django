"""
Django settings for fetch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8sreml@*n3(_exglrwtbd%&$#)ax*ae51h4-yzrt0-c)kcn-dx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'select_multiple_field',
    'static_precompiler',
    'bootstrap3',

    'app',
    'fetch',
    'provider',
    'series',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'static_precompiler.finders.StaticPrecompilerFinder',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_TZ = True
TIME_ZONE = 'Pacific/Auckland'

USE_I18N = True

USE_L10N = True

# Used for sub-directories:
# add URL_ROOT to ROOT_URLCONF's urlpatterns
# Should end with a /
URL_ROOT = ''


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = 'static'
MEDIA_ROOT = 'media'

# Bootstrap
BOOTSTRAP3 = {
    'jquery_url': '/static/js/jquery.min.js',
    'base_url': '/static/bootstrap/',
    'css_url': '/static/bootstrap/less/bootstrap.css',
    'theme_url': None,
    'javascript_url': None,
    'javascript_in_head': False,
    'include_jquery': True,
    'horizontal_label_class': 'col-md-2',
    'horizontal_field_class': 'col-md-4',
    'set_required': True,
    'set_placeholder': False,
    'required_css_class': '',
    'error_css_class': 'has-error',
    'success_css_class': 'has-success',
    'formset_renderers': {
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}


# static_precompiler
STATIC_PRECOMPILER_COMPILERS = (
    'static_precompiler.compilers.CoffeeScript',
    'static_precompiler.compilers.LESS',
)

STATIC_PRECOMPILER_COMPILERS = (
    ('static_precompiler.compilers.CoffeeScript',
     {"executable": "/usr/bin/coffee"}),
    ('static_precompiler.compilers.LESS',
     {"executable": "/usr/bin/lessc"}),
)

STATIC_PRECOMPILER_OUTPUT_DIR = ""
STATIC_PRECOMPILER_PREPEND_STATIC_URL = True
