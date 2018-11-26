#!/usr/bin/python
# -*- coding: utf-8 -*-


def binary_search(data, number, start=0, end=None):
    print "Range: ", start, end
    if end is None:
        end = len(data) - 1

    if start > end:
        raise ValueError('Number not in list')

    mid = (start + end) // 2

    if number == data[mid]:
        return mid

    if number < data[mid]:
        return binary_search(data, number, start, mid - 1)
    else:
        return binary_search(data, number, mid + 1, end)


if __name__ == "__main__":
    items = range(0, 100)
    print binary_search(items, 32)
