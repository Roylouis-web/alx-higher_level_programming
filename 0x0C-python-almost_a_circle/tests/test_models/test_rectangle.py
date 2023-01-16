#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

"""
    Module for class
    TestRectangle
"""


class TestRectangle(unittest.TestCase):
    """
        Tests all possible outcomes
        of the class Rectangle
    """

    def test_id_default(self):
        """
            tests output of
            default id
        """

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r2.id, r1.id + 1)

    def test_id_given(self):
        """
            tests output when
            id is given
        """

        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(2, 10, 2, 5, 9)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r2.id, 9)

    def test_type_error(self):
        """
             tests for type error
             among the attributes
        """

        with self.assertRaises(TypeError):
            r1 = Rectangle("str", 10.67)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "meat")
        with self.assertRaises(TypeError):
            r1 = Rectangle(True, True)
        with self.assertRaises(TypeError):
            r1 = Rectangle([1, 2, 3], None)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, {"one": 1, "two": 2}, None, False, 89)
        with self.assertRaises(TypeError):
            r1 = Rectangle(7, 8, (12, 78), {1, 2, 4})
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3.8, 9.8)

    def test_value_error(self):
        """
            test attributes of a
            class for value error
        """

        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 8, -9, -8, 29)

    def test_area(self):
        """
            tests the area of
            the object
        """

        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)

    def test__str__(self):
        """
            Test for the output of
            __str__ magic function
        """

        r1 = Rectangle(4, 6, 2, 1, 12)

        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')

    def test_update_args(self):
        """
        Tests for updates of the
        attributes of rectangle class
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        with self.assertRaises(TypeError):
            r1.update(89, "str", 3, 4, 5)
        with self.assertRaises(TypeError):
            r1.update(89, 2, 3, [1, 2, 3], 5)
        with self.assertRaises(ValueError):
            r1.update(89, -2, 3, 4, -5)
        with self.assertRaises(ValueError):
            r1.update(89, 2, -3, -4, 5)

    def test_update_kwargs(self):
        """
            test for updates of the attributes
            of the class using kwargs
        """

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(1, 2, 3, 4, 5, 6, 7, 8,  width=1, x=2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.id, 89)
        with self.assertRaises(TypeError):
            r1.update(width="str", height=3, x=4, y=5)
        with self.assertRaises(TypeError):
            r1.update(x=89, y=2, height=15, id=5, width=[1, 2, 3])
        with self.assertRaises(ValueError):
            r1.update(height=-2, x=3, y=4, width=-5)
        with self.assertRaises(ValueError):
            r1.update(y=89, id=2, x=-3, width=-4, height=5)

    def test_to_dictionary(self):
        """
            tests if output is equal
        """
        r1 = Rectangle(1, 2, 3, 4, 5)
        dic = r1.to_dictionary()
        self.assertEqual(dic,
                         {'x': 3, 'y': 4, 'width': 1, 'height': 2, 'id': 5})
