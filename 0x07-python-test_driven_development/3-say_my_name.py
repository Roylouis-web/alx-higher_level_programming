#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    :param first_name: first name to be validated
    :param last_name: last name to be validated
    :return: a validated full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
