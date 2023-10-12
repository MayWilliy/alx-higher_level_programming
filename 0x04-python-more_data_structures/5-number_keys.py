#!/usr/bin/pyhton3
def number_keys(a_dictionary):
	"""This function returns the number of keys in a dictionary."""
	number = 0
	list_key = list(a_dictionary.keys())
	for i in list_key:
		number += 1
	return (number)
