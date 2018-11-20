#!/usr/bin/python


def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return b


def main():
    n = int(input("Enter an index of element in fibonacci sequence: "))
    print fibonacci(n)


main()
