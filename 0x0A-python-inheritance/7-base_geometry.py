#!/usr/bin/pyhton3


class BaseGeometry:
    """
    empty class
    Arg:
        public isinstance
    rasie:
        expection with message
    """
    def area(self):
        raise ("area() is not implemented")
    """
    Arg:
        public isinstance
    rasie:
        expection with message TypeError and ValueError
    """
    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value < 0:
            raise ValueError("<name> must be greater than 0")
        return self.name * self.value
