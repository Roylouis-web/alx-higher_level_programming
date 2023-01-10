#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


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
        super().integer_validator("size", self.__size)
        super().__init__(size, size)
