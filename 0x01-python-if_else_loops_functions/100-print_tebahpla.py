#!/usr/bin/python3
for j in range(ord('z') and ord('a') -1, -1):
    if (ord('z') - j) % 2 == 0:
        print(chr(j), end="")
    else:
        print(chr(j - 32), end="")
