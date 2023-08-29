#!/usr/bin/python3

def safe_print_integer_err(value):
    """
     function that prints an integer.
    """
    try:
        print("{:d}".format(value))
        return true
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return false
        
