#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


def permutation(n):
    items = range(0, n)
    return random.sample(items, len(items))


def ascending_order_almost_sorted(n, changes):
    items = range(1, n + 1)
    for i in range(changes):
        old_index = random.randint(0, n - 1)
        new_index = random.randint(0, n - 1)
        items[old_index], items[new_index] = items[new_index], items[old_index]
    return items


def descending_order_almost_sorted(n, changes):
    items = range(n, 0, -1)
    for i in range(0, changes):
        old_index = random.randint(0, n - 1)
        new_index = random.randint(0, n - 1)
        items[old_index], items[new_index] = items[new_index], items[old_index]
    return items


def gaussian(n):
    items = [float] * n
    for i in range(0, n):
        items[i] = random.gauss(0, 0.1)
    return items


def permutation_with_repetition(n):
    items = [int] * n
    for i in range(0, n):
        items[i] = random.randint(0, n / 2)
    return items

