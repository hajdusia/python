#!/usr/bin/python


def axis():
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

    return ax + "\n" + description


def grid():
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

    return table


def main():
    print axis()
    print grid()


main()
