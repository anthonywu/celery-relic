#!/usr/bin/env ipython

print('Run this script with `-i` flag on for interactive use')

import celery
import time
from tasks import add, add_long_time

def test1():
    r1 = add_long_time.delay(1, 1)
    while not r1.ready():
        time.sleep(1)
        continue
    add_result, fake_wait = r1.result
    print('Result is: {} after waiting {} seconds'.format(add_result, fake_wait))

test1()
