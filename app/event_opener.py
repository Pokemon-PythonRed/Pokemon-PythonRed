from importlib import import_module
from os import path
from sys import path as syspath
from typing import Any, Optional

from saving import SaveFile

# event class
class Event:

	# set internals
	def __init__(self, id: str) -> None:
		self.id = id
		self.module_name = f'events.{self.id}'
		self.module = import_module(self.module_name)

	def __str__(self) -> str:
		return f'{self.id}'

	def execute(self, save: Optional[SaveFile]=None) -> SaveFile:
		return self.module.execute(save)
