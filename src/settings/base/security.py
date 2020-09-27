import os

SECRET_KEY = '3@2pg_7vw)mbg65dpu!5or&#xt=54dyjc-#**hd=d+&5y#g^e('

HOSTNAME = os.environ.get('HOSTNAME', '127.0.0.1')

ALLOWED_HOSTS = [
    HOSTNAME,
]
