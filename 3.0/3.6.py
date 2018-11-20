#!/usr/bin/python

try:
    height = int(raw_input("Enter an integer for height: "))
    width = int(raw_input("Enter an integer for width: "))
except ValueError:
    print "Wrong arguments!"
    exit(1)

table = "+"

for i in range(0, height, 1):
    for j in range(0, width, 1):
        table += "---+"
    table += "\n|"

    for j in range(0, width, 1):
        table += "   |"
    table += "\n+"

for j in range(0, width, 1):
    table += "---+"

print table
