#!/usr/bin/env python

"""

Table Docstring

The Table class represents the control of the
Turing Machine as the entire functional (edge)
relation between some defined present state and
the next target state.

"""

from typing import List
from lib.Head import Head
from lib.State import State
from lib.Controller import Controller
from lib.controllers.table.Edge import Edge

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Table"


class Table(Controller):
	"""
	Table

	Attributes:
		entries (:obj:`List[Edge]`): The list of mappings
			composing the finite state machine's graph.

	TODO:
		* Add add/remove edge function
		* Add sanitization functionality (behavior of the collection entries - e.g. only one root)
		* Add check to make sure that edge is fully defined (source, target, etc.)
		* Table for invalid functions

	"""

	def __init__(self, entries: List[Edge]):
		"""
		Table Constructor.

		:param entries: List[Edge], The list of mappings
			composing the finite state machine's graph.

		"""

		Controller.__init__(self)
		self.entries = entries

	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the table object.

		:return: str

		"""

		rep = "Control Table\n"

		for entry in self.entries:
			rep += str(entry) + "\n"

		return rep

	def run(self, state: State, tape_head: Head) -> State:
		"""
		Run the controller a single iteration with
			the the provided tape and head.

		:param state: State, The current state that
			the tape head is currently located.
		:param tape_head: Head, The machine's tape
			head interface for controlling the TM.
		:return: State

		"""

		raise NotImplementedError

	def get_init_state(self) -> State:
		"""
		Return the initial state of the table's
		transition entries. If no root is specified,
		then the lowest labeled state is selected.

		:return: State

		"""

		root = None

		# move check to entries definition
		for entry in self.entries:
			if entry.source.root:
				if root is None:
					root = entry.source
				elif root != entry.source:
					raise ValueError("Ambiguous Root Definition.")


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
