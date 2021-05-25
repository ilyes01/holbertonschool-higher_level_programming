#!/usr/bin/python3#!/usr/bin/python3
"""function empty rectangle
"""


class Rectangle:
    """function empty rectangle
    """
    number_of_instances = 0
    print_symbol = '#'
    pass

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol

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
        width = '{}'.format(self.print_symbol) * self.width
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

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
