#!/usr/bin/env python

"""

State Docstring

The State class represents a node in the
corresponding finite state machine graph.

"""

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "State"


class State(object):
	"""
	State

	Attributes:
		label (:obj:`int`): The integer label to associate
			with the given node.
		terminal (:obj:`bool`): Flag indicating whether
			the state is procedurally terminal or not.
		op_status (:obj:`int`): Operation status flag
			for indicating whether the given state is
			in a defined (status=0) state or an undefined
			(status=1) state.

	"""

	def __init__(self, label: int, terminal: bool = False, op_status: int = 0):
		"""
		State Constructor.

		:param label: int, The integer label to associate
			with the given node.
		:param terminal: bool, Flag indicating whether
			the state is procedurally terminal or not.
		:param op_status: int, Operation status flag for
			indicating whether the given state is in a defined
			(status=0) state or an undefined (status=1)
			state.

		"""

		self.label = label
		self.terminal = terminal
		self.op_status = op_status

	@property
	def label(self) -> int:
		"""
		:obj:`int` The integer label to associate
		with the given node (i.e. 0 for state 0).

		Set the integer label.

		"""

		return self.__label

	@label.setter
	def label(self, label: int) -> None:
		self.__label = label

	@property
	def terminal(self) -> bool:
		"""
		:obj:`bool` Flag indicating whether the
			state is procedurally terminal or not.

		Set the terminal flag.

		"""

		return self.__terminal

	@terminal.setter
	def terminal(self, terminal: bool) -> None:
		self.__terminal = terminal

	@property
	def op_status(self) -> int:
		"""
		:obj:`int` Operation status flag for indicating
			whether the given state is in a defined
			(status=0) state or an undefined (status=1)
			state.

		Set the op status flag.

		"""

		return self.__op_status

	@op_status.setter
	def op_status(self, op_status: int) -> None:
		self.__op_status = op_status
