#!/usr/bin/python3
""" 
    A class called Mylist 
    that inherits from a base class
    'list' and prints a sorted list
    in ascending order
"""
class MyList(list):
    """
    Attribute:
    print_sorted: prints the elements
    of the Mylist obj in ascending order
    """

    def print_sorted(self):
        """
        prints a sorted list
        in ascending order
        """

        if issubclass(MyList, list):
            copy = self.copy()
            copy.sort()
            print(copy)
