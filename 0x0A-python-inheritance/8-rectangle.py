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
            Initialises the attributes 
            of the class Rectangle
        """


        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
