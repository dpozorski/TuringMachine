#!/usr/bin/env python

"""

BinaryTable Docstring

The Table class represents the control of the
Turing Machine as the entire functional (edge)
relation between some defined present state and
the next target state.

TODO:
	* Need to make sure init sequence is added to listing

"""

import math
from typing import Set
from lib.Head import Head
from lib.State import State
from lib.Controller import Controller
from lib.controllers.table.Edge import Edge
from lib.controllers.binary_table.StateSequence import StateSequence
from lib.controllers.binary_table.ControlSequence import ControlSequence

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "BinaryTable"


class BinaryTable(Controller):
	"""
	BinaryTable

	Attributes:
		entries (:obj:`Set[ControlSequence]`): The list of
			control sequences making up the table.

	"""

	def __init__(self, entries: Set[ControlSequence]):
		"""
		BinaryTable Constructor.

		:param entries: Set[ControlSequence], The list of
			control sequences making up the table.

		"""

		Controller.__init__(self)
		entries = {} if entries is None else entries
		self.__entries = set()

		for entry in entries:
			self.add(entry=entry)

	def __len__(self) -> int:
		"""
		Return the number of entries in the table.

		:return: int

		"""

		return 0 if self.entries is None else len(self.entries)

	def __str__(self) -> str:
		"""
		Return the string representation of the binary
		table object.

		:return: str

		"""

		rep = "Binary Control Table\n"

		for entry in self.entries:
			rep += str(entry) + "\n"

		return rep

	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the table object.

		:return: str

		"""

		return self.__str__()

	def is_empty(self) -> bool:
		"""
		Returns whether the binary table is empty.

		:return: bool

		"""

		return self.__len__() == 0

	def add(self, entry: ControlSequence) -> None:
		"""
		Add the provided entry to the table.

		:param entry: ControlSequence, The entry to
			add to the table of control sequences.
		:return: None

		:raises: ValueError If an edge is added
			that leads to an ambiguous init state.

		"""

		if entry not in self.entries:
			if entry.source.root:
				s = self.initial_sequence()

				if s is None or not s.root \
					or s.identity == entry.source.identity:
					self.__entries.add(entry)
				elif s.identity != entry.source.identity:
					msg = "Ambiguous Initial State."
					raise ValueError(msg)
			else:
				self.__entries.add(entry)

	def remove(self, entry: ControlSequence) -> None:
		"""
		Remove the provided control sequence from the table.

		:param entry: ControlSequence, The control sequence
			to remove from the binary table.
		:return: None

		"""

		if entry in self.entries:
			for e in self.entries:
				if e == entry:
					self.entries.remove(entry)
					break

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
			identity = state.label

			for e in self.entries:
				# print(e.source.label, identity, int(r.name), e.condition.to_int())
				if e.source.label == identity and int(r.name) == e.condition.to_int():
					match = e.target.to_state()
					action = e.target.action()
					params = [tape_head.operations, state, match, repr(action), tape_head]
					print("{}. State {}->{}, {}, {}".format(*params))
					action.exec(head=tape_head)
					break

			return match
		else:
			init = self.initial_sequence()
			return None if init is None else init.to_state()

	def initial_sequence(self) -> StateSequence:
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
	def entries(self) -> Set[ControlSequence]:
		"""
		:obj:`Set[ControlSequence]` The list of control
		sequences composing the program.

		Set binary table entries.

		"""

		return self.__entries
