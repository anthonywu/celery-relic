#!/usr/bin/env ipython -i

import celery

from tasks import add, add_long_time

print(add.name)
print(add_long_time.name)

def do():
    r1 = add.delay(1, 2)
    return r1.ready(), r1
