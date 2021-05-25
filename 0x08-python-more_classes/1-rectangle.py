#!/usr/bin/python3
"""function empty rectangle
"""


class Rectangle:
    """function empty rectangle
    """
    pass
    def __init__(self, width=0, height=0):
        """fucntion
        args
        width
        height"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """funciton height
        args
        self"""
        return self.__height

    @height.setter
    def height(self, value):
        """function height
        args
        self
        value"""
        if not(isinstance(value, int)):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise TypeError('height must be >= 0')
        else:
            self.__height = value
            return (value)

    @property
    def width(self):
        """function width
        arg:self"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        args: self
        value"""
        if not(isinstance(value, int)):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise TypeError('width must be >= 0')
        else:
            self.__width = value
            return (value)
