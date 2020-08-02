#!/usr/bin/env python

"""

ControlSequence Docstring

The control sequence is the analog to the table's
edge class. It represents movement from one
StateSequence to another StateSequence given
some transition condition.

"""

import math
from typing import List
from lib.controllers.binary_table.Bit import Bit
from lib.controllers.binary_table.StateSequence import StateSequence
from lib.controllers.binary_table.BinarySequence import BinarySequence

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "ControlSequence"


class ControlSequence(BinarySequence):
	"""
	ControlSequence

	Attributes:
		source (:obj:`StateSequence`):
		condition (:obj:`BinarySequence`):
		target (:obj:`StateSequence`):

	"""

	def __init__(
			self,
			source: StateSequence,
			condition: BinarySequence,
			target: StateSequence):
		"""
		StateSequence Constructor.

		:param source: StateSequence,
		:param condition: BinarySequence,
		:param target: StateSequence,

		"""

		BinarySequence.__init__(self)
		self.source = source
		self.condition = condition
		self.target = target

	def pad(self, padding: int, value: str = "0", left: bool = True) -> None:
		"""
		Pad the sequence.

		:param padding: int, The number of bits to pad.
		:param value: str, The value to pad the sequence.
		:param left: bool, Side to pad the sequence.
		:return: None

		:raises: Not implemented error. Padding a structured
		sequence poses the risk of corrupting the denoted control.

		"""

		raise NotImplementedError

	def to_int(self) -> int:
		"""
		Return the value of the control sequence
		as an integer.

		:return: int

		"""

		int_rep = self.target.to_int()
		curr_len = len(self.target)
		int_rep += (self.condition.to_int() * math.pow(2, curr_len))
		curr_len = len(self.condition)
		int_rep += (self.source.to_int() * math.pow(2, curr_len))
		return int_rep

	@property
	def source(self) -> StateSequence:
		"""
		:obj:`StateSequence`

		Set termination bit.

		:raises: ValueError, If the source state sequence is None
			or its size is less than the min size of a state
			sequence (6 bits).

		"""

		return self.__source

	@source.setter
	def source(self, source: StateSequence) -> None:
		if source is None or len(source) < StateSequence.MIN_STATE_SEQUENCE_LEN:
			raise ValueError("Invalid Source Sequence:", source)

		self.__source = source

	@property
	def condition(self) -> BinarySequence:
		"""
		:obj:`BinarySequence` The value from the tape head
		that must be read for the transition from the source
		sequence to the target sequence.

		Set condition bit.

		:raises: ValueError, If the condition sequence is not
			a single bit in length. The condition represents
			the input from the tape head reading the tape.

		"""

		return self.__condition

	@condition.setter
	def condition(self, condition: BinarySequence) -> None:
		if len(condition) != 1:
			raise ValueError("Invalid Condition Bit:", condition)

		self.__condition = condition

	@property
	def target(self) -> StateSequence:
		"""
		:obj:`StateSequence` The target sequence to transition
			to from the source sequence provided the condition
			bit matches the tape head's reading.

		Set target sequence.

		:raises: ValueError, If the target state sequence is None
			or its size is less than the min size of a state
			sequence (6 bits).

		"""

		return self.__target

	@target.setter
	def target(self, target: StateSequence) -> None:
		if target is None or len(target) < StateSequence.MIN_STATE_SEQUENCE_LEN:
			raise ValueError("Invalid Target Sequence:", target)

		self.__target = target

	@property
	def values(self) -> List[Bit]:
		"""
		:obj:`List[Bit]` Return the composed listing.

		"""

		return self.source.values \
			+ self.condition.values \
			+ self.target.values
