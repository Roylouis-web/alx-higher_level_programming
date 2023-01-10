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
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
