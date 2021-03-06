#!/usr/bin/env python

"""

Head Docstring

The Head class represents read/write head of the
tape. This represents the interface that the
controller's dictated action on.

"""

from lib.Tape import Tape
from lib.controllers.table.Word import Word

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "Head"


class Head(object):
	"""
	Head

	Attributes:
		tape (:obj:`Tape`): The tape object the head
			is traversing and interacting with.

	"""

	def __init__(self, tape: Tape):
		"""
		Head Constructor.

		"""

		self.__tape = tape
		self.__position = 0
		self.__operations = 0

		if len(self.__tape) == 0:
			self.write(word=self.tape.default)

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the tape head object.

		:return: str

		"""

		p = []

		for i in range(0, len(self.tape.data)):
			d = str(self.tape.data[i])

			if i == self.position:
				d = '\033[1m\033[92m' + d + '\033[0m'

			p.append(d)

		return " ".join(p)

	def __repr__(self) -> str:
		"""
		Return the canonical string representation
		of the tape head object.

		:return: str

		"""

		return self.__str__()

	def left(self) -> None:
		"""
		Moves the tape head left.

		:return: None

		"""

		if self.position - 1 < 0:
			self.tape.data.insert(
				self.position,
				self.tape.default
			)
		else:
			self.__position -= 1

		self.__operations += 1

	def right(self) -> None:
		"""
		Moves the tape head right.

		:return: None

		"""

		if self.position + 1 >= len(self.tape):
			self.tape.data.append(self.tape.default)
			self.__position = len(self.tape) - 1
		else:
			self.__position += 1

		self.__operations += 1

	def write(self, word: Word) -> None:
		"""
		Writes the specified word to the tape
		at the tape head's current position.

		:param word: Word, The word to write.
		:return: None

		"""

		self.tape[self.position] = word
		self.__operations += 1

	def read(self) -> Word:
		"""
		Reads the word on the tape at the tape 
		head's current position.
		
		:return: Word

		"""

		return self.tape[self.position]

	@property
	def tape(self) -> Tape:
		"""
		:obj:`Tape` The tape object the head
		is traversing and interacting with.

		"""

		return self.__tape

	@property
	def position(self) -> int:
		"""
		:obj:`int` The position on the visible tape
		space that the head is currently located. The
		left-most position is always indexed at 0.

		"""

		return self.__position

	@property
	def operations(self) -> int:
		"""
		:obj:`int` The count of operations performed
		by the tape head (counting left, right, and write
		operations). Reading is implicitly done each
		machine action/state transition.

		"""

		return self.__operations
