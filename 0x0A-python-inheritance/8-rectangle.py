#!/usr/bin/python3
"""
    A non empty class called BaseGeometry
    that inherits from a super class Object
    and raises an error when area method is
    called and also validates the parameter
    'value'
"""


class BaseGeometry(object):
    """for use with shapes. Super class.
    """

    def area(self):
        """instance method to calculate area of shape
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer input
        """
        if type(value) != int:
            raise TypeError(name + ' ' + "must be an integer")
        elif value <= 0:
            raise ValueError(name + ' ' + "must be greater than 0")


class Rectangle(BaseGeometry):
    """
         class Rectangle that inherits from BaseGeometry
         (7-base_geometry.py)
    """

    def __init__(self, width, height):

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
        self.__width = width
        self.__height = height
