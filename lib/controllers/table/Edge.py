#!/usr/bin/env python

"""

Edge Docstring

The Edge class represents the transition
condition and action to perform between
nodes in the finite state machine graph.

"""

from lib.State import State
from lib.data.Word import Word
from lib.controls.Action import Action

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Edge"


class Edge(object):
	"""
	Edge

	Attributes:
		condition (:obj:`Word`): The edge condition
			indicating the necessary matching word
			for this transition to be made.
		action (:obj:`Action`): The action to identify
			with and perform at this state transition.
		source (:obj:`State`): The edge source node.
		target (:obj:`State`): The edge target node.

	"""

	def __init__(self, condition: Word, action: Action, source: State, target: State):
		"""
		Edge Constructor.

		:param condition: Word, The edge condition
			indicating the necessary matching word
			for this transition to be made.
		:param action: Action, The action to identify
			with and perform at this state transition.
		:param source: State, The edge source node.
		:param target: State, The edge target node.

		"""

		self.condition = condition
		self.action = action
		self.source = source
		self.target = target

	def __eq__(self, other: 'Edge') -> bool:
		"""
		Evaluate whether the provided edge is
		equal to current (self-referenced) edge.

		The source and condition define the entire
		transition state. It is an undefined function
		if there is more than one edge with the same
		source state and transition condition.

		:param other: Edge, The edge to compare to.
		:return: bool

		"""

		return self.source == other.source \
			and self.condition == other.condition

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the move action object.

		:return: str

		"""

		return " ".join([
			repr(self.source),
			str(self.condition),
			str(self.action),
			repr(self.target)
		])

	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the move action object.

		:return: str

		"""

		return self.__str__()

	@property
	def action(self) -> Action:
		"""
		:obj:`Action` The action to identify with
		and perform at this state transition.

		Set the edge action.

		"""

		return self.__action

	@action.setter
	def action(self, action: Action) -> None:
		self.__action = action

	@property
	def condition(self) -> Word:
		"""
		:obj:`Word` The edge condition indicating
			the necessary matching word for this
			transition to be made.

		Set the edge condition.

		:raises: ValueError if transition condition is None.

		"""

		return self.__condition

	@condition.setter
	def condition(self, condition: Word) -> None:
		if condition is None:
			raise ValueError("No Transition Condition Specified.")

		self.__condition = condition

	@property
	def source(self) -> State:
		"""
		:obj:`State` The edge source node.

		Set edge's source node.

		:raises: ValueError if source state is None.

		"""

		return self.__source

	@source.setter
	def source(self, source: State) -> None:
		if source is None:
			raise ValueError("No Source State Specified.")

		self.__source = source

	@property
	def target(self) -> State:
		"""
		:obj:`State` The edge target node.

		Set edge's target node.

		:raises: ValueError if target state is None.

		"""

		return self.__target

	@target.setter
	def target(self, target: State) -> None:
		if target is None:
			raise ValueError("No Target State Specified.")

		self.__target = target
