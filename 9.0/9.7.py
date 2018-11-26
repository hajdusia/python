#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        elif self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            pass

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def count(self):
        if self.root:
            return self.root.count()
        else:
            return 0

    def search(self, data):
        if self.root:
            return self.root.search(data)
        else:
            return None


def count_leafs(top):
    if not top.left and not top.right:
        return 1

    counter = 0
    if top.left:
        counter += count_leafs(top.left)
    if top.right:
        counter += count_leafs(top.right)
    return counter


def count_total(top):
    counter = top.data
    if top.left:
        counter += count_total(top.left)
    if top.right:
        counter += count_total(top.right)
    return counter


if __name__ == "__main__":

    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(1)
    bst.insert(2)
    bst.insert(6)
    bst.insert(4)
    print count_total(bst.root)
    print count_leafs(bst.root)
