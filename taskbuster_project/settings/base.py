"""
Django settings for taskbuster_project project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
#print("you are in settings.base")
import os
from .key import SECRET_KEY


# SEEMS TO BE CIRCULAR IMPORT PROBLEM, GO OVER WHY
# FOR NOW USE A KEY FILE BUT ADD IT TO .gitignore

# for secret key
# from django.core.exceptions import ImproperlyConfigured

# def get_env_variable(var_name):
#     try:
#         print("looking for {}".format(var_name))
#         key = os.environ.get(var_name, 'default')
#         print("returning {}".format(key))
#         print()
#         #print("found: ", os.environ['SECRET_KEY'])
#         #return os.environ[var_name]
#         return os.environ.get(var_name, 'default')
#     except KeyError:
#         error_msg = "Set the %s environment variable" % var_name
#         raise ImproperlyConfigured(error_msg)

# SECRET_KEY = get_env_variable('SECRET_KEY')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# points to folder containing this file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party
    # my apps
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'taskbuster_project.urls'

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

WSGI_APPLICATION = 'taskbuster_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Tell Django to look for static files in the 
# taskbuster_project/static directory
# With this configuration, Django will look for static files
# in a folder named static inside each app and into the 
# taskbuster_project/static folder
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)