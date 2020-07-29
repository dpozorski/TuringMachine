#!/usr/bin/env python

"""

Vocabulary Docstring

The Vocabulary class represents a collection
of words that should be considered as the domain
of words that may be written to or present on
the machine's tape.

"""

from lib.data.Word import Word
from typing import Set

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Vocabulary"


class Vocabulary(object):
	"""
	Vocabulary

	Attributes:
		words (:obj:`Set[Word]`): The set of words
			in the tape's vocabulary.

	"""

	def __init__(self, words: Set[Word]):
		"""
		Vocabulary Constructor.

		:param words: The set of words in
			the tape's vocabulary.

		"""

		self.words = words

	def __len__(self) -> int:
		"""
		Return the size of the vocabulary.

		:return: int

		"""

		return len(self.words)

	def __contains__(self, item: Word) -> bool:
		"""
		Examine whether the vocabulary contains
		the specified word.

		:param item: Word, Value to search for.
		:return: bool

		"""

		return item in self.words

	def __add__(self, other: Word) -> None:
		"""
		Add the specified word to the vocabulary
		if it is not already present.

		:param other: Word, The word to add to
			the vocabulary.
		:return: None

		"""

		if not self.__contains__(item=other):
			self.words.add(element=other)

	def __delitem__(self, key: str):
		"""
		Remove the specified word to the vocabulary
		if it exists in the vocabulary.

		:param key: str, The name of the word to
			remove from the vocabulary.
		:return: None

		"""

		if self.__contains__(item=Word(name=key)):
			self.words.remove(Word(name=key))

	@property
	def words(self) -> Set[Word]:
		"""
		:obj:`Set[Word]` The tape vocabulary.

		Set the vocabulary..

		:raises: ValueError if an empty vocabulary
			is attempted to be set.

		"""

		return self.__words

	@words.setter
	def words(self, words: Set[Word]) -> None:
		if words is None or len(words) == 0:
			raise ValueError("Empty Vocabulary Provided.")

		self.__words = words
