#!/usr/bin/env python

"""

Move Docstring

The Move class represents the move
operation to perform on the tape head.

"""

from lib.Head import Head
from lib.controls.Action import Action
from lib.controllers.binary_table.Bit import Bit
from lib.utilities.FinalProperty import FinalProperty
from lib.controllers.binary_table.BinarySequence import BinarySequence

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Move"


class Move(Action):
	"""
	Move

	Attributes:
		direction (:obj:`str`): The direction to move
			the type head on the machine's tape.

	"""

	"""
	Operation Code.

	"""
	OP_CODE = FinalProperty[str]("0")

	"""
	The class constant for moving left.
	
	"""
	DIRECTION_LEFT = FinalProperty[str]("L")

	"""
	The class constant for moving right.

	"""
	DIRECTION_RIGHT = FinalProperty[str]("R")

	def __init__(self, direction: str):
		"""
		Move Constructor.

		:param direction: str, The direction to move
			the type head on the machine's tape.

		"""

		Action.__init__(self)
		self.direction = direction

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the move action object.

		:return: str

		"""

		return self.direction

	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the move action object.

		:return: str

		"""

		msg = "Move Head (direction={})"
		return msg.format(self.direction)

	def exec(self, head: Head) -> None:
		"""
		Execute the move operation.

		:param head: Head, The tape head object
			interfacing with the machine's tape.
		:return: None

		"""

		if self.direction == Move.DIRECTION_LEFT:
			head.left()
		else:
			head.right()

	def to_binary(self) -> BinarySequence:
		"""
		Convert the write action into a binary sequence.

		:return: BinarySequence

		"""

		param_code = Bit.BINARY_LABEL_1

		if self.direction == self.DIRECTION_LEFT:
			param_code = Bit.BINARY_LABEL_0

		return BinarySequence(values=[
			Bit(value=self.OP_CODE),
			Bit(value=param_code)
		])

	@property
	def direction(self) -> str:
		"""
		:obj:`str` The direction to move the
			type head on the machine's tape.

		Set the direction to move the type head.

		:raises: ValueError, If invalid direction
			is supplied to the setter.

		"""

		return self.__direction

	@direction.setter
	def direction(self, direction: str) -> None:
		direction = '' if direction is None else direction
		direction = direction.upper().strip()

		if direction not in [Move.DIRECTION_LEFT, Move.DIRECTION_RIGHT]:
			raise ValueError("Invalid Direction Entered")

		self.__direction = direction
