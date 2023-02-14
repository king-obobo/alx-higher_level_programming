#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """set/get the width of te rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        @property
        def height(self):
            """Sets/gets the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the value for height"""
            self.__height = value


        @property
        def x(self):
            """Sets/gets the x of the rectangle"""
            return self.__x

        @x.setter
        def x(self, value):
            """Sets the value for x"""
            self.__x = value


        @property
        def y(self):
            """Sets/gets the y of the rectangle"""
            return self.__y

        @y.setter
        def x(self, value):
            """Sets the value for y"""
            self.__y = value
