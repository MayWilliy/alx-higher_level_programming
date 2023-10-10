#!/usr/bin/python3
def no_c(my_string):
    """This function removes all characters c and C from a string."""
    result = " "
    for char in my_string:
        if char.lower() != "c":
            result += char
    return result
