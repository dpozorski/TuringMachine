#!/usr/bin/env python

"""

Table Docstring

The Table class represents the control of the
Turing Machine as the entire functional (edge)
relation between some defined present state and
the next target state.

"""

from typing import List
from lib.controllers.table.Edge import Edge
from lib.Head import Head
from lib.Controller import Controller

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Table"


class Table(Controller):
	"""
	Table

	Attributes:
		entries (:obj:`List[Edge]`): The list of mappings
			composing the finite state machine's graph.

	"""

	def __init__(self, entries: List[Edge]):
		"""
		Table Constructor.

		:param entries: List[Edge], The list of mappings
			composing the finite state machine's graph.

		"""

		Controller.__init__(self)
		self.entries = entries

	def run(self, tape_head: Head) -> None:
		"""
		Run the controller a single iteration with
			the the provided tape and head.

		:param tape_head: Head, The machine's tape
			head interface for controlling the TM.
		:return: None

		"""

		raise NotImplementedError

	@property
	def entries(self) -> List[Edge]:
		"""
		:obj:`List[Edge]` The list of mappings
		composing the finite state machine's graph.

		Set table entries.

		"""

		return self.__entries

	@entries.setter
	def entries(self, entries: List[Edge]) -> None:
		self.__entries = entries
