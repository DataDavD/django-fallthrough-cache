TEST_RUNNER = 'django.test.runner.DiscoverRunner'

SECRET_KEY = 'whatever'

CACHES = {
    'a': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'a',
        'TIMEOUT': None,
        'VERSION': 1
    },
    'b': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'b',
        'TIMEOUT': None,
        'VERSION': 1
    },
    'c': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'c',
        'TIMEOUT': None,
        'VERSION': 1
    },
    'fallthrough': {
        'BACKEND': 'fallthrough_cache.FallthroughCache',
        'LOCATION': 'fallthrough',
        'OPTIONS': {
            'cache_names': ['a', 'b', 'c']
        }
    }
}
