#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """A subclass of list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
