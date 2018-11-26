#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.n == 10:
            raise ValueError("Stack is full")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.n == 0:
            raise ValueError("Stack is empty")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None
        return data


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        for i in range(0, 5):
            self.stack.push(i)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 0)
        self.assertRaises(ValueError, self.stack.pop)

    def test_put(self):
        for i in range(0, 5):
            self.stack.push(i)
        self.assertRaises(ValueError, self.stack.push, 0)


if __name__ == "__main__":
    unittest.main()
