#!/usr/bin/python3
"""function that prints the first x elements of a list and only integers.
"""
def safe_print_list_integers(my_list=[], x=0):
	value = 0
	for j in range(0, x):
		try:
			value += 1
			print("{:d}".format(my_list[j]), end="")
		except (ValueError, TypeError):
			continue
	print("")
	return (value)
