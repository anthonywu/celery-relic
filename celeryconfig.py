import logging
import os

_logger = logging.getLogger('celeryconfig')

BROKER_URL = os.environ['CELERY_RELIC_BROKER_URL']
CELERY_RESULT_BACKEND = 'amqp'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('tasks', )

CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}

CELERYD_LOG_FORMAT = "[%(asctime)s: %(levelname)s/%(processName)s/%(process)d/%(threadName)s] %(message)s]"

_logger.info('celeryconfig loaded')
