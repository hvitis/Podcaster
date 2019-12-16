"""
Django settings for podcasts project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
import django_heroku
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_FOLDER = os.path.dirname(BASE_DIR + '/podcasts/')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
try:
    if(os.environ['ENV'] == "prod"):
        DEBUG = False
        print("Using PRODUCTION configuration.")
    else:
        DEBUG = True
        print("Using DEBUG configuration.")
except:
    DEBUG = True
    print("Using DEBUG configuration.")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'about',
    'blog',
    'contact',
    'episodes',
    'home',
    'newsletter',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Middleware for heroku
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

###################### 
# General Settings:  #
######################

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']

# How to generate your own key:
# python manage.py shell 
#  >>> from django.core.management.utils import get_random_secret_key
#  >>> get_random_secret_key()
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']


if DEBUG:
    SECURE_SSL_REDIRECT = False
    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


if not DEBUG:
    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
    
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_HOST = os.environ['DB_HOST']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            # Database name
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASS,
            'HOST': DB_HOST,  # Or an IP Address that your DB is hosted on

        }
    }

    # AWS
    # S3 Amazon Buscket config
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_FILE_OVERWRITE = False
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    # s3 static settings
    # PUBLIC_STATIC_LOCATION = 'static'
    #STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_STATIC_LOCATION}/'
    #STATICFILES_STORAGE = 'podcasts.storage_backends.StaticStorage'
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'podcasts.storage_backends.PublicMediaStorage'

    # SECURE_SSL_REDIRECT = True
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600, ssl_require=True)

ROOT_URLCONF = 'podcasts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]
# Template directory setting
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)
WSGI_APPLICATION = 'podcasts.wsgi.application'




# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(ROOT_FOLDER, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# list of activated languages
LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


SITE_ROOT = 1

# Loggin the info

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

# Activate Django-Heroku.
django_heroku.settings(locals(), logging=False)
