#!/usr/bin/python3

class Square:
    
    def __init__(self, size):
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

    def area(self):
        """
        Calculate and return the area of the square.
        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """This function prints the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
