#!/usr/bin/python3
from models.rectangle import Rectangle

"""
    Module for a class
    called Square
"""


class Square(Rectangle):
    """
        class Square that inherits
        from class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """
             returns readable information
             about the Square Object
        """

        id = self.id
        x = self.x
        y = self.y
        w = self.__size
        name = self.__class__.__name__
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(name,
                                                       id, x, y, w)

    @property
    def size(self):
        """
            gets the size of the
            Square Object
        """

        return self.__size

    @size.setter
    def size(self, size):
        """
            sets the size of
            the Square Object
        """

        if self.validate_width(size):
            self.width = size
            self.height = size

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
                    self.__size = args[i]
            if i == 2:
                if self.validate_x(args[i]):
                    self.x = args[i]
            if i == 3:
                if self.validate_y(args[i]):
                    self.y = args[i]

        if not args:
            if 'size' in kwargs:
                if self.validate_width(kwargs['size']):
                    self.__size = kwargs['size']
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'x' in kwargs:
                if self.validate_x(kwargs['x']):
                    self.x = kwargs['x']
            if 'y' in kwargs:
                if self.validate_y(kwargs['y']):
                    self.y = kwargs['y']

    def to_dictionary(self):
        """
            returns the dictionary representation of a Rectangle
        """
        old = self.__dict__
        return {
            'id': old['id'],
            'x': old['_Rectangle__x'],
            'size': old['_Square__size'],
            'y': old['_Rectangle__y'],
        }
