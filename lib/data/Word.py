#!/usr/bin/env python

"""

Word Docstring

The Word class represents a word in the tape
vocabulary (the domain of what may be written
or present on the tape's domain).

"""

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Word"


class Word(object):
	"""
	Word

	Attributes:
		name (:obj:`str`): The name of the word.

	"""

	def __init__(self, name: str):
		"""
		Word Constructor.

		:param name: The name of the word.

		"""

		self.name = name

	def __eq__(self, other: 'Word') -> bool:
		"""
		Evaluate whether the provided other
		object is equal to this object.

		:param other: Word, Object to compare.
		:return: bool

		"""

		return self.name == other.name

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the word object.

		:return: str

		"""

		return self.name

	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the word object.

		:return: str

		"""

		return self.name

	@property
	def name(self) -> str:
		"""
		:obj:`str` The name of the word.

		Set the word name.

		:raises: ValueError on invalid word
			definition.

		"""

		return self.__name

	@name.setter
	def name(self, name: str) -> None:
		if name is None or len(name) != 1:
			raise ValueError("Invalid Word:", name)

		self.__name = name
