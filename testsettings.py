
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

SECRET_KEY = 'notsecure'

INSTALLED_APPS = (
    'encrypted_fields',
)

ENCRYPTED_FIELDS_KEYDIR = os.path.join(os.path.dirname(__file__), 'testkey')
