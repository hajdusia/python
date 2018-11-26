#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


class Queue:

    def __init__(self, size=5):
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0           # first to get
        self.tail = 0           # first empty

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.items[self.tail] is not None and self.items[self.head] == self.items[self.tail]:
            raise ValueError("Queue is full")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.items[self.head] is None and self.items[self.head] == self.items[self.tail]:
            raise ValueError("Queue is empty")
        data = self.items[self.head]
        self.items[self.head] = None      # reference removed
        self.head = (self.head + 1) % self.n
        return data


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        for i in range(0, 3):
            self.queue.put(i)

    def test_get(self):
        self.assertEqual(self.queue.get(), 0)
        self.assertEqual(self.queue.get(), 1)
        self.assertEqual(self.queue.get(), 2)
        self.assertRaises(ValueError, self.queue.get)

    def test_put(self):
        for i in range(0, 3):
            self.queue.put(i)
        self.assertRaises(ValueError, self.queue.put, 0)


if __name__ == "__main__":
    unittest.main()
