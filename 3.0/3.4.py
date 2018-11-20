#!/usr/bin/python

input = None

while input != "stop":
    input = raw_input("Enter a number: ")
    try:
        number = int(input)
        print "Number: " + str(number) + ", third power: " + str(pow(int(number), 3))
    except ValueError:
        if input != "stop":
            print input + " is not a number!"
