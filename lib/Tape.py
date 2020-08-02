#!/usr/bin/env python

"""

Tape Docstring

The Tape class represents the infinite input
tape for the Turing Machine.

"""

from typing import List
from lib.controllers.table.Word import Word
from lib.controllers.table.Vocabulary import Vocabulary

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Tape"


class Tape(object):
	"""
	Tape

	Attributes:
		vocab (:obj:`Vocabulary`): The vocabulary
			defines the valid characters that may be
			written to the tape.
		data (:obj:`List[Word]`): The data is the entire
			tape state as a (finite) array of what has
			been "seen" by th user or provided as input
			to the machine. However, the tape head is able
			to expand the tape's visible section indefinitely.
		default (:obj:`Word`): The default character to
			assign to newly visible space on the tape.
			Canonically this value is taken to be 'B'
			for a blank positional tape state.

	"""

	def __init__(self, vocab: Vocabulary, data: List[Word], default: Word):
		"""
		Tape Constructor.

		:param vocab: Vocabulary, The vocabulary
			defines the valid characters that may be
			written to the tape.
		:param data: List[Word], The data is the entire
			tape state as a (finite) array of what has
			been "seen" by th user or provided as input
			to the machine. However, the tape head is able
			to expand the tape's visible section indefinitely.
		:param default: Word, The default character to
			assign to newly visible space on the tape.
			Canonically this value is taken to be 'B'
			for a blank positional tape state.

		"""

		self.__vocab = vocab
		self.default = default
		self.__data = [] if data is None else data

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the tape object.

		:return: str

		"""

		return str(self.data)

	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the tape object.

		:return: str

		"""

		return str(self.data)

	def __len__(self) -> int:
		"""
		Return the length of the tape's visible
		or traversed section of the indefinitely
		defined machine tape.

		:return: int, The tape's length

		"""

		return len(self.data)

	def __setitem__(self, key: int, value: Word) -> None:
		"""
		Write the provided value at the specified index
		(key) location.

		:param key: The tape index to write to.
		:param value: The value to write.
		:return: None

		:raises: IndexError, ValueError

		"""

		if not self.vocab.__contains__(item=value):
			msg = "Trying to Set Word ({}) not in Vocab."
			raise ValueError(msg.format(value.name))

		self.data[key] = value

	def __getitem__(self, item: int) -> Word:
		"""
		Get the word at the specified position.

		:param item: int, The position to read.
		:return: Word

		:raises: IndexError

		"""

		return self.data[item]

	@property
	def vocab(self) -> Vocabulary:
		"""
		:obj:`Vocabulary` The vocabulary defines the
			valid words that may be written to the tape.

		Set tape's vocabulary.

		:raises: ValueError if (on update) the vocabulary
			is changed and excludes characters from either
			the data stream or default character.

		"""

		return self.__vocab

	@vocab.setter
	def vocab(self, vocab: Vocabulary) -> None:
		self.__vocab = vocab  # set new vocab
		self.default = self.default  # check default

		# check the data
		for word in self.data:
			if not self.vocab.__contains__(item=word):
				msg = "Invalid Word ({}) in Data Stream."
				raise ValueError(msg.format(word.name))

	@property
	def data(self) -> List[Word]:
		"""
		:obj:`List[Word]` The data is the entire
			tape state as a (finite) array of what has
			been "seen" by th user or provided as input
			to the machine. However, the tape head is able
			to expand the tape's visible section indefinitely.


		Set tape's data.

		:raises: ValueError if any of the characters
			in the data stream are not in the vocabulary.

		"""

		return self.__data

	@property
	def default(self) -> Word:
		"""
		:obj:`Word` The default character to assign
			to newly visible space on the tape.
			Canonically this value is taken to be 'B'
			for a blank positional tape state.


		Set tape's default character.

		:raises: ValueError if the default character
			does not belong to the defined vocabulary.

		"""

		return self.__default

	@default.setter
	def default(self, default: Word) -> None:
		if not self.vocab.__contains__(item=default):
			msg = "Default Word ({}) not in Vocab."
			raise ValueError(msg.format(default.name))

		self.__default = default
