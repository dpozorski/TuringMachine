#!/usr/bin/env python

"""

StateSequence Docstring

The state sequence is a defined ordering
of component-level binary sequences. Each
component represents an aspect of a given
state operation.

"""

import math
from typing import List
from lib.State import State
from lib.controls.Move import Move
from lib.controls.Write import Write
from lib.controls.Action import Action
from lib.controllers.table.Word import Word
from lib.controllers.binary_table.Bit import Bit
from lib.utilities.FinalProperty import FinalProperty
from lib.controllers.binary_table.BinarySequence import BinarySequence

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "StateSequence"


class StateSequence(BinarySequence):
	"""
	StateSequence

	Attributes:
		operation (:obj:`BinarySequence`): The binary sequence
			denoting the operation for the nth time step
			(i.e. the control to execute before transitioning
			to the next state).

			00: Move Tape Head Left
			01: Move Tape Head Right
			10: Write 0 to Tape
			11: Write 1 to Tape

		identity (:obj:`BinarySequence`): The binary sequence
			representing the state label for the (n)th time step. This
			sequence is the same as the state label in the table controller.
			Time-step (n). The ending bits of the identity block are
			the termination and termination status bits, respectively. The
			termination status is only considered if termination is true (1).

			-00: Non-terminal State, Proceed w/ Execution
			-01: Non-terminal State, Proceed w/ Execution
			-10: Terminal State, Successful Program Execution
			-11: Terminal State, Unsuccessful/Failed Program Execution

	"""

	"""
	Minimum State Sequence Length.

	"""
	MIN_STATE_SEQUENCE_LEN = FinalProperty[int](6)

	"""
	Operation Sequence Length.

	"""
	OPERATION_SEQUENCE_LEN = FinalProperty[int](2)

	def __init__(self, operation: BinarySequence, identity: BinarySequence):
		"""
		StateSequence Constructor.

		:param operation: BinarySequence, The binary sequence
			denoting the operation for the nth time step
			(i.e. the control to execute before transitioning
			to the next state).

			00: Move Tape Head Left
			01: Move Tape Head Right
			10: Write 0 to Tape
			11: Write 1 to Tape

		:param identity: BinarySequence, The binary sequence
			representing the state label for the (n)th time step. This
			sequence is the same as the state label in the table controller.
			Time-step (n). The ending bits of the identity block are
			the termination and termination status bits, respectively. The
			termination status is only considered if termination is true (1).

			-00: Non-terminal State
			-01: Non-terminal State
			-10: Terminal State, Successful Program Execution
			-11: Terminal State, Unsuccessful/Failed Program Execution

			Additionally, root/initial state status is provided as the
			leading node of the identity sequence:

			0-: Non-initial state
			1-: Initial state

		"""

		BinarySequence.__init__(self)
		self.operation = operation
		self.identity = identity

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
		Return the value of the state sequence
		as an integer.

		:return: int

		"""

		int_rep = self.identity.to_int()
		curr_len = len(self.identity)
		return int_rep + int(self.operation.to_int() * math.pow(2, curr_len))

	def to_state(self) -> State:
		"""
		Convert the state sequence to a state
		object.

		:return: State

		"""

		return State(
			label=self.label,
			root=self.root,
			terminal=self.terminal,
			op_status=self.op_status
		)

	@property
	def operation(self) -> BinarySequence:
		"""
		:obj:`BinarySequence` The one-digit binary sequence
			denoting the operation for the (n-1)th time step
			(i.e. the control to execute before transitioning
			to the specified next state). Time-step (n-1)

			0: Move Tape Head
			1: Write to Tape

		Set binary operation sequence values.

		:raises: ValueError, If the operation sequence
			is not a single bit in length.

		"""

		return self.__operation

	@operation.setter
	def operation(self, operation: BinarySequence) -> None:
		if len(operation) != self.OPERATION_SEQUENCE_LEN:
			raise ValueError("Invalid Operation Bit:", operation)

		self.__operation = operation

	@property
	def identity(self) -> BinarySequence:
		"""
		:obj:`BinarySequence` The binary sequence
			representing the state label for the (n)th time step. This
			sequence is the same as the state label in the table controller.
			Time-step (n). The ending bits of the identity block are
			the termination and termination status bits, respectively. The
			termination status is only considered if termination is true (1).

			-00: Non-terminal State, Proceed w/ Execution
			-01: Non-terminal State, Proceed w/ Execution
			-10: Terminal State, Successful Program Execution
			-11: Terminal State, Unsuccessful/Failed Program Execution

		Set binary identity sequence values.

		"""

		return self.__identity

	@identity.setter
	def identity(self, identity: BinarySequence) -> None:
		self.__identity = identity

	@property
	def terminal(self) -> bool:
		"""
		:obj:`bool` Flag indicating whether the
			state is procedurally terminal or not.

		"""

		return self.values[-4].value == Bit.BINARY_LABEL_1

	@property
	def root(self) -> bool:
		"""
		:obj:`bool` Flag indicating whether the
			state is the graph root/init state.

		"""

		return self.values[0].value == Bit.BINARY_LABEL_1

	@property
	def op_status(self) -> int:
		"""
		:obj:`int` Operation status flag for indicating
			whether the given state is in a defined
			(status=0) state or an undefined (status=1)
			state. This flag is only considered on terminal
			nodes.

		"""

		return int(self.values[-3].value)

	@property
	def values(self) -> List[Bit]:
		"""
		:obj:`List[Bit]` Return the composed listing.

		"""

		return self.identity.values \
			+ self.operation.values

	@property
	def label(self) -> int:
		"""
		:obj:`int` Return state label.

		"""

		bits = [i.value for i in self.identity.values[1:-2]]
		return int(''.join(bits), 2)

	def action(self) -> Action:
		"""
		:obj:`Action` Return the action
		associated with the operation sequence.

		"""

		if self.operation.values[0].value == Bit.BINARY_LABEL_0:
			left = self.operation.values[1].value == Bit.BINARY_LABEL_0
			direction = Move.DIRECTION_LEFT if left else Move.DIRECTION_RIGHT
			return Move(direction=direction)
		else:
			return Write(word=Word(name=self.operation.values[1].value))
