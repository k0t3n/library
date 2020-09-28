from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).parents[2]  # go up for 2 parent directories

AUTH_USER_MODEL = 'users.User'

URL_SCHEME = getenv('URL_SCHEME', 'https')
