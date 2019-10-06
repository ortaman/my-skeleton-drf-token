
import datetime

from .base import *
from _my_app.keys.development import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*2yg*z4j05$v&+l%e#n=*1f9%f*9481&bi21%d$hm#yt*h%r!k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if os.getenv('DOCKER_CONTAINER'):
    POSTGRES_HOST = 'db'             # to run with docker
else:
    POSTGRES_HOST = '127.0.0.1'      # to debug using pycharm

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'dbuser',
        'PASSWORD': 'dbpass',
        'HOST': POSTGRES_HOST,            # name the docker service
        'PORT': '5432',
        'CONN_MAX_AGE': 600,
    }
}

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
    'drf_yasg',
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


SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'Token',
    'JWT_AUTH_COOKIE': None,

}

###   django-cors-headers   ###
INSTALLED_APPS += [
    'corsheaders'
]

MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)