from data_opener import dex, xp
from input import get, y, yn
from output import sp
from pokemon import badges
from saving import SaveFile

def menu(save: SaveFile) -> SaveFile: # sourcery skip: low-code-quality
	global exit_status, menu_open, option, options_open
	option = ''
	menu = f'Menu\n[d] - Pokédex\n[p] - Pokémon\n[i] - Item\n[t] - {save["name"]}\n[s] - Save Game\n[o] - Options\n[e] - Exit Menu\n[q] - Quit Game\n' if 'Pokedex' in save['bag'] else f'Menu\n[p] - Pokémon\n[i] - Item\n[t] - {save["name"]}\n[s] - Save Game\n[o] - Options\n[e] - Exit Menu\n[q] - Quit Game\n'
	while menu_open:
		sp([(menu, False)])
		while not option:
			option = get(['d', 'e', 'i', 'o', 'p', 'q', 's', 't'])
		if option not in ['e', 'o']:
			sp([('', False)])
		if option == 'd' and 'Pokedex' in save['bag']:
			option = ''
			dex_string = ''
			for i in dex.keys():
				if i in save['dex'].keys():
					dex_string += f'\n{dex[i]["index"]} - {i}: Seen' if save['dex'][i]['seen'] else ''
					if save['dex'][i]['caught']:
						dex_string += ', Caught'
			sp([(f'{save["name"]}\'s Pokédex{dex_string}' if dex_string else '\nYou have no Pokémon in your Pokédex!', False)])
		elif option == 'p':
			if save['party']:
				sp([('\n'.join(f'{i.name} (`{i.type}`-type)\nLevel {i.level} ({i.current_xp}/{str(xp["next"][i.level_type][str(i.level)])} XP to next level)\n{i.stats["chp"]}/{i.stats["hp"]} HP' for i in save['party']), False)])
			else:
				sp([('Your party is empty!', False)])
		elif option == 'i':
			if save['bag']:
				for i in save['bag']:
					sp([(f'{i}: {save["bag"][i]}', False)])
			else:
				sp([('Your bag is empty!', False)])
		elif option == 't':
			sp([
				(f'Name: {save["name"]}', False),
				(f'Money: ¥{"{:,}".format(save["money"])}', False),
				(f'''Badges: {''.join(f"[{'-' if save['badges'][i] else ' '}]" for i in badges)}''', False)
			])
		elif option == 's':
			save.backup()
		elif option == 'o':
			options_open = True
		elif option == 'e':
			menu_open = False
		elif option == 'q':
			sp([('Are you sure you want to quit? Any unsaved progress will be lost. (Y/N)\n', False)])
			option = ''
			while option not in yn:
				option = get(yn)
			if option in y:
				exit_status = True
	return save
