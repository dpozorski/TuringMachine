#!/usr/bin/env python

"""

Table Docstring

The Table class represents the control of the
Turing Machine as the entire functional (edge)
relation between some defined present state and
the next target state.

"""

from typing import Set
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
		* Table for invalid functions?

	"""

	def __init__(self, entries: Set[Edge]):
		"""
		Table Constructor.

		:param entries: Set[Edge], The set of mappings
			composing the finite state machine's graph.

		"""

		Controller.__init__(self)
		entries = {} if entries is None else entries
		self.__entries = set()

		for entry in entries:
			self.add(edge=entry)

	def __len__(self) -> int:
		"""
		Return the number of entries that
		are in the table.

		:return: int

		"""

		return 0 if self.entries is None else len(self.entries)

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

	def is_empty(self) -> bool:
		"""
		Returns whether the table is empty
		of transition records.

		:return: bool

		"""

		return self.__len__() == 0

	def add(self, edge: Edge) -> None:
		"""
		Add the provided edge to the table.

		:param edge: Edge, The edge to add.
		:return: None

		:raises: ValueError If an edge is added
			that leads to an ambiguous init state.

		"""

		if not self.__contains__(item=edge):
			if edge.source.root:
				s = self.initial_state()

				if s.label != edge.source.label:
					if s is None or not s.root:
						self.__entries.add(edge)
					else:
						msg = "Ambiguous Initial State."
						raise ValueError(msg)
			else:
				self.__entries.add(edge)

	def remove(self, edge: Edge) -> None:
		"""
		Remove the provided edge from the table.

		:param edge: Edge, The edge to remove.
		:return: None

		"""

		if edge is not None:
			for entry in self.entries:
				if entry == edge:
					self.entries.remove(edge)
					break

	def __contains__(self, item: Edge) -> bool:
		"""
		Evaluate whether the table contains the
		specified edge.

		:param item: Edge, The edge to search for.
		:return: bool

		"""

		if item is not None:
			for entry in self.entries:
				if entry == item:
					return True

		return False

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

		if state is not None:
			match = None
			r = tape_head.read()

			for e in self.entries:
				if e.source == state and r == e.condition:
					match = e.target
					params = [tape_head.operations, state, match, repr(e.action), tape_head]
					print("{}. State {}->{}, {}, {}".format(*params))
					e.action.exec(head=tape_head)
					break

			return match
		else:
			return self.initial_state()

	def initial_state(self) -> State:
		"""
		Return the initial state of the table's
		transition entries. If no root is specified,
		then the lowest labeled state is selected.

		:return: State

		"""

		root, lowest = None, None

		for entry in self.entries:
			if entry.source.root:
				return entry.source
			elif lowest is None or lowest.label > entry.source.label:
				lowest = entry.source

		return lowest

	@property
	def entries(self) -> Set[Edge]:
		"""
		:obj:`Set[Edge]` The list of mappings
		composing the finite state machine's graph.

		Set table entries.

		"""

		return self.__entries
