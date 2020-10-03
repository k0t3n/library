INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    # 3d-party apps
    'rest_framework',

    # project apps
    'src.apps.users',
    'src.apps.authors',
    'src.apps.books',
    'src.apps.libraries',
    'src.apps.publishers',
]
