#!/usr/bin/env python

"""

Controller Docstring

The Controller class is an abstract base
class for controlling operations of the
Turing Machine. Generally this is defined
as a table or graph structure.

"""

import abc
from lib.Head import Head

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
	def run(self, tape_head: Head) -> None:
		"""
		Run the controller a single iteration with
			the the provided tape and head.

		:param tape_head: Head, The machine's tape
			head interface for controlling the TM.
		:return: None

		:raises: NotImplementedError

		"""

		raise NotImplementedError
