#!/usr/bin/env python

"""

Action Docstring

The Action class represents the action
the machine should perform on the tape
in a given transition state.

"""

import abc
from typing import Any
from lib.Head import Head
from lib.controllers.binary_table.BinarySequence import BinarySequence

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Action"


class Action(abc.ABC):
	"""
	Action

	Attributes:


	"""

	def __init__(self):
		"""
		Action Constructor.

		"""

		pass

	@abc.abstractmethod
	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the object.

		:return: str

		"""

		raise NotImplementedError

	@abc.abstractmethod
	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the object.

		:return: str

		"""

		raise NotImplementedError

	@abc.abstractmethod
	def exec(self, head: Head) -> Any:
		"""
		Execute the provided action.

		:param head: Head, The tape head object
			interfacing with the machine's tape.
		:return: Any

		"""

		raise NotImplementedError

	@abc.abstractmethod
	def to_binary(self) -> BinarySequence:
		"""
		Convert the action into a binary sequence.

		:return: BinarySequence

		"""

		raise NotImplementedError
