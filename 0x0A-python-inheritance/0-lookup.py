#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns an object's available attributes as a list."""
    return (dir(obj))
