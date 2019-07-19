
import unittest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import models


class TestFibMethods(unittest.TestCase):

    def test_equal_1(self):
        self.assertEqual(models.Fib(1).calculate(), 1)

    def test_equal_2(self):
        self.assertEqual(models.Fib(3).calculate(), 2)

    def test_equal_3(self):
        self.assertEqual(models.Fib(4).calculate(), 3)

    def test_equal_4(self):
        self.assertEqual(models.Fib(10).calculate(), 55)

    def test_non_int_value(self):
        with self.assertRaises(ValueError):
            models.Fib("abc")


class TestFactMethods(unittest.TestCase):

    def test_equal_1(self):
        self.assertEqual(models.Fact(0).calculate(), 1)

    def test_equal_2(self):
        self.assertEqual(models.Fact(1).calculate(), 1)

    def test_equal_3(self):
        self.assertEqual(models.Fact(3).calculate(), 6)

    def test_equal_4(self):
        self.assertEqual(models.Fact(5).calculate(), 120)

    def test_non_int_value(self):
        with self.assertRaises(ValueError):
            models.Fact("abc")


if __name__ == "__main__":
    unittest.main()