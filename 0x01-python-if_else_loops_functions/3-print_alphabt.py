#!/usr/bin/python3
#Lowercase letters (ASCII 97 to 122)
for ascii_value in range (97, 123):
    if ascii_value != 113 and  ascii_value != 101:
    print(chr(ascii_value), end=" ")
