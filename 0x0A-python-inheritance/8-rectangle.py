#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
    class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py)
"""


class Rectangle(BaseGeometry):
    """
         class Rectangle that inherits from BaseGeometry
         (7-base_geometry.py)
    """

    def __init__(self, width, height):
        """
            initialisation of the
            private attributes
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
