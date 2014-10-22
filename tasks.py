from celery import Celery
import os
import random
import time
import traceback

my_app = Celery('tasks', backend='amqp', broker=os.environ['CELERY_RELIC_BROKER_URL'])

@my_app.task
def add(x, y):
    """The usual hello world demo."""
    # traceback.print_stack()
    return x + y

@my_app.task
def add_long_time(x, y):
    """Take a long time to add two numbers in order to mock expensive transactions."""
    # traceback.print_stack()
    wait = random.randint(1, 5)
    print("Will wait {} seconds".format(wait))
    time.sleep(wait)
    return (x + y, wait)
