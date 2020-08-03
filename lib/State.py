#!/usr/bin/env python

"""

State Docstring

The State class represents a node in the
corresponding finite state machine graph.

"""

import math
from lib.controllers.binary_table.Bit import Bit
from lib.utilities.FinalProperty import FinalProperty
from lib.controllers.binary_table.BinarySequence import BinarySequence

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
		root (:obj:`bool`): Flag indicating whether the
			state is the graph root/init state.
		op_status (:obj:`int`): Operation status flag
			for indicating whether the given state is
			in a defined (status=0) state or an undefined
			(status=1) state.

	"""

	"""
	The class constant for designating failure. This
	flag is only considered on terminal nodes.

	"""
	FAILURE = FinalProperty[int](1)

	"""
	The class constant for designating success. This
	flag is only considered on terminal nodes.

	"""
	SUCCESS = FinalProperty[int](0)

	def __init__(self, label: int, terminal: bool = False, root: bool = False, op_status: int = 0):
		"""
		State Constructor.

		:param label: int, The integer label to associate
			with the given node.
		:param terminal: bool, Flag indicating whether
			the state is procedurally terminal or not.
		:param root: bool, Flag indicating whether the
			state is the graph root/init state.
		:param op_status: int, Operation status flag for
			indicating whether the given state is in a defined
			(status=0) state or an undefined (status=1)
			state.

		"""

		self.label = label
		self.terminal = terminal
		self.root = root
		self.op_status = op_status

	def __eq__(self, other: 'State') -> bool:
		"""
		Evaluate whether the provided other
		object is equal to this object.

		:param other: State, Object to compare.
		:return: bool

		"""

		return self.label == other.label

	def __lt__(self, other: 'State') -> bool:
		"""
		Compare whether the present state is less
		than the other state provided.

		:param other: State
		:return: bool

		"""

		return self.label < other.label

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the state object.

		:return: str

		"""

		return str(self.label)

	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the state object.

		:return: str

		"""

		return "q" + str(self.label)

	def __hash__(self) -> int:
		"""
		Hash the object for use in inserting
		records in dictionaries.

		:return: int, Hash value

		"""

		return hash(self.__repr__())

	def to_binary(self, label_size: int = -1) -> BinarySequence:
		"""
		Convert the state into a binary sequence.

		:param label_size: int, The size (in bits) that
			the label should be formatted.
		:return: BinarySequence

		:raises: ValueError, If the number of bits would result
			in an overflow (this covers negative/zero sizes too)

		"""

		bs = BinarySequence(values=[])
		bits = 1 if self.label == 0 else math.ceil(math.log(self.label, 2))
		label_size = bits if label_size < 1 else label_size

		if label_size < bits:
			msg = "Overflow Invalid Label Size (bits): {}"
			raise ValueError(msg.format(bits))

		converter = '{0:0' + str(label_size) + 'b}'
		bitstr = converter.format(self.label)
		bitstr = bitstr + Bit.BINARY_LABEL_1 if self.terminal else bitstr + Bit.BINARY_LABEL_0
		bitstr = bitstr + Bit.BINARY_LABEL_1 if self.op_status == self.FAILURE else bitstr + Bit.BINARY_LABEL_0
		bitstr = Bit.BINARY_LABEL_1 + bitstr if self.root else Bit.BINARY_LABEL_0 + bitstr

		for char in bitstr:
			bs.values.append(Bit(value=char))

		return bs

	@property
	def label(self) -> int:
		"""
		:obj:`int` The integer label to associate
		with the given node (i.e. 0 for state 0).

		Set the integer label.

		:raises: ValueError if label is <= 0.

		"""

		return self.__label

	@label.setter
	def label(self, label: int) -> None:
		if label < 0:
			raise ValueError("State Label Must be >= 0.")

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
	def root(self) -> bool:
		"""
		:obj:`bool` Flag indicating whether the
			state is the graph root/init state.

		Set the root flag.

		"""

		return self.__root

	@root.setter
	def root(self, root: bool) -> None:
		self.__root = root

	@property
	def op_status(self) -> int:
		"""
		:obj:`int` Operation status flag for indicating
			whether the given state is in a defined
			(status=0) state or an undefined (status=1)
			state. This flag is only considered on terminal
			nodes.

		Set the op status flag.

		:raises: ValueError, if an invalid op status is
			provided to the attribute setter.

		"""

		return self.__op_status

	@op_status.setter
	def op_status(self, op_status: int) -> None:
		if op_status not in [self.SUCCESS, self.FAILURE]:
			raise ValueError("Invalid Operation Status:", op_status)

		self.__op_status = op_status
