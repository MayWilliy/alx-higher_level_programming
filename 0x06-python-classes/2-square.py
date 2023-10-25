#!/usr/bin/python3
"""Write a class Square that defines a square by: 
(based on 1-square.py)
"""

""" class
"""
class Square:
	def __init__(self, size=0):
	""" Private instance attribute: size
	"""
		if not isinstance(size, int):
		""" instantiation with value and type veri
		"""
			raise TypeError("size must be an integer")
			""" riase typeerror with message
			"""
		elif size < 0:
		""" else if condition that check if size is less than 0
		"""
			raise ValueErrorprint("size must be >= 0")
			""" riase valueerroe with message
			"""
		self.___size = size
