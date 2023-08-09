#!/usr/bin/python
for j in range (0, 100):
    if j == 99:
        print("{}".format(j))
    else:
        print("{:02}".format(j) end=",")
