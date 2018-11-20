#!/usr/bin/python


def factorial(n):
    tmp = 1
    if n in (0, 1):
        return 1
    else:
        for i in range(2, n + 1):
            tmp = tmp * i
    return tmp


def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return b
