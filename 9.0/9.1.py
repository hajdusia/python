#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def print_list(node):
        while node:
            print node
            node = node.next

    def count_list(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(node):
        return node is None


def remove_head(node):
    new_head = node.next
    node_removed = node
    return new_head, node_removed


def remove_tail(head):
    if head.next is None:
        return None, head

    current = head
    previous = None
    while current.next:
        previous = current
        current = current.next
    if previous:
        previous.next = None
    return head, current


if __name__ == "__main__":
    head = None
    head = Node(2, head)  # [2]
    head = Node(3, head)  # [3, 2]
    head = Node(4, head)  # [4, 3, 3]

    while head:
        head, node = remove_head(head)
        print "Removed head: ", node

    head = None
    head = Node(5, head)  # [5]
    head = Node(6, head)  # [6, 5]
    head = Node(7, head)  # [7, 6, 5]

    while head:
        head, node = remove_tail(head)
        print "Removed tail: ", node
