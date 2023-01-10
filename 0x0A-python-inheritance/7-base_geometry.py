#!/usr/bin/python3
"""
    a class BaseGeometry
    (based on 6-base_geometry.py).
"""


class BaseGeometry(object):
    """
        a class BaseGeometry
        (based on 6-base_geometry.py).
    """

    def area(self):
        """
            raises an Exception with the
            message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validates the value passed
            into the function as argument
        """

        if type(value) is not int:
            raise TypeError(name +  ' ' + 'must be an integer')
        elif value <= 0:
            raise ValueError(name + ' ' + 'must be greater than 0')
