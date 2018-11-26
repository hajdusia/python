#!/usr/bin/python
# -*- coding: utf-8 -*-
import permutations


def mediana(data):
    n = len(data)
    sorted_data = sorted(data)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted_data[n // 2]  # integer division
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2.0


if __name__ == "__main__":
    items = permutations.permutation(10)
    print mediana(items)
