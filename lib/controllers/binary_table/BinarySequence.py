#!/usr/bin/env python

"""

BinarySequence Docstring

The binary sequence object represents a
bit string. This bit string is meant to be
used for representing components of the
control sequence.

"""

import math
from typing import List
from lib.controllers.binary_table.Bit import Bit

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "BinarySequence"


class BinarySequence(object):
	"""
	BinarySequence

	Attributes:
		values (:obj:`List[Bit]`): List of bits in the
			binary sequence.

	"""

	def __init__(self, values: List[Bit] = None):
		"""
		BinarySequence Constructor.

		:param values: List[Bit], List of bits in the
			binary sequence.

		"""

		self.__values = values

	def __len__(self) -> int:
		"""
		Return the length of the binary sequence
		as the number of bits in the sequence.

		:return: int

		"""

		return len(self.values)

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the binary sequence object.

		:return: str

		"""

		return ''.join([i.value for i in self.values])

	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the binary sequence object.

		:return: str

		"""

		return self.__str__()

	def __eq__(self, other: 'BinarySequence') -> bool:
		"""
		Compare whether the two binary sequences
		are the equal.

		:param other: BinarySequence
		:return: bool

		"""

		return self.__str__() == other.__str__()

	def __lt__(self, other: 'BinarySequence') -> bool:
		"""
		Compare whether the the self-referenced
		binary sequence is less than the other
		binary sequence.

		:param other: BinarySequence
		:return: bool

		"""

		return self.__str__() < other.__str__()

	def __hash__(self) -> int:
		"""
		Hash the object for use in inserting
		records in dictionaries.

		:return: int, Hash value

		"""

		return hash(self.__str__())

	def pad(self, padding: int, value: str = "0", left: bool = True) -> None:
		"""
		Pad the sequence.

		:param padding: int, The number of bits to pad.
		:param value: str, The value to pad the sequence.
		:param left: bool, Side to pad the sequence.
		:return: None

		"""

		if value in [Bit.BINARY_LABEL_0, Bit.BINARY_LABEL_1]:
			self.values = self.values if left else reversed(self.values)
			[self.values.insert(0, Bit(value=value)) for _i in range(0, max(0, padding))]
			self.values = self.values if left else reversed(self.values)

	def to_int(self) -> int:
		"""
		Return the value of the binary sequence
		as an integer.

		:return: int

		"""

		int_rep = 0

		for i in reversed(range(0, len(self.values))):
			int_rep += math.pow(2, i) * int(self.values[i].value)

		return int(int_rep)

	@property
	def values(self) -> List[Bit]:
		"""
		:obj:`List[Bit]`

		Set binary sequence values.

		"""

		return self.__values

	@values.setter
	def values(self, values: List[Bit]) -> None:
		self.__values = values if values is not None else []
