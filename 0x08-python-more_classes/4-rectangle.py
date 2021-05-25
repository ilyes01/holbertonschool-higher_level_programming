#!/usr/bin/python3#!/usr/bin/python3
"""function empty rectangle
"""


class Rectangle:
    """function empty rectangle
    """
    pass

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if (self.height == 0 or self.width == 0):
            return 0
        return 2 * self.height + 2 * self.width

    def setWidth(self, width):
        self.width = width

    def __str__(self):
        """function str
        args
        self"""
        if self.width == 0 or self.height == 0:
            return ('')
        width = '#' * self.width
        rect = width
        for i in range(self.height - 1):
            rect += '\n'
            rect += width
        return rect

    def setHeight(self, height):
        """ height
        args
        self
        value"""
        self.__height = value
        if not(isinstance(value, int)):
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')

    def __repr__(self):
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)
