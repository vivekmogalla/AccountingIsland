from AccountingWorld.config.settings.common import *
import os
import dj_database_url

# Access the environment variables using 'os.environ' in your Django settings.py
SECRET_KEY = os.environ.get('SECRET_KEY') # Django SECRET_KEY

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# Debug Mode
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']

# Email Configuration
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

