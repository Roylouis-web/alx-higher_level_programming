#!/usr/bin/python3

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

        if type(value) != int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")


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
