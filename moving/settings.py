import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6p0z2a-rm1fmxb(8hh_5f!1qt)z2jh1$&q&&%6572rr)ils^yc'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'information'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'moving.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'moving.wsgi.application'

if 'DJANGO_DB_USERNAME' in os.environ:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME'    : os.environ['DJANGO_DB_NAME'],
        'USER'    : os.environ['DJANGO_DB_USERNAME'],
        'PASSWORD': os.environ['DJANGO_DB_PASSWORD'],
        'HOST'    : os.environ['DJANGO_DB_HOST'],
        'PORT'    : os.environ['DJANGO_DB_PORT']
    }}
elif 'MYSQL_DATABASE' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ["DB_NAME"],
            'USER': os.environ["DB_USER"],
            'PASSWORD': os.environ["DB_PASSWORD"],
            'HOST': os.environ["DB_HOST"],
            'PORT': os.environ["DB_PORT"],
            'TEST': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'test.db',
            }
        }
    }
else:   
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moving',
        'USER': 'root',
        'PASSWORD': 'shadow5424!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
     }
 }

 
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#REMOVE_APPEND_SLASH_WARNING
APPEND_SLASH = False

##CORS
CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',

)