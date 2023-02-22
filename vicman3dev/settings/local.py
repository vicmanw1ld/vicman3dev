from .base import *

import pymysql



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

pymysql.version_info = (1,4,2, 'final', 0)
pymysql.install_as_MySQLdb()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "vicman3dev",
        "USER": "vicman3dev",
        "PASSWORD": "pass",
        "HOST": "localhost",
        "PORT": "3306"
    }
}
