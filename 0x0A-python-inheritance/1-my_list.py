#!/usr/bin/python3
"""
    class MyList that inherits from list
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
