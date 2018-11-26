#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import permutations


def insertion(data):
    counter = 0
    while counter < len(data) - 1:
        for i in range(counter + 1, 0, -1):
            if data[i] < data[i - 1]:
                data[i], data[i - 1] = data[i - 1], data[i]
            else:
                break
        counter += 1


def selection(data):
    swapped = True
    counter = 0
    while swapped:
        swapped = False
        min = data[counter]
        for i in range(counter, len(data)):
            if min <= data[i]:
                min = data[i]
                index = i
                swapped = True
        data[counter], data[index] = data[index], data[counter]
        counter += 1
        if counter == len(data):
            break


if __name__ == "__main__":
    numbers = [100, 1000, 10000, 100000, 1000000]

    for i in numbers:
        items = permutations.permutation(i)
        items2 = items[:]
        t0 = time.time()
        insertion(items)
        t1 = time.time()

        t2 = time.time()
        selection(items2)
        t3 = time.time()

        total_insert = t1 - t0
        total_select = t3 - t2

        print i, "elements: insert sort:", total_insert, "select sort:", total_select
