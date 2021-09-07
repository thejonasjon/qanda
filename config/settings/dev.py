from .base import *
from pathlib import Path

from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

INSTALLED_APPS += [

]


MEDIA_URL = '/uploaded/'
MEDIA_ROOT = BASE_DIR / 'media'