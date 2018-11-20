#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import unittest


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0:.2f}, {1:.2f})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0:.2f}, {1:.2f})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return round(math.sqrt(pow(self.x, 2) + pow(self.y, 2)), 2)


class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Point(1, 1)), "(1.00, 1.00)")
        self.assertEqual(repr(Point(1, 1)), "Point(1.00, 1.00)")
        self.assertEqual(str(Point(-1, 1)), "(-1.00, 1.00)")
        self.assertEqual(repr(Point(-1, 1)), "Point(-1.00, 1.00)")

    def test_eq(self):
        self.assertTrue(Point(1, 1) == Point(1, 1))
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertTrue(Point(-3, 1) == Point(-3, 1))

    def test_ne(self):
        self.assertTrue(Point(1, 1) != Point(1, 2))
        self.assertTrue(Point(1, 2) != Point(2, 2))
        self.assertTrue(Point(-3, 1) != Point(3, 1))

    def test_add(self):
        self.assertEqual(Point(1, 1) + Point(2, 2), Point(3, 3))
        self.assertEqual(Point(-1, 1) + Point(2, 2), Point(1, 3))
        self.assertEqual(Point(1, 10) + Point(2, -2), Point(3, 8))

    def test_sub(self):
        self.assertEqual(Point(1, 1) - Point(2, 2), Point(-1, -1))
        self.assertEqual(Point(6, 1) - Point(2, 2), Point(4, -1))
        self.assertEqual(Point(1, 0) - Point(2, 2), Point(-1, -2))

    def test_mul(self):
        self.assertEqual(Point(1, 1) * Point(2, 2), 4)
        self.assertEqual(Point(3, 1) * Point(2, 2), 8)
        self.assertEqual(Point(1, -5) * Point(2, 2), -8)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertEqual(Point(6, 8).length(), 10)
        self.assertEqual(Point(2, 2).length(), 2.83)
        self.assertEqual(Point(2, 5).length(), 5.39)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
