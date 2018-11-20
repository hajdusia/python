#!/usr/bin/python


result = 0


def sum_seq(seq):
    global result
    for item in seq:
        if isinstance(item, (list, tuple)):
            sum_seq(item)
        else:
            result += item
    return result


def main():
    seq = [1, (2, 3), [], [4, (5, 6, (7, 1))], 8, [(1, 2, [2, 2], 3), 9]]
    print sum_seq(seq)


main()
