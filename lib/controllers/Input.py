#!/usr/bin/env python

"""

Input Docstring

The Input class represents the input word at a
given time-step of the machine's execution.

"""

from lib.controllers.table.Word import Word
from lib.controllers.binary_table.BinarySequence import BinarySequence

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Input"


class Input(object):
	"""
	Input

	Attributes:
		word (:obj:`Word`): The input to the Turing
			Machine associated with the paired time step.
		timestep (:obj:`int`): The timestep of the program
			being executed in which the associated input was
			submitted to the Turing Machine.

	"""

	def __init__(self, word: Word, timestep: int):
		"""
		Input Constructor.

		:param word: Word, The input to the Turing
			Machine associated with the paired time step.
		:param timestep: int, The timestep of the program
			being executed in which the associated input was
			submitted to the Turing Machine.

		"""

		self.word = word
		self.timestep = timestep

	def __eq__(self, other: 'Input') -> bool:
		"""
		Evaluate whether the provided other
		object is equal to this object.

		:param other: Input, Object to compare.
		:return: bool

		"""

		return self.timestep == other.timestep \
			and self.word == other.word

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the input object.

		:return: str

		"""

		return str(self.word)

	def __repr__(self) -> str:
		"""
		Return the string representation of the
		input object.

		:return: str

		"""

		params = [self.word.name, self.timestep]
		return "{} (Timestep={})".format(*params)

	def to_binary(self) -> BinarySequence:
		"""
		Convert the input log into a binary sequence.

		:return: BinarySequence

		"""

		return self.word.to_binary()

	@property
	def word(self) -> Word:
		"""
		:obj:`Word` The input to the Turing Machine
			associated with the paired time step.

		Set the input word.

		"""

		return self.__word

	@word.setter
	def word(self, word: Word) -> None:
		self.__word = word

	@property
	def timestep(self) -> int:
		"""
		:obj:`int` The timestep of the program being
			executed in which the associated input was
			submitted to the Turing Machine.

		Set the timestep.

		:raises: ValueError, If the submitted time step
			is less than 0.

		"""

		return self.__timestep

	@timestep.setter
	def timestep(self, timestep: int) -> None:
		if timestep < 0:
			msg = "Invalid Timestep: {}"
			raise ValueError(msg.format(timestep))

		self.__timestep = timestep
