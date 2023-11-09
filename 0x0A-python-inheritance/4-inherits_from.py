#!/usr/bin/python3

"""
Write a function that returns True if the object is an
instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Check if the object is an instance or
    inherited from the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The specified class.

    Returns:
        bool: True if the object is an instance or
        inherited from the specified class, otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
