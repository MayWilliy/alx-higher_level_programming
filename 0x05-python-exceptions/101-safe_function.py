#!/usr/bin/python3
import sys
"""function that executes a function safely
"""
def safe_function(fct, *args):
	try:
		result = fct(*arg)
		return (result)
	except:
		print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
		return (None)
