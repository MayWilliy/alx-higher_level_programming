#!/usr/bin/python3
i = 0
for j in range(ord('z') and ord('a') -1, -1):
    print("{}".format(chr(j - i)), end="")
    if i % 2 == 0:
        i -= 32


