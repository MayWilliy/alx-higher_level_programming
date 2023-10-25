#!/usr/bin/python3
"""Write a class Square that defines a square
"""

""" class
"""
class Square:
	""" private instance attribution
	"""
	def __init__(self, size=0):
		""" isinstantiation wirh arg int
		"""
		if not isinstance(size, int):
			""" raise typeerror and valueerror with message
			"""
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size
	""" definition area
	"""
	def area(self):
		return (self.__size * self.__size)
