#!/usr/bin/env ipython

print('Run this script with `-i` flag on for interactive use')

import celery
import random
import time
from tasks import add, add_long_time

def test1():
    r1 = add_long_time.delay(1, 1)
    while not r1.ready():
        time.sleep(1)
        continue
    add_result, fake_wait = r1.result
    print('Result is: {} after waiting {} seconds'.format(add_result, fake_wait))


def test_n_times(n):
    result_proxies = []
    for x in xrange(n):
        y = random.randint(0,10)
        r = add_long_time.delay(x, y)
        result_proxies.append(r)
    results = []
    for r in result_proxies:
        results.append(r.get())
    return results
