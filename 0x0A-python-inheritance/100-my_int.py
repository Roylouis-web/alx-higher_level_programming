#!/usr/bin/python3
"""
     a class MyInt that inherits from int
     object
"""


class MyInt(int):
    """
         a class MyInt that inherits from int
    """

    def __init__(self, value):
        """
            initialises the attribute
            value
        """
        self.__value = value

    def __str__(self):
        """
            returns a string of
            the attribute value
        """
        return str(self.__value)

    def __eq__(self, x):
        """
            returns False if
            the object is compared
            with equality operator
        """
        return False

    def __ne__(self, x):
        """
            return True if the
            the object is compared
            with the not equal operator
        """
        return True
