#!/usr/bin/python3
"""Defines a Base class"""


class Base:
    """Base model.

    This represents the base for all other classes in this proect
    Private class attr:
        __nb_object(int): Nuber of intantiated bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base.
        Args:
            id(int): The identity of the new Base
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


