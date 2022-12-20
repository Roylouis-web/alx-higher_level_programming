#!/usr/bin/python3
import dis
import math

"""
    Python class MagicClass that does exactly
    the same as the following Python bytecode.
"""


class MagicClass:
    """Attributes:
        attr1 (int): Radius of a circle
    """
    def __init__(self, radius=0):
        self.__radius = 0

        """
        __init__: initialises the attribute of the class
            Args:
            param(int): parameter to be used within the class.
        """

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
