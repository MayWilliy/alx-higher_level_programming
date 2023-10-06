#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    """This program prints the result of the addition of all arguments
    """
    sum_total = 0
    for j in range(len(sys.argv) - 1):
        sum_total += int(sys.argv[j + 1])
    print("{}".format(sum_total))
