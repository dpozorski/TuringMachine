#!/usr/bin/env python

"""

TapeGenerator Docstring

The Tape Generator class is designed to easily
construct initial tape states for the addition,
multiplication, and successor operations.

"""

from lib.Tape import Tape
from lib.controllers.table.Word import Word
from lib.controllers.binary_table.Bit import Bit
from lib.controllers.table.Vocabulary import Vocabulary

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "TapeGenerator"


class TapeGenerator(object):
	"""
	TapeGenerator

	Attributes:


	"""

	def __init__(self):
		"""
		TapeGenerator Constructor.


		"""

		pass

	@staticmethod
	def addition(a: int, b: int) -> Tape:
		"""
		Configure the tape with the binary setup
		to process (a + b).

		:param a: int, First operand on the tape.
		:param b: int, Second operand on the tape.
		:return: Tape

		:raises ValueError If either operand is < 0.

		"""

		a = TapeGenerator.succession(a=a)
		a.data.append(Word(name=Bit.BINARY_LABEL_0))
		[a.data.append(c) for c in TapeGenerator.succession(a=b)]
		return a

	@staticmethod
	def multiplication(a: int, b: int) -> Tape:
		"""
		Configure the tape with the binary setup
		to process (a * b).

		:param a: int, First operand on the tape.
		:param b: int, Second operand on the tape.
		:return: Tape

		:raises ValueError If either operand is < 0.

		"""

		return TapeGenerator.addition(a=a, b=b)

	@staticmethod
	def succession(a: int) -> Tape:
		"""
		Configure the tape with the binary setup
		to process (a + 1).

		:param a: int, First operand on the tape.
		:return: Tape

		:raises ValueError If the operand is < 0.

		"""

		if a < 0:
			raise ValueError("Only non-negative operands allowed.")

		tape = TapeGenerator.new_tape()

		for i in range(0, (a + 1)):
			tape.data.append(Word(name=Bit.BINARY_LABEL_1))

		return tape

	@staticmethod
	def new_tape() -> Tape:
		"""
		Creates a configured but empty tape.

		:return: Tape

		"""

		return Tape(
			vocab=Vocabulary(
				words={
					Word(name=Bit.BINARY_LABEL_0),
					Word(name=Bit.BINARY_LABEL_1)
				}
			),
			default=Word(name=Bit.BINARY_LABEL_0),
			data=[]
		)
