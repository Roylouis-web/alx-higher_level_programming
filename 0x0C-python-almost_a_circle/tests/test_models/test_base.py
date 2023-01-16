#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""
    Module for the class
    TestBase
"""


class TestBase(unittest.TestCase):
    """
        class TestBase that tests all
        possible outcomes of the Base Class
    """

    def test_default_id(self):
        """
            test if the outcome is
            equal to the given argument
        """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)
        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)

    def test_equal_given_id(self):
        """
            test if the outcome is
            equal to the given argument
        """
        b1 = Base(10)
        self.assertEqual(b1.id, 10)
        b2 = Base(20)
        self.assertEqual(b2.id, 20)
        b3 = Base(30)
        self.assertEqual(b3.id, 30)

    def test_to_json_string(self):
        """
            test if the outcome is
            equal to the given argument
        """

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(dictionary,
                         {'x': 2, 'width': 10, 'id': 4, 'height': 7, 'y': 8})

    def test_from_json_string(self):
        """
            test if the outcome is
            equal to the given argument
        """

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output,
                         [{'height': 4, 'width': 10, 'id': 89},
                          {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string([]), [])
