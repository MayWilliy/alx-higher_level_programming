#!/usr/bin/python3
for digit in range (0, 10):
    for digital in range (digit + 1, 10):
        if digit == 8 and digital == 9:
        print("{}{}".format(digit, digital))
    else:
        print("{}{}".format(digit, digital) end=", ")
