#!/usr/bin/python3
"""
Function that returns the list of available attributes and methods of an obj.
"""


def lookup(obj):
    """
    Arg
        obj (class): the object
    return
        list the list of avaliable attribute and methods of an object
    """
    return dir(obj)
