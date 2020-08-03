#!/usr/bin/env python

"""

Controller Docstring

The Controller class is an abstract base
class for controlling operations of the
Turing Machine. Generally this is defined
as a table or graph structure.

"""

import abc
from lib.State import State
from lib.controllers.Input import Input
from lib.controllers.Output import Output

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Controller"


class Controller(abc.ABC):
	"""
	Controller

	Attributes:


	"""

	def __init__(self):
		"""
		Controller Constructor.

		"""

		pass

	@abc.abstractmethod
	def next(self, state: State, input: Input) -> Output:
		"""
		From the specified input, compute the transition
		action and the next graph state.

		:param state: State, The current state that
			the tape head is currently located.
		:param input: Input, The current word
			being read by the print head on the TM.
		:return: Output

		:raises: NotImplementedError

		"""

		raise NotImplementedError
