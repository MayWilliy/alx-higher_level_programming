#!/usr/bin/python3

"""
Function that creates a class Square that 
defines a square by: (based on 0-square.py)
"""

class Square:
    """
    This is a Square class that defines a square with a private size attribute.
    """
    def __init__(self, size):
         """
        Initialize a square with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size # Private attribute
