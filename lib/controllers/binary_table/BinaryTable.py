#!/usr/bin/env python

"""

BinaryTable Docstring

The Table class represents the control of the
Turing Machine as the entire functional (edge)
relation between some defined present state and
the next target state.

"""

import copy
from lib.State import State
from typing import Set, List, Tuple
from lib.controls.Write import Write
from lib.Controller import Controller
from lib.controllers.Input import Input
from lib.controllers.Output import Output
from lib.controllers.table.Word import Word
from lib.controllers.binary_table.Bit import Bit
from lib.controllers.binary_table.StateSequence import StateSequence
from lib.controllers.binary_table.BinarySequence import BinarySequence
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
			that leads to an ambiguous init state or
			if a control sequence is added that is not
			the same size as the rest of the control
			sequences.

		"""

		if entry not in self.entries:
			if len(self.entries) > 0 and len(entry) != len(list(self.entries)[0]):
				raise ValueError("Control Sequence of Different Lengths")

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

	def next(self, state: State, input: Input) -> Output:
		"""
		From the specified input, compute the transition
		action and the next graph state.

		:param state: State, The current state that
			the tape head is currently located.
		:param input: Input, The current word
			being read by the print head on the TM.
		:return: Output

		"""

		action, match = None, None

		if state is not None:
			identity = state.label

			for e in self.entries:
				if input.word.name == str(e.condition.to_int()) \
						and e.source.label == identity:
					match = e.target.to_state()
					action = e.target.action()
					break
		else:
			init = self.initial_sequence()
			match = None if init is None else init.to_state()

		return Output(
			action=action,
			state=match,
			timestep=input.timestep
		)

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

	def indefinite_states(self) -> List[Tuple[StateSequence, Bit]]:
		"""
		Return a list of the undefined control sequences.
		Undefined, here, means that it is a control sequence
		with a valid source state sequence which does not
		have coverage over all possible transition conditions.

		:return: List[State]

		"""

		states = list()
		pairs = [(entry.source.label, entry.condition.values[0].value) for entry in self.entries]

		for entry in self.entries:
			for condition in [Bit.BINARY_LABEL_0, Bit.BINARY_LABEL_1]:
				if (entry.source.label, condition) not in pairs:
					states.append((entry.source, Bit(value=condition)))

		return states

	def indefinite_sequences(self) -> List[ControlSequence]:
		"""
		Return a list of indefinite control sequences. With
		a dummy write action (writing the same value as currently)
		on the tape before transitioning to a terminal
		node.

		:return: List[ControlSequence]

		"""

		sequences, exceptions = list(), list()
		indefinites = self.indefinite_states()
		bits = len(list(self.entries)[0].source.identity) \
			- (StateSequence.MIN_STATE_SEQUENCE_LEN - 3)
		labeler = -1

		for e in self.entries:
			labeler = max(labeler, e.source.label, e.target.label)

		for indef in indefinites:
			labeler += 1
			sequences.append(
				ControlSequence(
					source=indef[0],
					condition=BinarySequence(values=[indef[1]]),
					target=StateSequence(
						identity=State(
							label=labeler,
							terminal=True,
							op_status=State.FAILURE
						).to_binary(label_size=bits),
						operation=Write(word=Word(name=indef[1].value)).to_binary()
					)
				)
			)

		return sequences

	def close_domain(self) -> None:
		"""
		Compute the domain's closure and add missing
		control sequences to the domain. This primarily
		deals with adding all of the indefinite control
		sequences to the control set and terminating them
		with failure nodes.

		:return: None

		"""

		sequences = list(self.indefinite_sequences())
		sequences = list(self.entries) + sequences
		self.__entries = set(sequences)

	def rebase(self) -> None:
		"""
		Rebasing the table reassigns the state
		labels into a contiguous listing of integer
		labels.

		:return: None

		"""

		states, rebased_seqs = list(), list()

		for entry in self.entries:
			states.append(entry.source.identity)
			states.append(entry.target.identity)

		states = sorted(list(set(states)))
		bits = len(list(self.entries)[0].source.identity) \
			- (StateSequence.MIN_STATE_SEQUENCE_LEN - 3) \
			if len(self.entries) > 0 else 0
		converter = '{0:0' + str(bits) + 'b}'

		for entry in self.entries:
			n = copy.deepcopy(entry)
			ident = converter.format(states.index(n.source.identity))
			values = [n.source.identity.values[0]] + [Bit(value=c) for c in ident] + n.source.identity.values[-2:]
			n.source.identity = BinarySequence(values=values)
			ident = converter.format(states.index(n.target.identity))
			values = [n.target.identity.values[0]] + [Bit(value=c) for c in ident] + n.target.identity.values[-2:]
			n.target.identity = BinarySequence(values=values)
			rebased_seqs.append(n)

		self.__entries = rebased_seqs

	@property
	def entries(self) -> Set[ControlSequence]:
		"""
		:obj:`Set[ControlSequence]` The list of control
		sequences composing the program.

		Set binary table entries.

		"""

		return self.__entries
