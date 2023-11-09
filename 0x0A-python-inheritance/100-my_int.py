#!/usr/bin/python3

"""
Write a class MyInt that inherits from int
"""


class MyInt(int):
    """
    A class
    Arg:
        MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
