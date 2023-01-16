#!/usr/bin/python3
import json

"""
    A module for a python
    class  called Base
"""


class Base(object):
    """
        A class Base to be
        tested by unittests
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns the JSON string
            representation of list_dictionaries

        """

        if not list_dictionaries or list_dictionaries is None:
            return json.dumps([])

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
             writes the JSON string
             representation of list_objs to a file
        """

        name = cls.__name__
        array = []

        if name == 'Rectangle':
            for obj in list_objs:
                dic2 = obj.__dict__
                array.append({
                    "y": dic2['_Rectangle__y'],
                    "x": dic2['_Rectangle__x'],
                    "id": dic2['id'],
                    "width": dic2['_Rectangle__width'],
                    "height": dic2['_Rectangle__height'],
                })

            with open('Rectangle.json', mode='w', encoding='utf-8') as f:
                f.write(json.dumps(array))

        if name == 'Square':
            for obj in list_objs:
                dic2 = obj.__dict__
                array.append({
                    "y": dic2['_Rectangle__y'],
                    "x": dic2['_Rectangle__x'],
                    "id": dic2['id'],
                    "size": dic2['_Square__size'],
                })

            with open('Square.json', mode='w', encoding='utf-8') as f:
                f.write(json.dumps(array))

    @staticmethod
    def from_json_string(json_string):
        """
            returns the list of the JSON string
            representation json_string
        """

        if not json_string or json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all
            attributes already set
        """
