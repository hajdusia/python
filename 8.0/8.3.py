#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import math


def calc_pi(n=100):
    inside = 0
    for i in range(0, n):
        x2 = random.random() ** 2
        y2 = random.random() ** 2
        if math.sqrt(x2 + y2) < 1.0:
            inside += 1

    pi = (float(inside) / n) * 4
    print(pi)


if __name__ == "__main__":
    calc_pi()
