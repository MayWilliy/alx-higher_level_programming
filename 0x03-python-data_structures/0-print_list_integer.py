#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """This function that prints all integers of a list
    """
    my_list = [1, 2, 3, 4, 5]
    for item in my_list:
        print("{}".format(item), end="\n")
