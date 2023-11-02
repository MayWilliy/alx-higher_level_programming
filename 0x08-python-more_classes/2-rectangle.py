#!/usr/bin/python3
"""
A Rectangle class that defines a rectangle
"""


class Rectangle:
    """
    This s a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """
        getter method to get the width of rectangle
        int the width of rectangle
    """
    @property
    def width(self):
        return self.__width

    """
        Setter method to set the width of the rectangle
        Args
            value (int): The width of the rectangle.
        Raises
            TypeError: If value is not an integer.
            ValueError: If value is less than
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """
        getter method to get the height of rectangle
        int the height of rectangle
    """
    @property
    def height(self):
        return self.__height

    """
        Setter method to set the width of the rectanl
        Agr
            value (int): The width of the rectangle.
        Raise
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
    """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """
        Calculate and return the area of the square
        Return int: The area of the square.
    """
    def area(self):
        return self.__width * self.__height

    """
        Calculate and return the perimertr of the rec
        int: The primeter of the rectangle.
    """
    def perimeter(self):
        return 2 * (self.__width + self.__height)
