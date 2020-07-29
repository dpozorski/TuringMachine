#!/usr/bin/env python

"""

TuringMachine Docstring

The Turing Machine class represents a revised
implementation of the original Turing Machine.
That is more directly represented in a functional
architecture of a finite state machine (F: N -> N).

TODO:
	* Finish Run Method

"""

from lib.Controller import Controller
from lib.Head import Head

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

	def run(self) -> None:
		"""
		Run the Turing Machine until execution terminates.

		:return: None

		"""

		state = self.controller.initial_state()
		done = True if state is None else False

		while not done:
			state = self.controller.run(
				state=state,
				tape_head=self.tape_head
			)

			if state.terminal:
				break

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
