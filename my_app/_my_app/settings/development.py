
from .base import *
from _my_app.keys.development import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*2yg*z4j05$v&+l%e#n=*1f9%f*9481&bi21%d$hm#yt*h%r!k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_database',
        'USER': 'dbuser',
        'PASSWORD': 'dbpass',
        'HOST': 'localhost',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    }
}
'''

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
    'rest_framework_swagger',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# This IP addresses ensure debug toolbar shows development environment
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

'''
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'               #Add Gmail SMTP Settings or your SMTP Settings your mail provider for Sending Mail
EMAIL_PORT = 587                            #Add port of your email account
EMAIL_HOST_USER = 'user@gmail.com' #Add the account email
EMAIL_HOST_PASSWORD = 'pass'         #Add password the account email
'''
