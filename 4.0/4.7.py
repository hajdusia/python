#!/usr/bin/python


result = []


def flatten_seq(seq):
    for item in seq:
        if isinstance(item, (list, tuple)):
            flatten_seq(item)
        else:
            result.append(item)
    return result


def main():
    seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [(1, 2, [2, 2], 3), 9]]
    print flatten_seq(seq)


main()
