from os import environ

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ.get('POSTGRES_DB'),
        'USER': environ.get('POSTGRES_USER'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD'),
        'HOST': environ.get('POSTGRES_HOST', '127.0.0.1'),
        'PORT': environ.get('POSTGRES_PORT', '5432'),
        'CONN_MAX_AGE': 60,
    },
}
