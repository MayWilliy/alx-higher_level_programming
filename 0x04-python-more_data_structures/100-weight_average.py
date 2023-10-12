#!/bin/usr/python3
def weight_average(my_list=[]):
	"""This function returns the weighted average 
	of all integers tuple (<score>, <weight>)."""
	if not my_list:
		return 0
	score = 0
	weight = 0
	for tuple in my_list:
		score += tuple[0] * tuple[1]
		weight += tuple[1]
	return (score / weight)
