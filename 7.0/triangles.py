#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from points import Point


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt3 = Point(x3, y3)
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.inline()

    def __str__(self):
        return "[({0:.2f}, {1:.2f}), ({2:.2f}, {3:.2f}), ({4:.2f}, {5:.2f})]".format(self.pt1.x, self.pt1.y, self.pt2.x,
                                                                                     self.pt2.y, self.pt3.x, self.pt3.y)

    def __repr__(self):
        return "Triangle({0:.2f}, {1:.2f}, {2:.2f}, {3:.2f}, {4:.2f}, {5:.2f})".format(self.pt1.x, self.pt1.y,
                                                                                       self.pt2.x, self.pt2.y,
                                                                                       self.pt3.x, self.pt3.y)

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3

    def __ne__(self, other):
        return not self == other

    def inline(self):
        if (self.pt3.y - self.pt2.y) * (self.pt2.x - self.pt1.x) == (self.pt2.y - self.pt1.y) * (
                self.pt3.x - self.pt2.x):
            raise ValueError("Tops of the triangle: {0}, {1} and {2} are collinear".format(str(self.pt1), str(self.pt2),
                                                                                           str(self.pt3)))

    def center(self):
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):
        return abs(0.5 * (
                    self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (
                        self.pt1.y - self.pt2.y)))

    def move(self, x, y):
        return Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y, self.pt3.x + x, self.pt3.y + y)

    def make3(self):
        result = [Triangle(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.center().x, self.center().y),
                  Triangle(self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y, self.center().x, self.center().y),
                  Triangle(self.pt3.x, self.pt3.y, self.pt1.x, self.pt1.y, self.center().x, self.center().y)]
        return result


class TestTriangle(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Triangle(0, 0, 0, 2, 2, 2)), "[(0.00, 0.00), (0.00, 2.00), (2.00, 2.00)]")
        self.assertEqual(repr(Triangle(0, 0, 0, -2, -2, -2)), "Triangle(0.00, 0.00, 0.00, -2.00, -2.00, -2.00)")

    def test_eq(self):
        self.assertTrue(Triangle(0, 0, 0, 2, 2, 2) == Triangle(0, 0, 0, 2, 2, 2))
        self.assertTrue(Triangle(0, 0, 0, -2, -2, -2) == Triangle(0, 0, 0, -2, -2, -2))

    def test_ne(self):
        self.assertTrue(Triangle(0, 0, 0, 2, 2, 2) != Triangle(0, 0, 0, -2, -2, -2))
        self.assertTrue(Triangle(0, 0, 0, -2, -2, -2) != Triangle(0, 0, 0, 2, 2, 2))

    def test_inline(self):
        self.assertRaises(ValueError, Triangle, 0, 0, 1, 1, 2, 2)
        self.assertRaises(ValueError, Triangle, 0, 0, -1, -1, -2, -2)

    def test_center(self):
        self.assertEqual(Triangle(0, 0, 0, 8, 8, 8).center(), Point(2.00, 5.00))
        self.assertEqual(Triangle(2, 2, 2, 5, 5, 5).center(), Point(3.00, 4.00))

    def test_area(self):
        self.assertEqual(Triangle(0, 0, 0, 2, 2, 2).area(), 2)
        self.assertEqual(Triangle(2, 2, 2, 5, 5, 5).area(), 4.5)

    def test_move(self):
        self.assertEqual(Triangle(0, 0, 0, 2, 2, 2).move(3, 3), Triangle(3, 3, 3, 5, 5, 5))
        self.assertEqual(Triangle(0, 0, 0, 2, 2, 2).move(-3, 3), Triangle(-3, 3, -3, 5, -1, 5))

    def test_make3(self):
        self.assertEqual(Triangle(2, 2, 2, 5, 5, 5).make3(), [Triangle(2.00, 2.00, 2.00, 5.00, 3.00, 4.00),
                                                              Triangle(2.00, 5.00, 5.00, 5.00, 3.00, 4.00),
                                                              Triangle(5.00, 5.00, 2.00, 2.00, 3.00, 4.00)])

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
