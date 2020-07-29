#!/usr/bin/env python

"""

Move Docstring

The Move class represents the move
operation to perform on the tape head.

"""

from lib.Head import Head
from lib.controls.Action import Action
from lib.utilities.FinalProperty import FinalProperty

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
