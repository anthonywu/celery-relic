from celery import Celery
import os
import random
import time

# the app, named `celery` by default convention
my_app = Celery('tasks', backend='amqp', broker=os.environ['CELERY_RELIC_BROKER_URL'])

@my_app.task
def add(x, y):
    """The usual hello world demo."""
    return x + y

@my_app.task
def add_long_time(x, y):
    "Take a long time to add two numbers in order to mock expensive transactions."
    wait = random.randint(1, 5)
    print("Will wait {} seconds".format(wait))
    time.sleep(wait)
    return (x + y, wait)


# === Main Bootstrap ===

# if __name__ == '__main__':
#     # celery.finalize()
#     celery.worker_main()
