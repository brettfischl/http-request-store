import os
db_url = os.environ.get('DATABASE_URL', None)
credentials = {}

def creds():
    if db_url:
        credentials['DATABASE_HOST'] = os.environ.get('DATABASE_HOST', None)
        credentials['DATABASE_USER'] = os.environ.get('DATABASE_USER', None)
        credentials['DATABASE_PASSWORD'] = os.environ.get('DATABASE_PASSWORD', None)
        credentials['DATABASE_NAME'] = os.environ.get('DATABASE_NAME', None)

    return credentials
