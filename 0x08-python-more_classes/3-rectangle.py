#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
"""


class Rectangle:
    """
    A class
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
    Setter method to set the height of the rectangle
    Args
        value (int): The height of the rectangle.
    Raises
        TypeError: If value is not an integer.
        ValueError: If value is less than
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
     calculates the perimeter of the rectangle. If either the 
     width or height is equal to 0, it returns 0 as specified.
    """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    """
    method has been customized to return a string representation 
    of the rectangle using # characters. If either the width or 
    height is equal to 0, it returns an empty string.
    """
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    """
        method has been added to return a string representation of 
        the rectangle in the form of Rectangle(width, height)
    """
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
