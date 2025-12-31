import os

# По умолчанию — development
SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE')

if not SETTINGS_MODULE:
    # Если не задан явно — ставим development
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookclub.settings.development')