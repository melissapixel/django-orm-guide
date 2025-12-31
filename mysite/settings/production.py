import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',') if os.getenv('ALLOWED_HOSTS') else []   # Получаем список хостов из переменной окружения

# Добавим защиту: если SECRET_KEY не задан — ошибка
if not os.getenv('SECRET_KEY'):
    raise ValueError("SECRET_KEY must be set in production!")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'db'),  # по умолчанию 'db' для Docker
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Безопасность
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True