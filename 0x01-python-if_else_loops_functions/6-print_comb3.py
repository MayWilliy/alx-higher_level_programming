#!/usr/bin/python3
for i in range (0, 9):
    for j in range (i + 1, 10):
        if i != j:
            if 1 == 0:
                print("0", end="")
            else:
                print("{}".format(i), end="")
            print("{}".format(j), end=", " if i != 8 or j != 9 else "\n")
