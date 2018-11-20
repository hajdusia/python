#!/usr/bin/python

a = [1, 2, 3, 4, 5, 6]
b = [3, 5, 7, 9]
print "Intersection: " + str(list(set(a).intersection(b)))
print "Union: " + str(list(set(a).union(b)))
