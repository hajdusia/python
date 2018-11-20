#!/usr/bin/python

# 1st OK
x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;

# 2nd Invalid syntax, each statement should be placed in separated line, like below:
for i in "qwerty":
    if ord(i) < 100:
        print i

# 3rd OK
for i in "axby": print ord(i) if ord(i) < 100 else i