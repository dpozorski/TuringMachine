#!/usr/bin/env python

"""

IOPair Docstring

The IOPair class represents the input-output pair
associated with a given time step.

"""

from lib.controllers.Input import Input
from lib.controllers.Output import Output

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "IOPair"


class IOPair(object):
	"""
	IOPair

	Attributes:
		input (:obj:`Input`): The input data log for a
			given time step of the machine's execution.
		output (:obj:`Output`): The output data log for a
			given time step of the machine's execution.
		label_size (:obj:`int`): The state label size to log
			the IOPair with. Pads the state label if necessary.

	"""

	def __init__(self, input: Input, output: Output, label_size: int = -1):
		"""
		IOPair Constructor.

		:param input: Input, The input data log for a
			given time step of the machine's execution.
		:param output: Output, The output data log for a
			given time step of the machine's execution.
		:param label_size: int, The state label size to log
			the IOPair with. Pads the state label if necessary.

		"""

		self.input = input
		self.output = output
		self.label_size = label_size

	def __lt__(self, other: 'IOPair') -> bool:
		"""
		Compare IO Pairs and see if this IOPair is
		less than the other IOPair.

		:param other: IOPair
		:return: bool

		"""

		pass

	def __eq__(self, other: 'IOPair') -> bool:
		"""
		Evaluate whether the provided other
		object is equal to this object.

		:param other: IOPair, Object to compare.
		:return: bool

		"""

		return self.input == other.input \
			and self.output == other.output

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the input object.

		:return: str

		"""

		return "{},{}".format(
			self.input.to_binary(),
			self.output.to_binary(
				label_size=self.label_size
			)
		)

	def __repr__(self) -> str:
		"""
		Return the string representation of the
		input object.

		:return: str

		"""

		return self.__str__()

	@property
	def input(self) -> Input:
		"""
		:obj:`Input` The input data log for a given
			time step of the machine's execution.

		Set the input word.

		"""

		return self.__input

	@input.setter
	def input(self, input: Input) -> None:
		self.__input = input

	@property
	def output(self) -> Output:
		"""
		:obj:`Output` The output data log for a given
			time step of the machine's execution.

		Set the input word.

		"""

		return self.__output

	@output.setter
	def output(self, output: Output) -> None:
		self.__output = output

	@property
	def label_size(self) -> int:
		"""
		:obj:`int` The state label size to log the
		IOPair with. Pads the state label if necessary.

		Set the label size.

		"""

		return self.__label_size

	@label_size.setter
	def label_size(self, label_size: int) -> None:
		self.__label_size = label_size
