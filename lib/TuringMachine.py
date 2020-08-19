#!/usr/bin/env python

"""

TuringMachine Docstring

The Turing Machine class represents a revised
implementation of the original Turing Machine.
That is more directly represented in a functional
architecture of a finite state machine (F: N -> N).

"""

from lib.Head import Head
from lib.State import State
from lib.Controller import Controller
from lib.controllers.Input import Input
from lib.controllers.IOPair import IOPair
from lib.data.log.MachineLog import MachineLog

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "TuringMachine"


class TuringMachine(object):
	"""
	TuringMachine

	Attributes:
		controller (:obj:`Controller`):
		tape_head (:obj:`Head`):

	"""

	def __init__(self, controller: Controller, tape_head: Head):
		"""
		TuringMachine Constructor.

		:param controller: Controller, object tasked
			with orchestrating the TM's behavior.
		:param tape_head: Head, interface used for
			executing control behaviors on the TM's
			memory (Tape).

		"""

		self.controller = controller
		self.tape_head = tape_head
		self.__log = MachineLog()

	def run(self) -> None:
		"""
		Run the Turing Machine until execution terminates.

		:return: None

		"""

		self.log.clear()
		done, old_state = False, None
		timestep = 0

		while not done:
			done = True
			input = Input(
				word=self.tape_head.read(),
				timestep=timestep
			)
			output = self.controller.next(
				state=old_state,
				input=input
			)
			action, new_state = output.action, output.state

			if new_state is not None:
				if action is not None:
					params = [self.tape_head.operations, old_state, new_state, repr(action), self.tape_head]
					print("{}. State {}->{}, {}, {}".format(*params))
					action.exec(head=self.tape_head)
					self.log.log(record=IOPair(input=input, output=output))

				old_state = new_state

			if new_state is None or (new_state.terminal and new_state.op_status == State.FAILURE):
				print("\033[91mProgram Terminated Unsuccessfully.\033[0m")
			elif new_state.terminal and new_state.op_status == State.SUCCESS:
				print("\033[92mProgram Terminated Successfully.\033[0m")
			else:
				done = False

			timestep += 1

	@property
	def controller(self) -> Controller:
		"""
		:obj:`Controller` The object tasked with
			orchestrating the TM's behavior.

		Set the controller.

		"""

		return self.__controller

	@controller.setter
	def controller(self, controller: Controller) -> None:
		self.__controller = controller

	@property
	def tape_head(self) -> Head:
		"""
		:obj:`Head` The interface used for executing
			control behaviors on the TM's memory (Tape).

		Set the tape head.

		"""

		return self.__tape_head

	@tape_head.setter
	def tape_head(self, tape_head: Head) -> None:
		self.__tape_head = tape_head

	@property
	def log(self) -> MachineLog:
		"""
		:obj:`MachineLog` The Turing Machine's
			execution log.

		"""

		return self.__log
