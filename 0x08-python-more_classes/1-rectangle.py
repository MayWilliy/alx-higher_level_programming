#!/usr/bin/python3
"""a Rectangle class that defines a rectangle"""


class Rectangle:
    """
    This s a rectangle class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
    """
    getter method to get the width of rectangle
    int the width of rectangle
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """
    Setter method to set the width of the rectangle.
    Args
        value (int): The width of the rectangle.
    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    @property
    def height(self):
        return self.__height
    """getter method to get the height of rectangle
                int the height of rectangle"""

    @height.setter
    def height(self, value):
        """
        Setter method to set the width of the rectangle.
        Args:
            value (int): The width of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
