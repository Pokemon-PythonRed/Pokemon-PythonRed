from keyboard import KeyboardEvent
from os import path
from sys import path as syspath
from typing import Optional, Union

from data_opener import locations, rates
from event_opener import Event
from saving import SaveFile

# location class
class Location:

	# set internals
	def __init__(self, id: str) -> None:
		self.id = id
		self.title = locations[self.id]['title']
		self.subtitle = locations[self.id]['subtitle']
		self.titled = locations[self.id]['titled']
		self.directions = locations[self.id]['directions']
		if self.title in rates.keys():
			self.rates = rates[self.title]
			self.is_encounter_zone = True
		else:
			self.rates = None
			self.is_encounter_zone = False

	# display options
	def execute(self) -> SaveFile: # TODO: execute location, save param, return SaveFile
		print(f'\n{self.title}')
		for key, val in self.directions.items():
			print(f'[{key}] - {locations[val]["title"]}')
