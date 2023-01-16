#!/usr/bin/python3
from models.base import Base

"""
    A module for a class
    called Rectangle
"""


class Rectangle(Base):
    """
        A class Rectangle that inherits
        from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if self.validate_width(width):
            self.__width = width
        if self.validate_height(height):
            self.__height = height
        if self.validate_x(x):
            self.__x = x
        if self.validate_y(y):
            self.__y = y

    @property
    def width(self):
        """
        return: the value assigned
        to the private instance attribute
        'width'
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        sets the value of the private
        instance attribute 'width'
        """

        if self.validate_width(width):
            self.__width = width

    @staticmethod
    def validate_width(width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            return True

    @property
    def height(self):
        """
        return: the value assigned
        to the private instance attribute
        'height'
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        sets the value of the private
        instance attribute 'height'
        """

        if self.validate_width(height):
            self.__height = height

    @staticmethod
    def validate_height(height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            return True

    @property
    def x(self):
        """
        return: the value assigned
        to the private instance attribute
        'x'
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        sets the value of the private
        instance attribute 'x'
        """

        if self.validate_x(x):
            self.__x = x

    @staticmethod
    def validate_x(x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            return True

    @property
    def y(self):
        """
        return: the value assigned
        to the private instance attribute
        'y'
        """

        return self.__y

    @y.setter
    def y(self, y):
        """
        sets the value of the private
        instance attribute 'y'
        """

        if self.validate_width(y):
            self.__y = y

    @staticmethod
    def validate_y(y):
        """
            validates the value
            passed to assigned to y
        """

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            return True

    def area(self):
        """
        return: The area of the object
        """

        height = self.__height
        width = self.__width

        return height * width

    def display(self):
        """
            prints in stdout the Rectangle
            instance with the character '#'
        """
        print('\n' * self.__y, end='')
        for i in range(0, self.__height):
            for line in range(0, self.__x):
                print(' ', end='')
            for j in range(0, self.__width):
                if j == self.__width - 1:
                    print('#')
                else:
                    print('#', end='')

    def __str__(self):
        id = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        name = self.__class__.__name__
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(name,
                                                            id, x, y, w, h)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        param args: unlimited arguments to be
        passed into the function
        return: Nothing
        """

        for i in range(0, len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                if self.validate_width(args[i]):
                    self.__width = args[i]
            if i == 2:
                if self.validate_height(args[i]):
                    self.__height = args[i]
            if i == 3:
                if self.validate_x(args[i]):
                    self.__x = args[i]
            if i == 4:
                if self.validate_y(args[i]):
                    self.__y = args[i]

        if not args:
            if 'width' in kwargs:
                if self.validate_width(kwargs['width']):
                    self.__width = kwargs['width']
            if 'height' in kwargs:
                if self.validate_width(kwargs['height']):
                    self.__height = kwargs['height']
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'x' in kwargs:
                if self.validate_width(kwargs['x']):
                    self.__x = kwargs['x']
            if 'y' in kwargs:
                if self.validate_width(kwargs['y']):
                    self.__y = kwargs['y']

    def to_dictionary(self):
        """
            returns the dictionary representation of a Rectangle
        """
        old = self.__dict__
        return {
            'x': old['_Rectangle__x'],
            'y': old['_Rectangle__y'],
            'id': old['id'],
            'height': old['_Rectangle__height'],
            'width': old['_Rectangle__width'],
        }
