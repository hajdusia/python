#!/usr/bin/python
# -*- coding: utf-8 -*-

tmp = {}


def P(a, b):
    i = 0
    while i <= a:
        tmp[i] = {}
        j = 0
        while j <= b:
            if i < 0 or j < 0:
                raise ValueError("a or b lower than 0")
            elif i == 0 and j == 0:
                tmp[i][j] = 0.5
            elif i > 0 and j == 0:
                tmp[i][j] = 0.0
            elif i == 0 and j > 0:
                tmp[i][j] = 1.0
            else:
                tmp[i][j] = 0.5 * (tmp[i - 1][j] + tmp[i][j - 1])

            j += 1
        i += 1
    # print tmp
    return tmp[a][b]


def P_rec(a, b):
    if a < 0 or b < 0:
        raise ValueError("a or b lower than 0")
    elif a == 0 and b == 0:
        return 0.5
    elif a > 0 and b == 0:
        return 0.0
    elif a == 0 and b > 0:
        return 1.0
    else:
        return 0.5 * (P_rec(a - 1, b) + P_rec(a, b - 1))


if __name__ == "__main__":
    print P(60, 5)
    print P_rec(60, 5)
