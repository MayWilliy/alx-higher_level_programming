#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """
    class:
        Mylist
    Args:
        list (list): the list to sort in ascending order.
    """
    def print_sorted(self):
        """
        Function that prints a list in ascending order.
        """
        list_ = self[:]
        list_.sort()
        print(list_)
