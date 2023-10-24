#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	""" function that prints x element of a list
	"""
	value = 0
	for j in range(x):
		try:
			print("{}".format(my_list[j]), end="")
			value += 1
		except IndexError:
			break
	print("")
	return (value)



