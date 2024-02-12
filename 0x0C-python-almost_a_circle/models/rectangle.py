#!/usr/bin/python3
"""Defines a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Subclass of Base with private instance attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor to assign each arg with the right attr"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def x(self):
        """gets y"""
        return self.__y

    @y.setter
      def y(self, value):
        """sets y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """calculates the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints rectangle using '#'"""
        print("\n" * self.y, end="")
        print(("\n" + " " * self.x + "#" * self.width) * self.height)

    def __str__(self):
        """returns string representatin of the class"""
        return "[Rectangle] ({:d}) <{:d}>/<{:d}> - <{:d}>/<{:d}>".format(
                self.id, self.x, self.y, self.width, self.height)


