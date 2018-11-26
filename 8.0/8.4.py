#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


def heron(a, b, c):
    if a + b < c or b + c < a or c + a < b:
        raise ValueError("Unfulfilled condition of triangle inequality")

    s = (a + b + c)/2
    print math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    heron(4, 4, 4)
