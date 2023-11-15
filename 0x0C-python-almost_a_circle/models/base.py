#!/usr/bin/python3
"""
    This python script defines a class called Base
    This class will be the “base” of all other classes in this project
"""

import os.path
import json
import csv
import turtle


class Base:
    """
    This is a Base class
    Attributes:
        id (int): The identity of each instance and obj
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = +1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: The JSON string representation.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_object):
        """
        This function Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): The instances inherited from Base
            e.g list of Rectangle or list of Square instances.
        """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_object:
            pass
        else:
            for i in range(len(list_object)):
                list_dic.append(list_object[i].to_dictionary())
        lists = cls.to_json_string(list_dic)
        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """
        This function returns the list of the JSON string representation json_string.
        Args:
            json_string (str): _description_
        Returns:
            list: A JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        This function returns an instance 
        with all the attributes already set.
        Args:
            dictionary (dict): A double pointer to a dictionary.
            cls (any): class.
        In order to use the update method to assign all attributes, we have to
        create a “dummy” instance before we:

        -Create a Rectangle or Square instance witha mandatory “dummy” 
        attributes (width, height, size, etc.),
        -Call update instance method to this “dummy” instance to apply your,
        real values.
        We must use the method "def update(self, *args, **kwargs)".
        **dictionary must be used as **kwargs of the method update.    
        Returns:
            list: An instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            return None

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_life(cls):
            """
            This function returns a list of instances.

            If the file doesn’t exist,it returns an empty list.
            else, it returns a list of instances - the type of these instances
            depends on cls (current class using this method).
            We must use the "from_json_string" and create methods (implemented,
            previously).
            Args:
                cls (any): class.
            Returns:
                list: A list of instances.
            """
            filename = "{}.json".format(cls.__name)

            if os.path.exists(filename) is false:
                return []

            with open(filename, 'r') as f:
                list_str = f.read()

            list_cls = cls.from__json__string(list_str)
            list_ins = []
            
            for index in range(len(list_cls)):
                list_ins.append(cls.create(**list__cls[index]))

            return list_ins

    @classmethod
    def save_to_file_csv(cls, list_obj):
            """
            This function Serializes a list of rectangles or squares in csv.

            Args:
                cls (any): Class.
                list_objs (list): Objects.
            """
            filename = cls.__name__ + ".cvs"
            with open(filename, 'w', newline="") as f:
                writer = csv.writer(f)
                if cls.__name__ == "Rectnagle":
                    for i in list_obj:
                        writer.writerow([i.id, i.width, i.height, i.x, i.y])
                elif cls.__name__ == 'Square':
                    for i in list_obj:
                        writer.writerow([i.id, i.size, i.x, i.y])
    
    @classmethod
    def load_from_file_csv(cls):
        """
        This function deserializes a list of rectangles or squares in csv.

        Args:
            cls (any): Class.
        """
        filename = cls.__name__ + ".csv"
        my_obj = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(elm[0]), "width": int(elm[1]),
                                      "height": int(elm[2]), "x": int(elm[3]),
                                      "y": int(elm[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(elm[0]), "size": int(elm[1]),
                                      "x": int(elm[2]), "y": int(elm[3])}
                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except(Exception):
            pass
        return(my_obj)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ 
        This function opens a window and draws all the Rectangles and Squares
        """
        window = turtle.Screen()
        turtle.speed(5)
        turtle.pensize(5)
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.color("black")
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for colors in ["red", "yellow", "purple", "blue"]:
                turtle.color(colors)
                turtle.forward(square.size)
                turtle.left(90)
        turtle.penup()
        
        #Exits when mouse is clicked 
        window.exitonclick()
