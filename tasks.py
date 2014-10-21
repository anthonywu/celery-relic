from celery import Celery
import os
import random
import time

# the app, named `celery` by default convention
celery = Celery('tasks', backend='amqp', broker=os.environ['CELERY_RELIC_BROKER_URL'])

@celery.task
def add(x, y):
    """The usual hello world demo."""
    return x + y

@celery.task
def add_long_time(x, y):
    "Take a long time to add two numbers in order to mock expensive transactions."
    wait = random.randint(1, 5)
    print("Will wait {} seconds".format(wait))
    time.sleep(wait)
    return (x + y, wait)

if __name__ == '__main__':
    celery.worker_main()
