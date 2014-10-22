#!/usr/bin/env ipython

print('Run this script with `-i` flag on for interactive use')

from tasks import add, add_long_time

print(add.name)
print(add_long_time.name)

def do():
    r1 = add.delay(1, 2)
    return r1.ready(), r1
