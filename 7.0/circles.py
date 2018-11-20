#!/usr/bin/python
# -*- coding: utf-8 -*-


import math
import unittest

from points import Point


class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("The radius contains negative value")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle({0:.2f}, {1:.2f}, {2:.2f})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return round(math.pi * math.pow(self.radius, 2), 2)

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        distance_between_centers = round(math.sqrt(pow(self.pt.x - other.pt.x, 2) + pow(self.pt.y - other.pt.y, 2)), 2)
        new_diameter = self.radius + other.radius + distance_between_centers
        new_center = Point((self.pt.x + other.pt.x)/2, (self.pt.y + other.pt.y)/2)
        new_radius = new_diameter/2
        if self.pt.x == other.pt.x or self.pt.y == other.pt.y:
            new_radius = max(self.radius, other.radius)
        return Circle(new_center.x, new_center.y, new_radius)


class TestCircle(unittest.TestCase):

    def setUp(self): pass

    def test_init(self):
        self.assertRaises(ValueError, Circle, 0, 0, -1)
        self.assertRaises(ValueError, Circle, 0, 0, -2)

    def test_print(self):
        self.assertEqual(repr(Circle(0, 0, 2)), "Circle(0.00, 0.00, 2.00)")
        self.assertEqual(repr(Circle(2, 2, 2)), "Circle(2.00, 2.00, 2.00)")

    def test_eq(self):
        self.assertTrue(Circle(0, 0, 2) == Circle(0, 0, 2))
        self.assertTrue(Circle(2, 2, 2) == Circle(2, 2, 2))

    def test_ne(self):
        self.assertTrue(Circle(0, 0, 2) != Circle(0, 0, 1))
        self.assertTrue(Circle(2, 2, 2) != Circle(1, 1, 1))

    def test_area(self):
        self.assertEqual(Circle(0, 0, 2).area(), 12.57)
        self.assertEqual(Circle(2, 2, 2).area(), 12.57)

    def test_move(self):
        self.assertEqual(Circle(0, 0, 2).move(3, 3), Circle(3, 3, 2))
        self.assertEqual(Circle(2, 2, 2).move(-3, -3), Circle(-1, -1, 2))

    def test_cover(self):
        self.assertEqual(Circle(0, 0, 2).cover(Circle(4, 4, 3)), Circle(2, 2, 5.33))
        self.assertEqual(Circle(0, 0, 1).cover(Circle(0, 0, 3)), Circle(0, 0, 3))
        self.assertEqual(Circle(0, 1, 1).cover(Circle(0, 0, 3)), Circle(0, 0, 3))

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
