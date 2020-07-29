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

		"""

		return self.__condition

	@condition.setter
	def condition(self, condition: Word) -> None:
		self.__condition = condition

	@property
	def source(self) -> State:
		"""
		:obj:`State` The edge source node.

		Set edge's source node.

		"""

		return self.__source

	@source.setter
	def source(self, source: State) -> None:
		self.__source = source

	@property
	def target(self) -> State:
		"""
		:obj:`State` The edge target node.

		Set edge's target node.

		"""

		return self.__target

	@target.setter
	def target(self, target: State) -> None:
		self.__target = target
