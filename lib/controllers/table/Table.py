#!/usr/bin/env python

"""

Table Docstring

The Table class represents the control of the
Turing Machine as the entire functional (edge)
relation between some defined present state and
the next target state.

"""

import math
import copy
from lib.State import State
from typing import Set, List, Tuple
from lib.controls.Write import Write
from lib.Controller import Controller
from lib.controllers.Input import Input
from lib.controllers.Output import Output
from lib.controllers.table.Edge import Edge
from lib.controllers.table.Word import Word
from lib.controllers.binary_table.Bit import Bit
from lib.controllers.binary_table.BinaryTable import BinaryTable
from lib.controllers.binary_table.StateSequence import StateSequence
from lib.controllers.binary_table.ControlSequence import ControlSequence

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Table"


class Table(Controller):
	"""
	Table

	Attributes:
		entries (:obj:`Set[Edge]`): The list of mappings
			composing the finite state machine's graph.

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

	def __str__(self) -> str:
		"""
		Return the canonical string representation
		of the table object.

		:return: str

		"""

		rep = "Control Table\n"

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

		if edge not in self.entries:
			if edge.source.root:
				s = self.initial_state()

				if s is None or not s.root \
					or s.label == edge.source.label:
					self.__entries.add(edge)
				elif s.label != edge.source.label:
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
			for e in self.entries:
				if input.word == e.condition \
						and e.source == state:
					match = e.target
					action = e.action
					break
		else:
			match = self.initial_state()

		return Output(
			action=action,
			state=match,
			timestep=input.timestep
		)

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

	def indefinite_states(self) -> List[Tuple[State, Word]]:
		"""
		Return a list of indefinite state-input pairs.
		These pairs indicate accessible states within the
		table, but ones that are not defined across all
		potential inputs/transitions. Creates and randomly
		assigns terminal failure nodes to the targets.

		:return: List[Tuple[State, Word]]

		"""

		states = [s.label for s in self.states if not s.terminal]
		vocab = [w.name for w in self.vocab]
		indefinites = list()

		for s in states:
			for w in vocab:
				tmp_s = State(label=s)
				tmp_w = Word(name=w)
				e = Edge(source=tmp_s, condition=tmp_w, target=tmp_s)

				if e not in self.entries:
					indefinites.append((tmp_s, tmp_w))

		return indefinites

	def indefinite_edges(self) -> List[Edge]:
		"""
		Return a list of indefinite edges. With a dummy
		write action (writing the same value as currently)
		on the tape before transitioning to a terminal
		node.

		:return: List[Edge]

		"""

		edges, indefinites = list(), self.indefinite_states()
		labeler = max([s.label for s in self.states])

		for indef in indefinites:
			labeler += 1
			s = State(
				label=labeler,
				terminal=True,
				op_status=1
			)
			edges.append(
				Edge(
					source=indef[0],
					condition=indef[1],
					action=Write(word=indef[1]),
					target=s
				)
			)

		return edges

	def close_domain(self) -> None:
		"""
		Compute the domain's closure and add missing
		elements to the domain. This primarily deals
		with adding all of the indefinite transition
		states to the edge set and terminating them
		with failure nodes.

		:return: None

		"""

		edges = list(self.indefinite_edges())
		edges = list(self.entries) + edges
		self.__entries = set(edges)

	def rebase(self) -> None:
		"""
		Rebasing the table reassigns the state
		labels into a contiguous listing of integer
		labels.

		:return: None

		"""

		states = list()
		[states.append(e.source) for e in self.entries]
		[states.append(e.target) for e in self.entries]
		states = sorted(list(set(states)))
		rebased_edges = list()

		for edge in self.entries:
			n = copy.deepcopy(edge)
			n.source.label = states.index(n.source)
			n.target.label = states.index(n.target)
			rebased_edges.append(n)

		self.__entries = rebased_edges

	def is_binary(self) -> bool:
		"""
		Evaluate whether the current table is a
		binary table (i.e. it only has transition
		conditions and write operations over the
		binary vocabulary {0, 1}).

		:return: bool

		"""

		vocab = [w.name for w in list(self.vocab)]
		return len(vocab) == 2 and Bit.BINARY_LABEL_1 in vocab \
			and Bit.BINARY_LABEL_0 in vocab

	def to_binary(self) -> BinaryTable:
		"""
		Convert the table into a binary table
		controller.

		:return: BinaryTable

		"""

		bits = math.ceil(math.log(len(self.states), 2))
		sources, targets = list(), list()
		controls = list()

		for entry in self.entries:
			targets.append(
				StateSequence(
					identity=entry.target.to_binary(label_size=bits),
					operation=entry.action.to_binary()
				)
			)

		for entry in self.entries:
			found = False
			source = StateSequence(
				identity=entry.source.to_binary(label_size=bits),
				operation=entry.action.to_binary()  # just a placeholder
			)
			condition = entry.condition.to_binary()
			target = StateSequence(
				identity=entry.target.to_binary(label_size=bits),
				operation=entry.action.to_binary()
			)

			for node in targets:
				if node.identity == source.identity:
					found = True
					source.operation = node.operation
					controls.append(
						ControlSequence(
							source=source,
							condition=condition,
							target=target
						)
					)

			if not found and source.root:
				w = Word(name=condition.values[1].value)
				source.operation = Write(word=w).to_binary()
				controls.append(
					ControlSequence(
						source=source,
						condition=condition,
						target=target
					)
				)

		return BinaryTable(entries=set(controls))

	@property
	def entries(self) -> Set[Edge]:
		"""
		:obj:`Set[Edge]` The list of mappings
		composing the finite state machine's graph.

		Set table entries.

		"""

		return self.__entries

	@property
	def states(self) -> Set[State]:
		"""
		:obj:`Set[State]` The set of states that
		are contained within the domain and range
		of the table.

		"""

		states = set()

		for entry in self.entries:
			states.add(entry.source)
			states.add(entry.target)

		return states

	@property
	def vocab(self) -> Set[Word]:
		"""
		:obj:`Set[Word]` The vocabulary of
		words that are conditioned upon for
		transitions. This vocabulary may be
		a subset of the Tape's vocabulary, but
		only trivially so (i.e. in the case where
		the tape includes an unused vocab word).

		"""

		vocab = set()

		for entry in self.entries:
			vocab.add(entry.condition)

			if isinstance(entry.action, Write):
				vocab.add(getattr(entry.action, "word"))

		return vocab
