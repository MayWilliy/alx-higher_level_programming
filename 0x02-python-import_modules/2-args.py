#!/usr/bin/python3
if __name__ == "__main__":
    """ This program prints the number of and the list of its arguments
    """
    import sys
    num_arg = len(sys.argv) - 1
    if num_arg == 0:
        print("0 arguments.")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arg))
    for j in range(num_arg):
        print("{} : {}".format(j + 1, sys.argv[j + 1]))
