#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""The python script defines a class Rectangle

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""

"""
A sub-class
"""


class Rectangle(BaseGeometry):
    """This function creates new instances of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
    """
    def __init__(self, width, height):

        self.__width = width
        self.__height = height

        self.integer_validator = ("width", width)
        self.integer_validator = ("height", height)
