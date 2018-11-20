#!/usr/bin/python


def swap(list, left, right):
    part1 = list[:left]
    part2 = list[left:right]
    part3 = list[right:]

    part2 = part2[::-1]

    tmp = part1 + part2 + part3
    list = tmp

    return list


def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print swap(list, 2, 5)


main()
