from contextlib import suppress
from getpass import getuser
from json import dump, dumps, load
from os import path
from sys import path as syspath
from typing import Optional, Union

from data_opener import locations, save_template
from handling import abort
from input import get, y, yn
from output import sp
from pokemon import badges, Pokemon

# save file class
class SaveFile(dict):
	def __init__(
		self,
		save_path: Optional[Union[str, list[str]]]='.ppr-save',
		save_exists: bool=True,
		**saves: Optional[dict]
	) -> None:
		for key, val in {
			**save_template, **saves, 'badges': {i: False for i in badges}
		}.items():
			setattr(self, key, val)
		if getuser() not in getattr(self, 'user'):
			setattr(self, 'user', getattr(self, 'user').append(getuser()))
		global is_debug
		is_debug = getattr(self, 'options')['debug']
		if save_exists:
			try:
				with open(
					path.join(
						syspath[0], *save_path
					), 'tr'
				) as f:
					for key, val in {
						**load(f)
					}.items():
						setattr(self, key, val)
				for location in ['party', 'box']:
					for pokemon_iter in getattr(self, location):
						setattr(self, location, [Pokemon(species=pokemon_iter['species'], level=pokemon_iter['level'], ivs=pokemon_iter['ivs'], moves=pokemon_iter['moves'], chp=pokemon_iter['stats']['chp'], current_xp=pokemon_iter['current_xp'], fainted=pokemon_iter['fainted'], player_pokemon=True)])
			except FileNotFoundError as e:
				abort(f'{e}')

	# save data to file
	def save_to_file(self, path: str='.ppr-save') -> None:
		self['flags']['has_saved'] = True
		save_temp = {**self, 'party': [dumps(i) for i in self['party']], 'box': [dumps(i) for i in self['box']], 'last_played': None} # TODO: save time last played
		with open(
			path.join([syspath[0], path]), 'w'
		) as f:
			f.write(f'{dumps(save_temp, indent=4, sort_keys=True)}\n')
		sp([('\nGame saved successfully!', False)])

	# save from pause menu or pokemon centre
	def backup(
		self,
		pokemon_center: bool=False
	) -> None:
		if not pokemon_center:
			sp([('Would you like to save your progress? (Y/N)\n', False)])
			if get(yn) in y:
				self.save_to_file()
		else:
			self.save_to_file()

	# check for illegal save data
	def scan(self) -> bool:
		with suppress(KeyError):
			if not any([
				len(self['name']) > 15,
				len(self['party']) > 6,
				self['flag']['been_to_route_1'] and len(self['party']) == 0,
				self['flag']['chosen_starter'] and not self['flag']['intro_complete'],
				self['flag']['chosen_starter'] and self['location'] == '',
				self['name'] != '' and not self['flag']['intro_complete'],
				self['name'] != self['name'].upper(),
				self['name'] == '' and self['flag']['intro_complete']
			]):
				return True
		return False
