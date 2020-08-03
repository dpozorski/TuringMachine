#!/usr/bin/env python

"""

MachineLog Docstring

The Machine Log class logs the input/output
data from the Turing Machine..

"""

import math
import copy
import pandas as pd
from typing import List
from lib.controllers.IOPair import IOPair

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "MachineLog"


class MachineLog(object):
	"""
	MachineLog

	Attributes:
		records (:obj:`List[IOPair]`): The list of input-
			output pairs logged during the duration of
			program execution.

	"""

	def __init__(self, records: List[IOPair] = None):
		"""
		MachineLog Constructor.

		:param records: List[IOPair], The list of
			machine log i/o records.

		"""

		self.__records = []
		records = [] if records is None else records

		for record in records:
			self.log(record=record)

	def __str__(self) -> str:
		"""
		Return the informal string representation
		of the state object.

		:return: str

		"""

		ls = self.label_size
		records = copy.deepcopy(self.__records)

		for record in records:
			record.label_size = ls

		return '\n'.join([str(r) for r in records])

	def __len__(self) -> int:
		"""
		Return the number of records in the
		machine's log.

		:return: int

		"""

		return len(self.__records)

	def log(self, record: IOPair) -> None:
		"""
		Log the record passed into this function
		into the machine's record log.

		:param record: IOPair, Record to add.
		:return: None

		"""

		if record.input is None or record.output is None:
			raise ValueError("Record Missing I/O Component.")
		elif record.input.timestep != record.output.timestep:
			raise ValueError("Timestep Mismatch in I/O.")

		if record not in self.__records:
			for i in self.__records:
				if i.input.timestep == record.input.timestep:
					raise ValueError("Conflicting I/O for Timestep.")

			self.__records.append(record)

	def export_csv(self, filepath: str, label_padding: int = 0) -> None:
		"""
		Export the machine log as a .csv file.

		:param filepath: str, The file path to export.
		:param label_padding: int, The number of bits to
			pad the output state label (prepend w/ 0s).
		:return: None

		"""

		items = []
		ls = self.label_size + max(0, label_padding)
		records = copy.deepcopy(self.__records)

		for record in records:
			record.label_size = ls

		[items.append(str(record).split(','))
			for record in records]
		items = pd.DataFrame(items)
		items.columns = ["input", "output"]
		items.to_csv(path_or_buf=filepath, index=False)

	def remove(self, record: IOPair) -> None:
		"""
		Remove the IOPair from the machine's log.

		:param record: IOPair, The removed record.
		:return: IOPair

		"""

		if record in self.__records:
			self.__records.remove(record)

	def clear(self) -> None:
		"""
		Clear the record log.

		:return: None

		"""

		self.__records = []

	@property
	def label_size(self) -> int:
		"""
		:obj:`int` The state label size to log the
		IOPair with. Pads the state label if necessary.

		"""

		bits = 1 if len(self.__records) == 0 else \
			max([r.output.state.label for r in self.__records])
		return int(math.ceil(math.log(max(1, bits), 2)))
