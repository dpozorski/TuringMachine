#!/usr/bin/env python

"""

Write Docstring

The Write class represents the write
action to perform using the tape head.

"""

from lib.Head import Head
from lib.controls.Action import Action
from lib.data.Word import Word

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Write"


class Write(Action):
	"""
	Write

	Attributes:
		word (:obj:`Word`): The word to write
			provided a valid tape head.

	"""

	def __init__(self, word: Word):
		"""
		Write Constructor.

		:param word: str, The word to write
			provided a valid tape head.

		"""

		Action.__init__(self)
		self.word = word

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the write action object.

		:return: str

		"""

		return self.word.name

	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the write action object.

		:return: str

		"""

		msg = "Write to Tape (value={})"
		return msg.format(self.word.name)

	def exec(self, head: Head) -> None:
		"""
		Execute the write operation.

		:param head: Head, The tape head object
			interfacing with the machine's tape.
		:return: None

		"""

		head.write(word=self.word)

	@property
	def word(self) -> Word:
		"""
		:obj:`Word` The word to write
			provided a valid tape head.

		Set word to print.

		"""

		return self.__word

	@word.setter
	def word(self, word: Word) -> None:
		self.__word = word
