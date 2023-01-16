#!/usr/bin/python3
import unittest
from models.square import Square

"""
    Module for the class
    TestSquare
"""


class TestSquare(unittest.TestCase):
    """
        class TestSquare which tests
        all test cases of the Square Class
    """

    def test__str__(self):
        """
            Test for the output of
            __str__ magic function
        """

        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 5')

    def test_id_default(self):
        """
            tests output of
            default id
        """

        s1 = Square(5)
        s2 = Square(2, 2)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s2.id, s1.id + 1)

    def test_id_given(self):
        """
            tests output when
            id is given
        """

        s1 = Square(10, 2, 0, 12)
        s2 = Square(2, 10, 2, 9)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s2.id, 9)

    def test_update_args(self):
        """
        Tests for updates of the
        attributes of rectangle class
        """
        s1 = Square(5)
        self.assertEqual(s1.id, 4)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        s1.update(1, 2, 3)
        self.assertEqual(s1.size, 2)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        with self.assertRaises(TypeError):
            s1.update(89, "str", 3, 4)
        with self.assertRaises(TypeError):
            s1.update(89, 2, 3, [1, 2, 3])
        with self.assertRaises(ValueError):
            s1.update(89, -2, 3, 4)
        with self.assertRaises(ValueError):
            s1.update(89, 2, -3, -4)

    def test_update_kwargs(self):
        """
            test for updates of the attributes
            of the class using kwargs
        """

        s1 = Square(5)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)
        s1.update(size=7, y=1)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.y, 1)
        s1.update(1, 2, 3, 4, 5, size=89)
        self.assertEqual(s1.size, 2)
        with self.assertRaises(TypeError):
            s1.update(size="str", id=3, x=4, y=5)
        with self.assertRaises(TypeError):
            s1.update(size=89, y=2, height=15, id=5, x=[1, 2, 3])
        with self.assertRaises(ValueError):
            s1.update(size=-2, x=3, y=4, id=-5)
        with self.assertRaises(ValueError):
            s1.update(y=89, id=2, x=-3, width=-4, height=5)

    def test_to_dictionary(self):
        """
            tests if output is equal
        """
        r1 = Square(1, 2, 3, 4)
        dic = r1.to_dictionary()
        self.assertEqual(dic, {'x': 2, 'y': 3, 'size': 1, 'id': 4})
