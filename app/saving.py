from json import dump, dumps
from os import path
from sys import path as syspath

from input import get, y, yn
from output import sp

# save from pause menu or pokemon centre
def backup(save: dict, pokemon_centre: bool=False) -> None:
	if not pokemon_centre:
		sp('Would you like to save your progress? (Y/N)\n')
		save_option = ' '
		while save_option.lower()[0] not in yn:
			save_option = f'{get()} '
		if save_option.lower()[0] in y:
			save_data_to_file(save)
	else:
		save_data_to_file(save)

# save data to file
def save_data_to_file(save: dict) -> None:
	save['flag']['has_saved'] = True
	save_temp = {**save, 'party': [dumps(i) for i in save['party']], 'box': [dumps(i) for i in save['box']], 'last_played': None} # TODO: save time last played
	open(path.join(syspath[0], '.ppr-save'), 'w').write(f'{dumps(save_temp, indent=4, sort_keys=True)}\n')
	sp('\nGame saved successfully!')
