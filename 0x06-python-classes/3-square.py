#!/usr/bin/python3

"""
Function that write's class Square that 
defines a square by: (based on 2-square.py)
"""

class Square:
    """
    This is a Square class that defines a square with size validation.
    """
    def __init__(self, size=0):
    """
    Initialize a square with the given size.

    Args:
        size (int, optional): The size of the square (default is 0).
    """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return (self.__size *self.__size)
