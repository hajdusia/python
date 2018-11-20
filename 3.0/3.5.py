#!/usr/bin/python

try:
    length = int(raw_input("Enter an integer for length between 1 and 999: "))
except ValueError:
    print "Wrong argument!"
    exit(1)

ax = "|"
description = "0"

for i in range(1, length + 1, 1):
    if i < 10:
        ax += "....|"
        description += ("    " + str(i))
    elif i < 100:
        ax += "....|"
        description += ("   " + str(i))
    elif i < 1000:
        ax += "....|"
        description += ("  " + str(i))

print ax + "\n" + description
