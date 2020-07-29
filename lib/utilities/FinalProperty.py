#!/usr/bin/env python

"""

FinalProperty Docstring

The Final Property class allows for the definition
of final object properties that can only be set once
on instantiation) and cannot be set afterward.

Source:
https://stackoverflow.com/questions/802578/final-keyword-equivalent-for-variables-in-python

"""

from typing import TypeVar, Generic, Type

__author__ = "Eli Courtwright"
__project__ = "TuringMachine"
__class__ = "FinalProperty"

T = TypeVar('T')


class FinalProperty(Generic[T]):
	"""
	FinalProperty

	Attributes:

	"""

	def __init__(self, value: T):
		"""
		FinalProperty Constructor

		:param value: T, The value to assign to
			the given property.

		"""

		self.__value = value

	def __get__(self, instance: Type, owner) -> T:
		"""
		Accessor method for getting the value.

		:param instance: instance, The object instance type.
		:param owner: The object owner.
		:return: T

		"""

		return self.__value

	def __set__(self, instance: Type, value: T) -> None:
		"""
		Method for setting the property. Always fails
		since this property is defined as final.

		:param instance: Type, The object type of the
			property to make final.
		:param value: T, The value to store for the
			property being made final.
		:return: None

		:raises: ValueError

		"""

		raise ValueError("Final types cannot be set")
