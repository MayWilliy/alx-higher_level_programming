#!/usr/bin/python3

"""
function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""

def is_same_class(obj, a_class):
    """
    This function returns True if the object is exactly an instance of the,
    specified class, else it returns  False

    Args:
        obj (a_class): The object to check type.
        a_class (type): type of type to check.

    Returns:
        A boolean- True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
