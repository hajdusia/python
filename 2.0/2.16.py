#!/usr/bin/python

line = "An example text that contains GvR"

old = "GvR"
new = "Guido van Rossum"

line = line.replace(old, new, 1)
print(line)
