"""
Django settings for MPV_Landing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__) + '/../')

BASE_PATH = os.path.abspath(os.path.dirname(__file__) + '/../../')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uz!w_&y7h+tn+oba#*eu^o!f!bev=hgppa=%*fz+#+m*fz+b2z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

SITE_ID = 1

ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    '*',
    ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'pipeline',
    'conference',
    'sekizai',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
)

ROOT_URLCONF = 'PythonMN_Landing.urls'

WSGI_APPLICATION = 'PythonMN_Landing.wsgi.application'

# DATABASE
# DATABASES = {'default': dj_database_url.config()}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'python',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'python',
        'PASSWORD': 'python',
        'HOST': 'localhost',    # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '',      # Set to empty string for default.
    }
}
CONN_MAX_AGE = 600

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static-only')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static', 'static'),
    )

PIPELINE_CSS = {
    'pythonMN_base': {
        'source_filenames': (
            'static/css/bootstrap.min.css',
            'static/css/styles.css',
        ),
        'output_filename': '/css/base.css',
        'extra_context': {
            'media': 'screen,print',
        },
    },
}

PIPELINE_JS = {
    'pythonMN_base': {
        'source_filenames': (
            'static/js/bootstrap.min.js',
            'static/js/jquery.min.js',
            'static/js/jquery.validate.min.js',
        ),
        'output_filename': 'static/js/base.js',
    }
}