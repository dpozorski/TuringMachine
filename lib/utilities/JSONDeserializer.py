#!/usr/bin/env python

"""

JSONDeserializer Docstring

The JSON Deserializer class is meant for converting
object data stored in a JSON format to the corresponding
python object.

Code based on Medium post for a Pythonic way to manage JSON
and updated to allow for nested/recursive object structure:

https://medium.com/python-pandemonium/json-the-python-way-91aac95d4041
@The Fellow

"""

from typing import Dict, Any, List, Union
from lib.utilities.ObjectMapping import ObjectMapping

__author__ = "Dylan Pozorski"
__project__ = "TuringMachine"
__class__ = "JSONDeserializer"


class JSONDeserializer(object):
	"""
	JSONDeserializer

	Attributes:


	"""

	def __init__(self):
		"""
		Construct the JSONDeserializer.

		"""

		pass

	@staticmethod
	def deserialize(obj_json: Union[Dict, List]) -> Any:
		"""
		Deserialize a Dict/JSON object into a
		Python object.

		:param obj_json: Dict, Dict/JSON object to
			deserialize into a Python object.
		:return: Any

		"""

		if isinstance(obj_json, dict):
			if "__module__" in obj_json and "__class__" in obj_json:
				cls = ObjectMapping(
					mapper_class_name=obj_json.pop("__class__"),
					mapper_module_path=obj_json.pop("__module__")
				).target_class()

				for k in obj_json.keys():
					obj_json[k] = JSONDeserializer.deserialize(
						obj_json=obj_json[k]
					)

				return cls(**obj_json)
		elif isinstance(obj_json, list):
			items = list()

			for i in range(0, len(obj_json)):
				items.append(
					JSONDeserializer.deserialize(
						obj_json=obj_json[i]
					)
				)

			return items

		return obj_json
