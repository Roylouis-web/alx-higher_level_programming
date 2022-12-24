#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
        checks all possible edge cases
    """
    def test_max(self):
        """
        checks for maximum element
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
    def test_is_empty(self):
        """
        checks if a list is empty
        """
        self.assertEqual(max_integer([]), None)
    def test_max_negative(self):
        """
        checks for max in a list of
        positive and negative elements
        :return:
        """
        self.assertEqual(max_integer([-2, -67, 90, 78]), 90)
