#!/usr/bin/python3

from models.base import Base
"""
A class that inherit Base
"""


class Rectangle(Base):
    """
    The Rectangle class with Base inheritance
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): x.
        y (int): y.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This function creates new instances of the rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): The identity number of rectangle it defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        Function that prints the rectangle
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
            format(self.id, self.__x, self.__y, self.width, self.height))

    @property
    def width(self):
        """
        Function that retrieve the width of the rectangle
        return:
            int: of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Function that define property width of the rectangle
        arg:
            int: width of the recrangle
        raises:
            TypeError if the width is not an integer
            ValueError if the width is less than or equal to zero

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Function that retrieve the height of the rectangle
        return:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Function that define property height of the rectangle
        arg:
            int: height of the recrangle
        raises:
            TypeError if the height is not an integer
            ValueError if the height is less than or equal to zero

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Function that retrieve the x of the rectangle
        return:
            int: of the rectangle
        """
        return self.__x

    @width.setter
    def x(self, value):
        """
        Function that define property x of the rectangle
        arg:
            int: x of the recrangle
        raises:
            TypeError if the x is not an integer
            ValueError if the x is less than or equal to zero

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """
        Function that retrieve the y of the rectangle
        return:
            int: y of the rectangle
        """
        return self.__y

    @width.setter
    def y(self, value):
        """
        Function that define property y of the rectangle
        arg:
            int: y of the recrangle
        raises:
            TypeError if the y is not an integer
            ValueError if the y is less than or equal to zero

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__y = value

    def area(self):
        """
        this function calculate the area of a rectangel
        Return:
            int: area
        """
        return self.__width * self.__height

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dic) for dic in list_dicts]
        except FileNotFoundError:
            return []

    def display(self):
        """
        this function print the STOUT of a rectangel
        with the instance # 
        """
        if self.__y > 0:
            for i in range(self.__y):
                print()
            self.__y = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        This function assigns an argument to each attribute.

        Args:
            *args (tuple): Positional arguments.
            **kwargs (dict): Keyword arguments.
        """
        if args is not None and len(args) != 0:
            attr_names = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr_names[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This function returns the dictionary representation of a Rectangle.

        Returns:
            dict: rectangle.
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
