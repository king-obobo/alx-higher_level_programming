#!/usr/bin/python3
"""Defines a Base class"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base.
        Args:
            id(int): The identity of the new Base
        """
        if id != None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1


