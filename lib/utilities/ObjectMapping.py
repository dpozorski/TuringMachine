#!/usr/bin/env python

"""

ObjectMapping Docstring

The ObjectMapping object represents the ORM/
Database object mapping that extracted and
transformed data should be mapped to.


"""

from typing import Type
import importlib.util
import importlib

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "ObjectMapping"


class ObjectMapping(object):
	"""
	ObjectMapping

	Attributes:
		mapper_class_name (:obj:`str`): The name class
			being mapped to by the extracted data.
		mapper_module_path (:obj:`str`): The module path to
			the class being mapped to by the extracted data.

	"""

	def __init__(self, mapper_class_name: str, mapper_module_path: str):
		"""
		ObjectMapping Constructor

		:param mapper_class_name: str, The name class
			being mapped to by the extracted data.
		:param mapper_module_path: str,  The module path to
			the class being mapped to by the extracted data.

		"""

		self.mapper_class_name = mapper_class_name
		self.mapper_module_path = mapper_module_path

	def target_class(self) -> Type:
		"""
		Returns whether the column is a concrete
		column and not the prototype for a set of columns.

		:return: bool

		"""

		spec = importlib.util.find_spec(
			self.mapper_module_path,
			self.mapper_class_name
		)
		mod = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(mod)
		return getattr(mod, self.mapper_class_name)

	@property
	def mapper_class_name(self) -> str:
		"""
		:obj:`str` The name class being mapped to
			by the extracted data.

		Set mapper class name.

		"""

		return self.__mapper_class_name

	@mapper_class_name.setter
	def mapper_class_name(self, mapper_class_name: str):
		self.__mapper_class_name = mapper_class_name

	@property
	def mapper_module_path(self) -> str:
		"""
		:obj:`str` The module path to the class
			being mapped to by the extracted data.

		Set mapper module path.

		"""

		return self.__mapper_module_path

	@mapper_module_path.setter
	def mapper_module_path(self, mapper_module_path: str):
		self.__mapper_module_path = mapper_module_path
