#!/usr/bin/env python

"""

Bit Docstring

The bit object is just an enumerated
class for representing "bit" literals
in the vocabulary.

"""

from lib.utilities.FinalProperty import FinalProperty

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Bit"


class Bit(object):
	"""
	Bit

	Attributes:
		value (:obj:`str`): The bit's value.

	"""

	"""
	Binary label 0.

	"""
	BINARY_LABEL_0 = FinalProperty[str]("0")

	"""
	Binary label 1.

	"""
	BINARY_LABEL_1 = FinalProperty[str]("1")

	def __init__(self, value: str):
		"""
		Bit Constructor.

		:param value: str, The bit's value.

		"""

		self.value = value

	@property
	def value(self) -> str:
		"""
		:obj:`str` The bit's value.

		Set the bit's value.

		:raises: ValueError if the value is not
			a valid binary character.

		"""

		return self.__value

	@value.setter
	def value(self, value: str) -> None:
		if value != self.BINARY_LABEL_0 and value != self.BINARY_LABEL_1:
			raise ValueError("Invalid bit value provided:", value)

		self.__value = value
