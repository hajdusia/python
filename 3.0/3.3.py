#!/usr/bin/python

for i in range(0, 30, 1):
    if i % 3 != 0:
        print i

for i in filter(lambda x: x % 3 != 0, range(0, 30)):
    print i
