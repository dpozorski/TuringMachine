#!/usr/bin/env python

"""

Output Docstring

The Output class represents the output state and
action dictated by the controller at a given
time step.

"""

from lib.State import State
from lib.controls.Action import Action
from lib.controllers.binary_table.BinarySequence import BinarySequence

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Output"


class Output(object):
	"""
	Output

	Attributes:
		action (:obj:`Action`): The action executed by the
			Turing Machine on the tape head.
		state (:obj:`State`): The state the machine transitioned
			to following the completion of the action
			and transition from the prior machine state.
		timestep (:obj:`int`): The timestep of the program
			being executed in which the associated output was
			submitted to the Turing Machine.

	"""

	def __init__(self, action: Action, state: State, timestep: int):
		"""
		Output Constructor.

		:param action: Action, The action executed by the
			Turing Machine on the tape head.
		:param state: State, The state the machine transitioned
			to following the completion of the action
			and transition from the prior machine state.
		:param timestep: int, The time step of the program
			being executed in which the associated output was
			submitted to the Turing Machine.

		"""

		self.action = action
		self.state = state
		self.timestep = timestep

	def __eq__(self, other: 'Output') -> bool:
		"""
		Evaluate whether the provided other
		object is equal to this object.

		:param other: Output, Object to compare.
		:return: bool

		"""

		return self.timestep == other.timestep

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the output object.

		:return: str

		"""

		return "{}, {}".format(self.action, self.state)

	def __repr__(self) -> str:
		"""
		Return the string representation of the
		output object.

		:return: str

		"""

		msg = "{}, {}".format(self.action, self.state)
		return "{} (Timestep={})".format(msg, self.timestep)

	def to_binary(self, label_size: int = -1) -> BinarySequence:
		"""
		Convert the output log into a binary sequence.

		:param: label_size, int The size of the label in bits
		:return: BinarySequence

		"""

		state = self.state.to_binary(label_size=label_size)
		output = state.values + self.action.to_binary().values
		return BinarySequence(values=output)

	@property
	def action(self) -> Action:
		"""
		:obj:`Action` The action executed by the
			Turing Machine on the tape head.

		Set the action executed at this time step.

		"""

		return self.__action

	@action.setter
	def action(self, action: Action) -> None:
		self.__action = action

	@property
	def state(self) -> State:
		"""
		:obj:`State` The state the machine transitioned
			to following the completion of the action
			and transition from the prior machine state.

		Set the state.

		"""

		return self.__state

	@state.setter
	def state(self, state: State) -> None:
		self.__state = state

	@property
	def timestep(self) -> int:
		"""
		:obj:`int` The time step of the program being
			executed in which the associated output was
			produced by the Turing Machine's controller.

		Set the time step.

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
