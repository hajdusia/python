#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class Time:

    def __init__(self, s=0):
        self.s = int(s)

    def __str__(self):
        h = self.s / 3600
        sec = self.s - h * 3600
        m = sec / 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        return "Time({0})".format(self.s)

    def __add__(self, other):
        return Time(self.s + other.s)

    def __cmp__(self, other):
        return cmp(self.s, other.s)

    def __int__(self):
        return self.s


class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Time(1)), "00:00:01")
        self.assertEqual(repr(Time(1)), "Time(1)")
        self.assertEqual(str(Time(-1)), "-1:59:59")
        self.assertEqual(repr(Time(-1)), "Time(-1)")
        self.assertEqual(str(Time("1")), "00:00:01")
        self.assertEqual(repr(Time("1")), "Time(1)")

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(4) + Time(5), Time(9))
        self.assertEqual(Time(-1) + Time(2), Time(1))
        self.assertEqual(Time(-10) + Time(2), Time(-8))
        self.assertEqual(Time("1") + Time(1), Time("2"))
        self.assertEqual(Time("-1") + Time(1), Time("0"))

    def test_cmp(self):
        self.assertTrue(Time(1) == Time(1))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(3) > Time(2))
        self.assertTrue(Time(-1) == Time(-1))
        self.assertTrue(Time(-1) != Time(-2))
        self.assertTrue(Time(-3) < Time(-2))
        self.assertTrue(Time("1") == Time(1))
        self.assertTrue(Time("1") != Time(2))
        self.assertTrue(Time("3") > Time(2))

    def test_int(self):
        self.assertTrue(Time("1").s == int("1"))
        self.assertTrue(Time("-1").s == int("-1"))

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
