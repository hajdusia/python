#!/usr/bin/python

numbers = [12, 345, 6, 78, 901, 23]

newNumbers = map(lambda x: str(x).zfill(3), numbers)
print("Numbers: " + str(newNumbers))
