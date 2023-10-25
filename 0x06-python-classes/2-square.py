#!/usr/bin/python3
"""Write a class Square that defines a square by: 
(based on 1-square.py)
Private instance attribute: size
"""
class Square:
	def __init__(self, size=0):
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueErrorprint("size must be >= 0")
		self.___size = size
