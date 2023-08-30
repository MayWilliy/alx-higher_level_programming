#!/usr/bin/python3

"""
Function that write's class Square that 
defines a square by: (based on 2-square.py)
"""

class Square:
    """
    This is a Square class that defines a square with a getter and setter for size.
    """
    def __init__(self, size=0):
         """
        Initialize a square with the given size.
        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method to set the size.
        Args:
         value (int): The size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        """
        Calculate and return the area of the square.
        Returns:
            int: The area of the square.
        """
    def area(self):
        return (self.__size *self.__size)
