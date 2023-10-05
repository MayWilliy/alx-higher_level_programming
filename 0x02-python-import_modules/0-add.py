#!/usr/bin/python3
if __name__ == "__main__":
    """This module prints the sum of 1 and 2."""
#import add_0
from add_0 import add

def add(a, b):
    a = 1
    b = 2
    sum = a + b
    print("{} + {} = {:1d}".format (a, b, sum))
add(1, 2)
