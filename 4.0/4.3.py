#!/usr/bin/python


def factorial(n):
    tmp = 1
    if n in (0, 1):
        return 1
    else:
        for i in range(2, n + 1):
            tmp = tmp * i
    return tmp


def main():
    n = int(raw_input("Enter an integer: "))
    print factorial(n)


main()
