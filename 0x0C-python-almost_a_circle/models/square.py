#!/urs/bin/python3

from inspect import classify_class_attrs
from models.rectangle import Rectangle


"""
A class Square that inherits from Rectangle
"""
class Square(Rectangle):
    """
    A Class that defines the properties of a square.
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): Value x.
        y (int): Value y.
        id (int): The identity of square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This function creates new instances of Square

        Args:
            size (int): The width and height of the square.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): The identity number of the square.
                                It Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __size__(self):
        """
        This function print square
        """
        return ("[square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """This function defines the property retriever for size.

        Returns:
            int: The size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """This function defines the calculate the size of sqaure

        Args:
            int: The size of one side of square
        raise:
            TypeError if value is not a type of integer 
            ValueError if value is not less than or equal t0 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This function assigns an argument to each attribute

       i Args:
            *args (tuple): arguments.
            **kwargs (dict): A double pointer to a dictionary.
        """
        attr_names = ['id', 'size', 'x', 'y']
        for i, arg in enumerate(args[:len(attr_names)]):
            setattr(self, attr_names[i], arg)
        for key, value in kwargs.items():
            if key == 'size':
                setattr(self, 'width', value)
                setattr(self, 'height', value)
            else:
                setattr(self, key, value)

    def to_dictionary(self):
        """
        This function returns the dictionary representation of a Square.

        Returns:
            dict: square.
        """
        dict1 = super().to_dictionary()
        dict2 = {}
        dict2['size'] = dict1['width']  # Use 'width' instead of '_Rectangle_width'
        dict2['id'] = dict1['id']
        dict2['x'] = dict1['x']
        dict2['y'] = dict1['y']
        return dict2
