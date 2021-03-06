"""
Main settings for simpletest project
"""
# Django settings for simpletest project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

import os
CURDIR = os.path.dirname(__file__)

MANAGERS = ADMINS

# 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_ENGINE = ''

# Or path to database file if using sqlite3.
DATABASE_NAME = ''

# Not used with sqlite3.
DATABASE_USER = ''

# Not used with sqlite3.
DATABASE_PASSWORD = ''

# Set to empty string for localhost. Not used with sqlite3.
DATABASE_HOST = ''

# Set to empty string for default. Not used with sqlite3.
DATABASE_PORT = ''

ACCOUNT_ACTIVATION_DAYS = 4 # days

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = CURDIR + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'za-3ysg_e=2qvd$pvvqb5=1sjm9czbsn&b79-o)az72%ge)els'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'simpletest.urls'

TEMPLATE_DIRS = (
    CURDIR + '/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'registration',
    'simpletest',
    'simpletest.profiles',
)

try:
    from simpletest.mysettings import DATABASE_ENGINE, \
                                      DATABASE_NAME, \
                                      DATABASE_USER, \
                                      DATABASE_PASSWORD, \
                                      DATABASE_HOST, \
                                      DATABASE_PORT
except ImportError:
    pass
