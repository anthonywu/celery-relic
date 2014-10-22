import os

BROKER_URL = os.environ['CELERY_RELIC_BROKER_URL']

# List of modules to import when celery starts.
CELERY_IMPORTS = ('tasks', )

CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}
