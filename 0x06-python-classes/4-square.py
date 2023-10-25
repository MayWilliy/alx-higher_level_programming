#!/usr/bin/python3
"""Write a class Square that defines a square by
"""

""" create class
"""
class Square:
	def __init__(self, size=0):
		self.__size = size
	""" def size(self): to retrieve it
	instance private atrribute
	"""
	def size(self):
		return (self.__size)
	""" property setter def size(self, value): to set it
	raise typeerror and valueerror with message
	instantiation with args
	"""
	def size(self, value):
		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value
	""" public instance method
	"""
	def area(self):
		return (self.__size * self.__size)
