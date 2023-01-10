#!/usr/bin/python3
"""
    class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

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
        super().integer_validator("width", self.__height)
        super().integer_validator("height", self.__height)

    def area(self):
        """
            returns the area of
            the rectangle object
        """

        return self.__width * self.__height

    def __str__(self):
        """
            returns the following rectangle
            description: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
