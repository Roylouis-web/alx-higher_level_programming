#!/usr/bin/python3
"""
    class MyList that inherits from list
"""


class MyList(list):
    """
    class MyList that inherits from list
    """

    def print_sorted(self):
        """
        prints a sorted list
        in ascending order
        """

        if issubclass(MyList, list):
            print(sorted(self))
