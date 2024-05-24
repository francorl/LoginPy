from .base import *


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret_key('NAME'),
        'USER': get_secret_key('USER'),
        'PASSWORD': get_secret_key('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR.child('media')