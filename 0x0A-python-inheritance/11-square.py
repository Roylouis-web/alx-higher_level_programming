#!/usr/bin/python3
"""
    A non empty class called BaseGeometry
    that inherits from a super class Object
    and raises an error when area method is
    called and also validates the parameter
    'value'
"""


class BaseGeometry():
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
        """
            initialisation of the
            private attributes
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
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

class Square(Rectangle):
    """
        Write a class Square that inherits
        from Rectangle (9-rectangle.py)
    """

    def __init__(self, size):
        """
            initialisation of the
            private attribute size
        """
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", self.__size)

    def __str__(self):
        """
            returns the following rectangle
            description: [Square] <width>/<height>
        """

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
