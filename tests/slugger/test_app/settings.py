SECRET_KEY = 'test'

INSTALLED_APPS = [
    'tests.slugger.test_app',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
