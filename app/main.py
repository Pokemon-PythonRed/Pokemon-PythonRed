'''
Project Page - [https://Pokemon-PythonRed.github.io]
Repository   - [https://github.com/Pokemon-PythonRed/Pokemon-PythonRed]
License      - MIT
'''

# import system modules
from datetime import datetime
from getpass import getuser
from json import dumps, loads
from math import ceil, floor, sqrt
from os import path, system, remove
from platform import system as platform
from random import choice, choices, randint
# TODO: from string import ...
from sys import exit as sysexit, path as syspath, stdout
from time import sleep
from typing import Optional, Union
from webbrowser import open as webopen

# import installed modules
from jsons import dump, load
# TODO: from pygame import ...

# abort function to be used before functions that require libraries
def abort_early() -> None:
	input('It appears that you are using an unsupported operating system. Please use Windows or Linux.\n\nPress Enter to exit.')
	system.exit()

# import getch according to system
if platform() == 'Windows':
	from msvcrt import getch # type: ignore
elif platform() == 'Linux':
	from getch import getch # type: ignore
else:
	abort_early()

# type colours
colours = {
	'NORMAL': '\x1b[0;0m',
	'FIRE': '\x1b[38;5;196m',
	'WATER': '\x1b[38;5;027m',
	'GRASS': '\x1b[38;5;082m',
	'ELECTRIC': '\x1b[38;5;184m',
	'ICE': '\x1b[38;5;159m',
	'FIGHTING': '\x1b[38;5;167m',
	'POISON': '\x1b[38;5;135m',
	'GROUND': '\x1b[38;5;215m',
	'FLYING': '\x1b[38;5;183m',
	'PSYCHIC': '\x1b[38;5;198m',
	'BUG': '\x1b[38;5;028m',
	'ROCK': '\x1b[38;5;179m',
	'GHOST': '\x1b[38;5;126m',
	'DRAGON': '\x1b[38;5;057m',
	'DARK': '\x1b[38;5;095m',
	'STEEL': '\x1b[38;5;250m',
	'FAIRY': '\x1b[38;5;212m',
	'RESET': '\x1b[0;0m'
}

# declare timed text output
text = {
	'slow': 0.03,
	'normal': 0.02,
	'fast': 0.01,
	'ultra': 0.005,
	'debug': 0.0
}
text_speed = 'normal'
def reset_sp(speed) -> None:
	global sp, sg
	def sp(text, g=False) -> None:
		for key in colours.keys():
			text = text.replace(f'{key}', f'{colours[key]}{key}{colours["RESET"]}')
		for char in f'{text}\n':
			sleep(speed)
			stdout.write(char)
			stdout.flush()
		if g:
			getch()
	def sg(text) -> None:
		sp(text, g=True)
reset_sp(speed=text[text_speed])

# load screen
sp('Loading...')

# input function:
def get() -> str:
	return input('> ')

# store links
link = {
	'repository': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed',
	'installation': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed#installation',
	'issue': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed/issues/new/choose'
}

# check for required files
if not (path.isfile(path.join(syspath[0], i)) for i in [
	'data/dex.json',
	'data/level.json',
	'data/trainer.json',
	'data/types.json',
	'data/moves.json',
	'data/map.json',
	'data/pokemart.json',
	'build_to_exe.py'
]):
	sp(f'\nOne or more required files are not found.\n\nPlease see\n[{link["installation"]}]\nfor more information.\n\nPress Enter to exit.\n')
	get()
	sysexit()

# declare clear
platforms = [
	['darwin', 'clear'],
	['java', 'System.out.print("\\033[H\\033[2J");System.out.flush();'],
	['linux', 'clear'],
	['windows', 'cls']
]
for i in range(len(platforms)):
	if platform().lower() == (platforms[i][0]):
		cls_command = platforms[i][1]
		def cls(command=cls_command) -> int: return system(command)
		break
try:
	cls() # type: ignore
except NameError:
	abort_early()

# menu variables
exit = is_debug = menu_open = options_open = False
y, n, yn = ['y'], ['n'], ['y', 'n']
types = ['NORMAL', 'FIRE', 'WATER', 'GRASS', 'ELECTRIC', 'ICE', 'FIGHTING', 'POISON', 'GROUND', 'FLYING', 'PSYCHIC', 'BUG', 'ROCK', 'GHOST', 'DARK', 'DRAGON', 'STEEL', 'FAIRY']
badges = ['Boulder', 'Cascade', 'Thunder', 'Rainbow', 'Soul', 'Marsh', 'Volcano', 'Earth']

# battle screen variables
name_length = 15
bars_length = 20

# enables ANSI escape codes in Windows
system('')

# error message
def abort(message) -> None:
	print(f'\n{colours["FIRE"]}- - - INTERNAL ERROR - - -{colours["RESET"]}\n\nERROR MESSAGE: {message}\n\nIf you have not edited any files, feel free to create an issue on the repository by going to the link below.\n\nNote: your save file will be preserved in the program folder. Any unsaved progress will be lost (sorry).\n\n[{link["issue"]}]\n\nPress Enter to exit.')
	input('\n> ')
	global exit
	exit = True

# save from pause menu
def backup() -> None:
	sp('Would you like to save your progress? (Y/N)\n')
	save_option = ' '
	while save_option.lower()[0] not in yn:
		save_option = f'{get()} '
	if save_option.lower()[0] in y:
		save_data_to_file()

# save data to file
def save_data_to_file():
	save['flag']['has_saved'] = True
	save_temp = {**save, 'party': [dump(i) for i in save['party']], 'box': [dump(i) for i in save['box']], 'last_played': None} # TODO: save time last played
	open(path.join(syspath[0], '.ppr-save'), 'w').write(f'{dumps(save_temp, indent=4, sort_keys=True)}\n')
	sp('\nGame saved successfully!')

# decide if damage is critical
def critical() -> bool:
	return randint(0, 255) <= 17

# pokemon class
class Pokemon:

	# set internals
	def __init__(self, species, level, ivs, moves=None, chp=None, current_xp=0, fainted=False, player_pokemon = False) -> None:
		self.species = species
		self.index = dex[self.species]['index'] # type: ignore
		self.name = dex[self.species]['name'] # type: ignore
		self.type = dex[self.species]['type'] # type: ignore
		self.level = level
		self.ivs = ivs if ivs != 'random' else {i: randint(0, 31) for i in ['hp', 'atk', 'def', 'spa', 'spd', 'spe']}
		self.level_type = dex[self.species]['xp'] # type: ignore
		self.total_xp = xp['total'][self.level_type][str(self.level)] # type: ignore
		self.current_xp = current_xp
		self.moves = moves or find_moves(self.species, self.level)
		self.status = {
			'burn': False,
			'confusion': False,
			'freeze': False,
			'paralysis': False,
			'poison': False,
			'sleep': False
		}

		# update pokedex
		if self.species not in save['dex']:
			save['dex'].update({self.species: {'seen': True, 'caught': False}})
		else:
			if 'seen' not in save['dex'][self.species]:
				save['dex'][self.species]['seen'] = True
			if 'caught' not in save['dex'][self.species]:
				save['dex'][self.species]['caught'] = False
		if self.type not in save['flag']['type']:
			save['flag']['type'].update({self.type: {'seen': True, 'caught': False}})
		else:
			if 'seen' not in save['flag']['type'][self.type]:
				save['flag']['type'][self.species]['seen'] = True
			if 'caught' not in save['flag']['type'][self.type]:
				save['flag']['type'][self.species]['caught'] = False

		# initialise stats
		self.reset_stats(chp, fainted, player_pokemon)

	# reset stats
	def reset_stats(self, chp=None, fainted=None, player_pokemon = False) -> None:
			self.stats = {
				'hp': floor(((dex[self.species]['hp'] + self.ivs['hp']) * 2 + floor(ceil(sqrt(self.ivs['hp'])) / 4) * self.level) / 100) + self.level + 10, # type: ignore
				'atk': floor(((dex[self.species]['atk'] + self.ivs['atk']) * 2 + floor(ceil(sqrt(self.ivs['atk'])) / 4) * self.level) / 100) + 5, # type: ignore
				'def': floor(((dex[self.species]['def'] + self.ivs['def']) * 2 + floor(ceil(sqrt(self.ivs['def'])) / 4) * self.level) / 100) + 5, # type: ignore
				'spa': floor(((dex[self.species]['spa'] + self.ivs['spa']) * 2 + floor(ceil(sqrt(self.ivs['spa'])) / 4) * self.level) / 100) + 5, # type: ignore
				'spd': floor(((dex[self.species]['spd'] + self.ivs['spd']) * 2 + floor(ceil(sqrt(self.ivs['spd'])) / 4) * self.level) / 100) + 5, # type: ignore
				'spe': floor(((dex[self.species]['spe'] + self.ivs['spe']) * 2 + floor(ceil(sqrt(self.ivs['spe'])) / 4) * self.level) / 100) + 5 # type: ignore
			}
			if player_pokemon == False:
				for move in self.moves:
					move['pp'] = list(filter(lambda m, move=move: m['name'] == move['name'], moves))[0]['pp'] # type: ignore
			self.stats['chp'] = chp or self.stats['hp']
			self.fainted = fainted or self.stats['chp'] <= 0
			if self.fainted:
				self.stats['chp'] = 0

	# check levels for entire party
	def check_level_up(self, party) -> None:
		for i in party:
			while self.current_xp >= xp['next'][self.level_type][str(self.level)] and self.level < 100: # type: ignore
				i.current_xp -= xp['next'][self.level_type][str(self.level)] # type: ignore
				self.level_up(i)

	# check if pokemon is fainted
	def check_fainted(self) -> bool:
		if self.stats['chp'] <= 0:
			self.stats['chp'] = 0
			self.fainted = True
			return True
		return False

	# lower chp when pokemon is attacked
	def deal_damage(self, attacker, move) -> Optional[int]:
		move_entry = list(filter(lambda m: m['name'] == move['name'], moves))[0] # type: ignore
		sp(f'\n{attacker.name} used {move["name"].upper()}!')
		if move_entry['damage_class'] == 'status':
			# TODO: Implement status conditions
			sp(f'(Note: {move["name"].upper()} is a status move)')
		else:
			if randint(1,100) <= move_entry["accuracy"]:
				damage = self.damage_calc(move_entry, attacker)
			else:
				sp(f'{attacker.name} missed!')
			return damage # type: ignore

	# TODO Rename this here and in `deal_damage`
	def damage_calc(self, move_entry, attacker):
		is_critical = critical()
		attack_defense = ('atk', 'def') if move_entry['damage_class'] == 'physical' else ('spa', 'spd')
		result = floor((((((2 * attacker.level * (2 if is_critical else 1) / 5) + 2) * move_entry['power'] * attacker.stats[attack_defense[0]] / self.stats[attack_defense[1]]) / 50) + 2) * (1.5 if move_entry['type'] == attacker.type else 1) * randint(217, 255) / 255 * (type_effectiveness(move_entry, self) if save['flag']['been_to_route_1'] else 1))

		self.stats['chp'] -= result
		if result > 0: 
			sp(f'\n{attacker.name} dealt {result} damage to {self.name}!')
		if is_critical:
			sp('A critical hit!')
		for i in [
			(0, 'It had no effect!'),
			(0.5, 'It\'s super effective!'),
			(2, 'It\'s not very effective!')
		]:
			if types[self.type][move_entry['type'].upper()] == i[0]:
				sp(f'{i[1]}')
		self.check_fainted()
		if self.fainted:
			sp(f'\n{self.name} fainted!')
		return result

	def deal_struggle_damage(self, damage):
		sp(f'{self.name} is hit with recoil!')
		self.stats['chp'] -= floor(damage / 2)
		self.check_fainted()
		if self.fainted:
			sp(f'\n{self.name} fainted!')

	# calculate xp rewarded after battle
	def calculate_xp(self, battle_type='wild') -> int:
		return ceil((self.total_xp * self.level * (1 if battle_type == 'wild' else 1.5)) / 7) # type: ignore

	# level up pokemon in context of battle
	def give_xp(self, battle_type='wild') -> None:
		self.current_xp += self.calculate_xp(battle_type)
		sg(f'\n{self.name} gained {self.calculate_xp(battle_type)} XP!')
		while self.current_xp >= xp['next'][self.level_type][self.level]: # type: ignore
			self.current_xp -= xp['next'][self.level_type][self.level] # type: ignore
			self.level_up(self)
			if self.level == 100:
				sp(f'\nCongratulations, {self.name} has reached level 100!')
				break

	# raw level up
	def level_up(self, pokemon): # sourcery skip: low-code-quality
		pokemon.level += 1
		pokemon.reset_stats()
		sp(f'{pokemon.name} grew to level {pokemon.level}!')
		for m in dex[pokemon.species]['moves']: # type: ignore
			if m['level'] == pokemon.level:
				if len(pokemon.moves) == 4:
					sg(f'{pokemon.name} wants to learn {m["name"].upper()}!')
					sg(f'But {pokemon.name} already knows 4 moves')
					all_moves = [*pokemon.moves, m]
					move_forgotten = False
					while not move_forgotten:
						sp(f'Which move should {pokemon.name} forget?')
						for i in range(5):
							print(f'[{i+1}] - {all_moves[i]["name"].upper().replace("-", " ")}')
						forget_move = ''
						while not forget_move:
							forget_move = get()
							if forget_move not in ['1', '2', '3', '4', '5']:
								forget_move = ''
							else:
								if forget_move == '5':
									sp(f'\nAre you sure you want {pokemon.name} to not learn {m["name"].upper()}? (Y/N)')
								else:
									sp(f'\nAre you sure you want {pokemon.name} to forget {all_moves[int(forget_move)-1]["name"].upper()}? (Y/N)')
								option = ''
								while option not in ['y','n']:
									option = get()
								if option in ['y']:
									if forget_move == '5':
										sp(f'\n{pokemon.name} didn\'t learn {m["name"].upper()}')
									else:
										sp(f'\n{pokemon.name} forgot {all_moves[int(forget_move)-1]["name"].upper()}\n')
										sp(f'\n{pokemon.name} learned {m["name"].upper()}!')
										pokemon.moves = [m for m in pokemon.moves if m['name'] != all_moves[int(forget_move) - 1]['name']]
										pokemon.moves.append({"name": m['name'], "pp": list(filter(lambda mv: mv['name'] == m['name'], moves))[0]['pp']}) # type: ignore
									move_forgotten = True
				else:
					sg(f'{pokemon.name} learned {m["name"].upper()}')
					pokemon.moves.append({"name": m['name'], "pp": list(filter(lambda mv, m=m: mv['name'] == m['name'], moves))[0]['pp']}) # type: ignore

	# catch Pokemon
	def catch(self, ball: str) -> bool:
		global save
		if max(bool(self.status[i]) for i in ['freeze', 'sleep']):
			status = 25
		elif max(bool(self.status[i]) for i in ['burn', 'poison', 'paralysis']):
			status = 12
		else:
			status = 0

		# find Poke Ball type
		if ball == "Great Ball":
			ball_modifier = 201
		elif ball == "Poke Ball":
			ball_modifier = 256
		elif ball == "Ultra Ball":
			ball_modifier = 151
		else:
			abort(f'Invalid ball: {ball}')

		# decide whether caught
		C = dex[self.species]['catch'] # type: ignore
		if ball == "Master Ball":
			catch = True
		elif self.stats['hp'] / (2 if ball == "Great Ball" else 3) >= self.stats['chp'] and (status + C + 1) / ball_modifier >= 1: # type: ignore
			catch = True
		else:
			X = randint(0, ball_modifier-1) # type: ignore
			if X < status:
				catch = True
			elif X > status + C:
				catch = False
			else:
				catch = min(
					255,
					floor(
						floor(self.stats['hp'] * 255 / (8 if ball == "Great Ball" else 12))
						/ max(1, floor(self.stats['chp'] / 4))
					),
				) >= randint(0, 255)

		# catch Pokemon process
		if catch:
			location = 'party' if len(save['party']) < 6 else 'box'
			save[location].append(self)
			save['dex'][self.species] = {'seen': True, 'caught': True}
			save['flag']['type'][self.type] = {'seen': True, 'caught': True}
			sg(f'\nYou caught {self.name}!')
			sg(f'\n{self.name} ({self.type}-type) was added to your {location}.')
			return True
		else:
			if floor(
				C * 100 / ball_modifier # type: ignore
			) > 255: # 3 wobbles
				sp('Shoot! It was so close too!')
			else:
				wobble_chance = floor(C * 100 * min(255, floor(floor(self.stats['chp'] * 255 / 8 if ball == "Great Ball" else 12) / max(1, floor(self.stats['hp'] / 4)))) / 255) + status
				if wobble_chance >= 0 and wobble_chance < 10: # No wobbles
					sp('The ball missed the Pokémon!')
				elif wobble_chance >= 10 and wobble_chance < 30: # 1 wobble
					sp('Darn! The Pokémon broke free!')
				elif wobble_chance >= 30 and wobble_chance < 70: # 2 wobbles
					sp('Aww! It appeared to be caught!')
				elif wobble_chance >= 70 and wobble_chance <= 100: # 3 wobbles
					sp('Shoot! It was so close too!')
			return False

# check if party is alive
def is_alive(self) -> bool:
	return any(not i.fainted for i in self)

# use item from bag
def use_item(battle=False) -> str: # type: ignore
	global save
	item_used = False
	sp('\nPlease choose an item to use.')
	if battle:
		sp('\n'.join(f'{key}: {save["bag"][key]}' for key in save['bag'] if items[key]['battle'])) # type: ignore
	else:
		sp('\n'.join(f'{key}: {save["bag"][key]}' for key in save['bag']))
	sp('[e] - Back\n')
	while not item_used:
		item = ''
		while not item:
			item = get()
		if item == "e":
			return "exit"
		if item in save['bag']:
			if save['bag'][item] > 0:
				save['bag'][item] -= 1
				# exec(items[item]['command']) # type: ignore
				return item
			else:
				sp('You have none of that item!')

# randomise escape
def escape(pokemon, opponent, escape_attempts) -> bool:
	return floor((pokemon.stats['spe'] * 32) / (floor(opponent.stats['spe'] / 4) % 256)) + 30 * escape_attempts > 255 or floor(opponent.stats['spe'] / 4) % 256 == 0

# calculate type effectiveness
def type_effectiveness(move, defender) -> float:
	return types[move['type'].upper()][defender.type] # type: ignore

# calculate prize money
def prize_money(self=None, type='Pokémon Trainer') -> int:
	return floor(trainer[type] * max(i.level for i in (save['party'] if self is None else self))) # type: ignore

# find moves of a wild pokemon
def find_moves(name, level) -> list:
	learned_moves = [{**move, "pp": list(filter(lambda m, move=move: m['name'] == move['name'], moves))[0]['pp']} for move in dex[name]['moves'] if move['level'] <= level] # type: ignore

	learned_moves = sorted(learned_moves, key=lambda m: m['level'], reverse=True)
	if len(learned_moves) >= 4:
		return list(map(lambda m: {"name": m['name'], "pp": m["pp"]}, learned_moves[:4]))
	else:
		return list(map(lambda m: {"name": m['name'], "pp": m["pp"]}, learned_moves))

# switch pokemon in battle
def switch_pokemon(party_length: int) -> Union[int, str]:
	sp(f'''\nWhich Pokémon should you switch to?\n\n{
				chr(10).join(f'{f"[{i+1}]" if not save["party"][i].check_fainted() else "FAINTED"} - {save["party"][i].name} ({save["party"][i].stats["chp"]}/{save["party"][i].stats["hp"]})' for i in range(party_length))
			}''')
	sp('[e] - Back\n')
	switch_choice = ''
	while not switch_choice:
		while switch_choice == '':
			switch_choice = get()
		if switch_choice == 'e':
			return 'exit'
		try:
			if switch_choice not in [str(i+1) for i in range(party_length)]:
				switch_choice = ''
				sp('\nInvalid choice.')
			elif save['party'][int(switch_choice)-1].check_fainted():
				switch_choice = ''
				sp('That Pokémon is fainted!')
		except (TypeError, ValueError):
			switch_choice = ''
			sp('\nInvalid choice.')
	return int(switch_choice)

# create battle process
def battle(opponent_party=None, battle_type='wild', name=None, title=None, start_diagloue=None, end_dialouge=None, earn_xp=True) -> None:
	global save
	debug('Entered battle!')
	debug(f'Party: {save["party"]}')
	party_length = len(save['party'])
	current = ''
	opponent_current = 0
	for i in range(party_length):
		if not save['party'][i].check_fainted():
			debug(f'{save["party"][i].name} is the first alive Pokemon in the party.')
			current = i
			break

	# battle intro
	if battle_type == 'trainer':
		sp(f'\n{name}: {start_diagloue}')
		sp(f'\n{title} {name} wants to fight!')
	elif battle_type == 'wild':
		sp(f'\nA wild {opponent_party[opponent_current].name} appeared!') # type: ignore
	else:
		abort('\nInvalid battle type: neither trainer nor wild.')
	sleep(0.5)
	sp(f'\nGo, {save["party"][current].name}!')
	sleep(0.5)
	if battle_type == 'trainer':
		sp(f'\n{name} sent out {opponent_party[opponent_current].name}!') # type: ignore

	# battle variables
	escaped_from_battle = False
	escape_attempts = 0
	caught = False
	catch_attempt = False
	switched = False
	participating_pokemon = [current]

	# check if parties are alive
	debug(f'\nPlayer party alive: {is_alive(save["party"])}\nOpponent party alive: {is_alive(opponent_party)}')

	# battle loop
	while is_alive(save['party']) and is_alive(opponent_party):

		# player turn
		debug('Turn start!')
		player_attacked_this_turn = False
		opponent_attacked_this_turn = False
		catch_attempt = False
		switched = False

		# calculate health bars according to ratio (chp:hp)
		bars = ceil((save['party'][current].stats['chp']/(save['party'][current].stats['hp']))*bars_length)
		opponent_bars = ceil((opponent_party[opponent_current].stats['chp']/(opponent_party[opponent_current].stats['hp']))*bars_length) # type: ignore
		debug(f'Player bars: {bars}\nOpponent bars: {opponent_bars}')
		debug(f'Player level: {save["party"][current].level}\nOpponent level: {opponent_party[opponent_current].level}') # type: ignore
		sp(f'''\n{save["party"][current].name}{' '*(name_length-len(save['party'][current].name))}[{'='*bars}{' '*(bars_length-bars)}] {str(save['party'][current].stats['chp'])}/{save['party'][current].stats['hp']} ({save["party"][current].type}) Lv. {save["party"][current].level}\n{opponent_party[opponent_current].name}{' '*(name_length-len(opponent_party[opponent_current].name))}[{'='*opponent_bars}{' '*(bars_length-opponent_bars)}] {opponent_party[opponent_current].stats['chp']}/{opponent_party[opponent_current].stats['hp']} ({opponent_party[opponent_current].type}) Lv. {opponent_party[opponent_current].level}''') # type: ignore
		sp(f'\nWhat should {save["party"][current].name} do?\n\n[1] - Attack\n[2] - Switch\n[3] - Item\n[4] - Run\n')

		valid_choice = False
		while not valid_choice:
			user_choice = get()
			if user_choice == '2' and len(save['party']) == 1:
				sp('You can\'t switch out your only Pokémon!')
			elif user_choice == '3' and len(save['bag']) == 0:
				sp('You have no items!')
			elif user_choice == '4' and battle_type == 'trainer':
				sp('You can\'t run from a trainer battle!')
			elif user_choice in ['1', '2', '3', '4']:
				valid_choice = True

		# choose attack
		if user_choice == '1': # type: ignore
			struggle = True
			for move_iter in save['party'][current].moves:
				if move_iter['pp'] > 0:
					struggle = False
			if struggle:
				sp(f'{save["party"][current].name} has no moves left!')
				chosen_move = {'name': 'struggle'}
			else:
				options = []
				sp('')
				move_names = []
				type_names = []
				for i in save['party'][current].moves:
					move_names.append(i['name'])
					type_names.append(list(filter(lambda m, i=i: m['name'] == i['name'], moves))[0]['type']) # type: ignore
				longest_move_name_length = len(max(move_names, key=len))
				longest_type_name_length = len(max(type_names, key=len))

				for i in range(len(save['party'][current].moves)):
					move_entry = list(filter(lambda m, i=i: m['name'] == save['party'][current].moves[i]['name'], moves))[0] # type: ignore
					sp(f'[{i+1}] - {save["party"][current].moves[i]["name"].upper().replace("-"," ")}{" "*(longest_move_name_length-len(save["party"][current].moves[i]["name"].upper().replace("-"," ")))} | {move_entry["type"].upper()}{" "*(longest_type_name_length-len(move_entry["type"].upper()))} - {save["party"][current].moves[i]["pp"]}/{move_entry["pp"]}')
					options.append(str(i+1))
				sp(f'[e] - Back\n')
				valid_choice = False
				while not valid_choice:
					move_choice = get()
					if move_choice in options:
						if save['party'][current].moves[int(move_choice)-1]['pp'] == 0:
							sp(f'{save["party"][current].name} cannot use {save["party"][current].moves[int(move_choice)-1]["name"]}')
						else: valid_choice = True
					elif move_choice == "e":
						valid_choice = True
				if move_choice == "e": # type: ignore
					continue

				chosen_move = save["party"][current].moves[int(move_choice)-1] # type: ignore

			if save['party'][current].stats['spe'] >= opponent_party[opponent_current].stats['spe']: # type: ignore
				damage = opponent_party[opponent_current].deal_damage(save['party'][current], chosen_move) # type: ignore
				if chosen_move["name"] == "struggle":
					save['party'][current].deal_struggle_damage(damage)
				else:
					save["party"][current].moves[int(move_choice)-1]['pp'] -= 1 # type: ignore

				player_attacked_this_turn = True

		# choose switch
		elif user_choice == '2': # type: ignore
			switch_choice = switch_pokemon(party_length)

			if switch_choice == "exit":
				continue

			if int(switch_choice)-1 == current:
				continue

			current = int(switch_choice)-1
			switched = True
			if int(switch_choice)-1 not in participating_pokemon:
				participating_pokemon.append(current)

		# choose item
		elif user_choice == '3': # type: ignore
			item = use_item(battle=True)
			if item == "exit":
				continue
			if (item == 'Poke Ball' or item == 'Great Ball' or item == 'Ultra Ball' or item == 'Master Ball') and battle_type == 'trainer':
				sp("You can't catch another trainer's Pokémon!")
			elif item == 'Poke Ball':
				if opponent_party[opponent_current].catch("Poke Ball"): # type: ignore
					caught = True
					break
				else: catch_attempt = True
			elif item == 'Great Ball':
				if opponent_party[opponent_current].catch("Great Ball"): # type: ignore
					caught = True
					break
				else: catch_attempt = True
			elif item == 'Ultra Ball':
				if opponent_party[opponent_current].catch("Ultra Ball"): # type: ignore
					caught = True
					break
				else: catch_attempt = True
			elif item == 'Master Ball':
				if opponent_party[opponent_current].catch("Master Ball"): # type: ignore
					caught = True
					break
				else: catch_attempt = True

		# choose run
		elif user_choice == '4': # type: ignore
			if escape(save['party'][current], opponent_party[opponent_current], escape_attempts): # type: ignore
				escaped_from_battle = True
				break
			else:
				escape_attempts += 1

		# reset consecutive escape attempts
		if user_choice != '4': # type: ignore
			escape_attempts = 0

		# opponent attack
		if is_alive(save['party']) and is_alive(opponent_party):
			save['party'][current].deal_damage(opponent_party[opponent_current], choice(opponent_party[opponent_current].moves)) # type: ignore
			opponent_attacked_this_turn = True

		# player attack if player speed is lower
		if is_alive(save['party']) and is_alive(opponent_party) and not player_attacked_this_turn and escape_attempts == 0 and not catch_attempt and not switched:
			damage = opponent_party[opponent_current].deal_damage(save['party'][current], chosen_move) # type: ignore
			if chosen_move["name"] == "struggle": # type: ignore
				save['party'][current].deal_struggle_damage(damage)
			else:
				save["party"][current].moves[int(move_choice)-1]['pp'] -= 1 # type: ignore
			player_attacked_this_turn = True

		# end battle if player wins
		elif is_alive(save['party']) and not is_alive(opponent_party):
			break

		elif save['party'][current].check_fainted():
			participating_pokemon = list(filter(lambda p, current=current: save['party'][p].name != save['party'][current].name, participating_pokemon))
			switch_choice = switch_pokemon(party_length)
			current = int(switch_choice)-1
			switched = True
			if int(switch_choice)-1 not in participating_pokemon:
				participating_pokemon.append(current)

		# display turn details
		debug(f'Higher Speed: {"Player" if save["party"][current].stats["spe"] > opponent_party[opponent_current].stats["spe"] else "Opponent"}\nPlayer Attacked: {player_attacked_this_turn}\nOpponent Attacked: {opponent_attacked_this_turn}\n') # type: ignore

	# upon escaping
	if escaped_from_battle:
		sp('You escaped!')

	# upon catching
	elif caught:
		pass # type: ignore

	# upon winning
	elif is_alive(save['party']) and not is_alive(opponent_party):
		if save['flag']['been_to_route_1']:
			if battle_type == 'trainer':
				sg(f'\n{save["party"][current].name} won the battle!')
				save['money'] += prize_money()
				sg(f'You recieved ¥{str(prize_money())} as prize money.')
			if earn_xp == True:
				total_xp = ceil(opponent_party[opponent_current].calculate_xp()) # type: ignore
				debug(f'total xp: {total_xp}')
				if 'EXP. All' in save['bag']:
					for p in participating_pokemon:
						save['party'][p].current_xp += floor(total_xp / (len(participating_pokemon) + 1))
						sg(f'{save["party"][p].name} gained {floor(total_xp / (len(participating_pokemon) + 1))} XP!')
						save['party'][p].check_level_up(save['party'])

					other_pokemon = []
					for i in save['party']:
						if i not in participating_pokemon: other_pokemon.append(i)
					for o in other_pokemon:
						save['party'][o].current_xp += floor((total_xp / (len(participating_pokemon) + 1)) / len(other_pokemon))
						sg(f'{save["party"][o].name} gained {floor((total_xp / (len(participating_pokemon) + 1)) / len(other_pokemon))} XP!')
						save['party'][o].check_level_up(save['party'])

				else:
					for p in participating_pokemon:
						save['party'][p].current_xp += floor(total_xp / len(participating_pokemon))
						sg(f'{save["party"][p].name} gained {floor(total_xp / len(participating_pokemon))} XP!')
						save['party'][p].check_level_up(save['party'])
					sp("")
				sleep(0.5)
			if battle_type == 'trainer':
				sp(f'\n{name}: {end_dialouge}')
				save['money'] += trainer[title] # type: ignore
				sp(f'You got ¥{trainer[title]}') # type: ignore
		else:
			save['flag']['won_first_battle'] = True

	# upon losing
	elif is_alive(opponent_party) and (not is_alive(save['party'])):
		if battle_type == 'trainer':
			if save['flag']['been_to_route_1']:
				save['money'] -= prize_money()
				sg('You lost the battle!')
				sg(f'You gave ¥{round(save["money"] / 2)} as prize money.')
			else:
				save['flag']['won_first_battle'] = False
		sg('...')
		sg(f'{save["name"]} blacked out!')
		save['money'] = round(save['money'] / 2)
		save['location'] = save['recent_center']
		heal()

	# if battle is neither won nor lost
	else:
		abort('\nInvalid battle state; neither won, lost, caught, nor escaped. Could not load player turn.')

# pokemon center heal
def heal(pokemon=None, party=None, type='party') -> None:
	global save
	if type == 'party':
		party = party or save['party']
	elif type == 'single':
		pokemon = pokemon or save['party'][0]
		party = [pokemon]
	else:
		abort('Invalid heal type: neither party nor single.')
	sp('')
	for i in party: # type: ignore
			i.reset_stats()
			sp(f'{i.name} was healed to max health.')

def get_encounter(loc, type) -> dict:
	pokemon = []
	weights = []
	for chance in rates[loc][type]: # type: ignore
		for i in range(len(rates[loc][type][chance])): # type: ignore
			pokemon.append(rates[loc][type][chance][i]) # type: ignore
			weights.append(int(chance)/255)
	return choices(pokemon, weights)[0]

def display_pokemart(loc) -> None: # sourcery skip: low-code-quality
	choice = ''
	action_choice = ''
	pokemart_exit = False
	while not pokemart_exit:
		while not action_choice:
			while not action_choice:
				sp("\n[b] - Buy\n[s] - Sell\n[e] - Back\n")
				action_choice = get()
			if action_choice not in ['b', 's', 'e']:
				action_choice = ''
		if action_choice == 'e':
			pokemart_exit = True
		elif action_choice == 's':
			sp(f'\nMoney: ¥{"{:,}".format(save["money"])}')
			while not choice:
				options = ['e']
				max_name_length = (len(max(pokemart[loc], key=len))) # type: ignore
				for i, item in enumerate(pokemart[loc], start=1): # type: ignore
					options.append(str(i))
					price_len = len("{:,}".format(items[item]["price"])) # type: ignore
					sp(f'[{i}] - {item}{" "*(max_name_length-len(item))}{" "*(8-price_len)}¥{"{:,}".format(items[item]["sell_price"])}') # type: ignore
				sp(f'[e] - Back\n')
				while not choice:
					choice = get()
				if choice not in options:
					choice = ''
			if choice == "e":
				action_choice = ''
				choice = ''
			else:
				amount = 0
				try:
					in_bag = save['bag'][pokemart[loc][int(choice)-1]] # type: ignore
				except KeyError:
					in_bag = 0
				sp(f'\n{pokemart[loc][int(choice)-1]}: ¥{"{:,}".format(items[pokemart[loc][int(choice)-1]]["sell_price"])} (in bag: {in_bag})') # type: ignore
				sp("Description coming soon")
				sp("How many would you like to sell(1-99)? (press 'e' to go back)\n")
				while not amount:
					while not amount:
						amount = get()
					if amount == 'e':
						break
					if (not amount.isnumeric()) or int(amount) > 99 or int(amount) < 1:
						amount = ''
				if amount == 'e':
					choice = ''
					amount = ''
				elif in_bag < int(amount):
					sp(f'\nYou do not have enough items (you need {int(amount)-in_bag} more)')
					amount = ''
				else:
					save['bag'][pokemart[loc][int(choice)-1]] -= int(amount) # type: ignore
					save['money'] += items[pokemart[loc][int(choice)-1]]["sell_price"]*int(amount) # type: ignore
					debug(f'Sold {amount} {pokemart[loc][int(choice)-1]}s for ¥{items[pokemart[loc][int(choice)-1]]["sell_price"]*int(amount)}') # type: ignore
					choice = ''

		elif action_choice == 'b':
			sp(f'\nMoney: ¥{"{:,}".format(save["money"])}')
			while not choice:
				options = ['e']
				max_name_length = (len(max(pokemart[loc], key=len))) # type: ignore
				for i, item in enumerate(pokemart[loc], start=1): # type: ignore
					options.append(str(i))
					price_len = len("{:,}".format(items[item]["price"])) # type: ignore
					sp(f'[{i}] - {item}{" "*(max_name_length-len(item))}{" "*(8-price_len)}¥{"{:,}".format(items[item]["price"])}') # type: ignore
				sp(f'[e] - Back\n')
				while not choice:
					choice = get()
				if choice not in options:
					choice = ''
			if choice == "e":
				action_choice = ''
				choice = ''
			else:
				amount = 0
				try:
					in_bag = save['bag'][pokemart[loc][int(choice)-1]] # type: ignore
				except KeyError:
					in_bag = 0

				sp(f'\n{pokemart[loc][int(choice)-1]}: ¥{"{:,}".format(items[pokemart[loc][int(choice)-1]]["price"])} (in bag: {in_bag})') # type: ignore
				sp("Description coming soon")
				sp("How many would you like to buy(1-99)? (press 'e' to go back)\n")
				while not amount:
					while not amount:
						amount = get()
					if amount == 'e':
						break
					if (not amount.isnumeric()) or int(amount) > 99 or int(amount) < 1:
						amount = ''
				if amount == 'e':
					choice = ''
					amount = ''
				else:
					required_money = items[pokemart[loc][int(choice)-1]]["price"]*int(amount) # type: ignore
					if required_money > save['money']:
						sp(f'\nYou do not have enough money (you need ¥{required_money-save["money"]} more)')
						amount = ''
					else:
						if pokemart[loc][int(choice)-1] not in save['bag']: # type: ignore
							save['bag'][pokemart[loc][int(choice)-1]] = int(amount) # type: ignore
						else:
							save['bag'][pokemart[loc][int(choice)-1]] += int(amount) # type: ignore
						save['money'] -= required_money
						sp(f'\n{save["name"]} obtained {amount} {pokemart[loc][int(choice)-1]}(s)') # type: ignore
						choice = ''

# display title screen
cls() # type: ignore
title = ['''\n                                  ,'\\\n    _.----.        ____         ,'  _\   ___    ___     ____\n_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.\n\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |\n \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |\n   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |\n     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |\n      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |\n       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |\n        \_.-'       |__|    `-._ |              '-.|     '-.| |   |\n                                `'                            '-._|\n''', '                          PythonRed Version\n', '                       Press any key to begin!'] # type: ignore
title.append(f'{title[0]}\n{title[1]}\n{title[2]}\n\n')
sleep(1)
print(title[0])
sleep(2.65)
print(title[1])
sleep(1.85)
print(title[2])
getch() # type: ignore
cls() # type: ignore
print(f'{title[3]}Please choose an option.\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')
start_option = ''
while start_option != '2':
	start_option = get()
	cls() # type: ignore

	# continue from save file
	if start_option == '1':
		try:
			if path.isfile(path.join(syspath[0], '.ppr-save')) and loads(open(path.join(syspath[0], '.ppr-save')).read())['flag']['has_saved']:
				cls() # type: ignore
				print(f'{title[3]}Loading save file!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n\n> 1\n')
				break
		except KeyError:
			print(f'{title[3]}Your save file is outdated and the game cannot load it. Please back up your save file and contact us with option [3].\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')
		else:
			print(f'{title[3]}No previous save file found!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	# new game
	elif start_option == '2':
		cls() # type: ignore
		print(f'{title[3]}Starting game!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	# open github link
	elif start_option == '3':
		try:
			webopen(link['repository'], new=2, autoraise=True)
		except Exception:
			print(f'{title[3]}Failed to open website, here\'s the link:\n[{link["repository"]}]\n')
		else:
			print(f'{title[3]}Repository page opened successfully!')
		finally:
			print('\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	# handle invalid input
	else:
		print(f'{title[3]}Invalid input!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

# load data from files
for i in [
	['dex', 'dex.json'],
	['items', 'item.json'],
	['moves', 'moves.json'],
	['rates', 'map.json'],
	['save_template', 'save_template.json'],
	['trainer', 'trainer.json'],
	['types', 'types.json'],
	['xp', 'level.json'],
	['pokemart', 'pokemart.json']
]:
	try:
		exec(f'{i[0]} = loads(open(path.join(syspath[0], "data", "{i[1]}"), encoding="utf8").read())\nopen(path.join(syspath[0], "data", "{i[1]}")).close()')
	except Exception:
		abort(f'Failed to load {i[1]}!')

# debug statements
def debug(text) -> None:
	if is_debug:
		sp(f'{colours["GROUND"]}Debug: {text}{colours["RESET"]}')

# load save file
if start_option == '1':
	save_temp = {**save_template, **loads(open(path.join(syspath[0], '.ppr-save'), 'r').read())} # type: ignore
	open(path.join(syspath[0], '.ppr-save')).close()
	save = save_temp
	for pokemon_location in ['party', 'box']:
		save[pokemon_location] = [Pokemon(species=i['species'], level=i['level'], ivs=i['ivs'], moves=i['moves'], chp=i['stats']['chp'], current_xp=i['current_xp'], fainted=i['fainted'], player_pokemon=True) for i in save_temp[pokemon_location]]
else:
	save = save_template # type: ignore
	save['badges'] = {i: False for i in badges}
	save['options']['text_speed'] = 'normal'
if getuser() not in save['user']:
	save['user'].append(getuser())
is_debug = save['options']['debug']

# test party status (debug)
if start_option == '1':
	for i in range(len(save['party'])):
		debug(f'{type(save["party"][i])}')

# check for illegal save data
try:
	if max([
		len(save['name']) > 15,
		len(save['party']) > 6,
		save['flag']['been_to_route_1'] and len(save['party']) == 0,
		save['flag']['chosen_starter'] and not save['flag']['intro_complete'],
		save['flag']['chosen_starter'] and save['location'] == '',
		save['name'] != '' and not save['flag']['intro_complete'],
		save['name'] != save['name'].upper(),
		save['name'] == '' and save['flag']['intro_complete']
	]):
		abort('Illegal or outdated save data detected!')
except KeyError:
	abort('Illegal or outdated save data detected!')

# reset getch according to options
reset_sp(text[save['options']['text_speed']])

# main loop
while not exit:
	option = dex_string = ''

	# intro
	if save['flag']['intro_complete'] == False:
		sp('(Intro Start!)\n')
		sg('OAK: Hello there! Welcome to the world of Pokémon!')
		sg('My name is OAK! People call me the Pokémon Professor!')
		sg('This world is inhabited by creatures called Pokémon!')
		sg('For some people, Pokémon are pets. Others use them for fights. Myself...')
		sg('I study Pokémon as a profession.')
		sp('\nFirst, what is your name?\n\n[1] - PYTHON\n[2] - New Name\n')
		introAnswer = ''
		while introAnswer not in ['1', '2']:
			introAnswer = get()
		if introAnswer == '1':
			playerName = 'PYTHON'
		elif introAnswer == '2':
			sp('\n(Caps, 15 chars. max)\n')
			playerName = get()
			while len(playerName) > 15 or playerName == '':
				playerName = get()
		else:
			sp('\nInvalid answer!')
		playerName = playerName.upper() # type: ignore
		sg(f'\nRight! So your name is {playerName}!')
		sg('\nNow, since you\'re so raring to go, I\'ve prepared a rival for you.')
		sg('He will go on an adventure just like yours, and battle you along the way.')
		sp('\n...Erm, what is his name again?\n')
		get()
		sg('\n...')
		sg('Hoho, just kidding! His name is JOHNNY! You\'ll meet him soon!\n')
		sg(f'{playerName}! Your very own Pokémon legend is about to unfold! A world of dreams and adventures with Pokémon awaits! Let\'s go!')
		save['name'] = playerName
		save['location'] = 'playerHouseUp'
		save['flag']['intro_complete'] = True
		sp('\n(Intro Complete!)')

	# options menu
	elif options_open == True:
		sp('Options Menu\n[1] - Text Speed\n[2] - EMPTY\n[3] - EMPTY\n[4] - Back\n')
		while not option:
			option = get()
		if option == '1':
			option = ''
			while option != '5':
				sp('\nText Speed\n[1] - Slow\n[2] - Normal\n[3] - Fast\n[4] - Ultra\n[5] - Back\n')
				option = ''
				while (not option) and option not in ['1', '2', '3', '4', '5']:
					option = get()
				if option != '5':
					sp('')
				if option == '1':
					save['options']['text_speed'] = 'slow'
					sp('Text Speed set to Slow!')
				elif option == '2':
					save['options']['text_speed'] = 'normal'
					sp('Text Speed set to Normal!')
				elif option == '3':
					save['options']['text_speed'] = 'fast'
					sp('Text Speed set to Fast!')
				elif option == '4':
					save['options']['text_speed'] = 'ultra'
					sp('Text Speed set to Ultra!')
				reset_sp(text[save['options']['text_speed']])
		elif option in ['2', '3']:
			sp('Coming Soon!')
		elif option == '4':
			options_open = False
		else:
			sp('\nInvalid answer!')

	# pause menu
	elif menu_open == True:
		menu = f'Menu\n[d] - Pokédex\n[p] - Pokémon\n[i] - Item\n[t] - {save["name"]}\n[s] - Save Game\n[o] - Options\n[e] - Exit Menu\n[q] - Quit Game\n' if 'Pokedex' in save['bag'] else f'Menu\n[p] - Pokémon\n[i] - Item\n[t] - {save["name"]}\n[s] - Save Game\n[o] - Options\n[e] - Exit Menu\n[q] - Quit Game\n'
		sp(menu)
		while not option:
			option = get()
		if option not in ['e', 'o']:
			sp('')
		if option == 'd' and 'Pokedex' in save['bag']:
			option = ''
			dex_string = ''
			for i in dex.keys(): # type: ignore
				if i in save['dex'].keys():
					dex_string += f'\n{dex[i]["index"]} - {i}: Seen' if save['dex'][i]['seen'] else '' # type: ignore
					if save['dex'][i]['caught']:
						dex_string += ', Caught'
			sp(f'{save["name"]}\'s Pokédex{dex_string}' if dex_string else '\nYou have no Pokémon in your Pokédex!')
		elif option == 'p':
			if save['party']:
				sp('\n'.join(f'{i.name} ({i.type}-type)\nLevel {i.level} ({i.current_xp}/{str(xp["next"][i.level_type][str(i.level)])} XP to next level)\n{i.stats["chp"]}/{i.stats["hp"]} HP' for i in save['party'])) # type: ignore
			else:
				sp('Your party is empty!')
		elif option == 'i':
			if save['bag']:
				for i in save['bag']:
					sp(f'{i}: {save["bag"][i]}')
			else:
				sp('Your bag is empty!')
		elif option == 't':
			sp(f'Name: {save["name"]}')
			sp(f'Money: ¥{"{:,}".format(save["money"])}')
			sp(f'''Badges: {''.join(f"[{'x' if save['badges'][i] else ' '}]" for i in badges)}''')
		elif option == 's':
			backup()
		elif option == 'o':
			options_open = True
		elif option == 'e':
			menu_open = False
		elif option == 'q':
			sp('Are you sure you want to quit? Any unsaved progress will be lost. (Y/N)\n')
			option = ''
			while option not in yn:
				option = get()
			if option in y:
				exit = True
		else:
			sp('\nInvalid answer!')
		if option not in ['e', 'i', 'o', 'p', 's']:
			sp('')

	# player house - upstairs
	elif save['location'] == 'playerHouseUp':
		sp(f'Current Location: {save["name"]}\'s Room (Upstairs)\n\n[s] - Go Downstairs\n[1] - Computer\n[2] - Notebook\n')
		while option == '':
			option = get()
		if option == '1':
			sg('\n...')
			sg('Looks like you can\'t use it yet.')
		elif option == '2':
			sg('\nThe notebook is open to a page that says:\n\n"Use the [m] command in the overworld to open the menu.\nFrom the menu, you can save your progress, check your Pokémon, and more!"')
		elif option == 's':
			save['location'] = 'playerHouseDown'
		elif option == 'm':
			menu_open = True
		else:
			sp('\nInvalid answer!')

	# player house - downstairs
	elif save['location'] == 'playerHouseDown':
		sp(f'Current Location: {save["name"]}\'s House (Downstairs)\n\n[w] - Go Upstairs\n[d] - Go Outside\n')
		while option == '':
			option = get()
		if option == 'd':
			save['location'] = 'pallet'
		elif option == 'w':
			save['location'] = 'playerHouseUp'
		elif option == 'm':
			menu_open = True
		else:
			sp('\nInvalid answer!')

	# pallet town
	elif save['location'] == 'pallet':
		sp(f'Current Location: Pallet Town - "Shades of your journey await!"\n\n[w] - Go to Route 1\n[a] - Go to {save["name"]}\'s House\n[s] - Go to Sea-Route 21\n[d] - Go to OAK\'s LAB\n')
		while option == '':
			option = get()
		if option == 'w':
			if save['flag']['chosen_starter']:
				save['location'] = 'route1-s'
			else:
				sg('\nYou take a step into the tall grass north of Pallet Town.')
				sg('...')
				sg('Suddenly, you hear a voice shouting from behind you.')
				sg('\nOAK: Hey! Wait! Don\'t go out!')
				sg('\nProfessor OAK runs up to you from behind.')
				sg('\nOAK: It\'s unsafe! Wild Pokémon live in tall grass! You need your own Pokémon for protection. Come with me!')
				sg('\nProfessor OAK leads you to his laboratory. He walks up to a table with three Poké Balls on it.')
				sg(f'\nOAK: Here, {save["name"]}! There are three Pokémon here, reserved for new trainers.')
				while not save['flag']['chosen_starter']:
					sp('Go ahead and choose one!\n\n[1] - Bulbasaur\n[2] - Charmander\n[3] - Squirtle\n')
					option = ''
					while not option and option not in ['1', '2', '3']:
						option = get()
					if option in ['1', '2', '3']:
						sp(f'\nDo you want the {["GRASS", "FIRE", "WATER"][int(option)-1]}-type Pokémon, {["Bulbasaur", "Charmander", "Squirtle"][int(option)-1]}? (Y/N)\n')
						confirm = ''
						while confirm not in yn:
							confirm = get()
						if confirm in y:
							save['flag']['chosen_starter'] = True
							save['starter'] = ['BULBASAUR', 'CHARMANDER', 'SQUIRTLE'][int(option)-1]
							save['dex'] = {save['starter']: {'seen': True, 'caught': True}}
							save['flag']['type'] = {dex[save['starter']]['type']: {'seen': True, 'caught': True}} # type: ignore
							for i in [('BULBASAUR', 'CHARMANDER'), ('CHARMANDER', 'SQUIRTLE'), ('SQUIRTLE', 'BULBASAUR')]:
								if save['starter'] == i[0]:
									save['rivalStarter'] = i[1]
							save['party'].append(Pokemon(save['starter'], 5, {
								'hp': 31,
								'atk': 31,
								'def': 31,
								'spa': 31,
								'spd': 31,
								'spe': 31
							}, find_moves(save['starter'], 5) ))
						else:
							sp('')
				sg(f'\nOAK: {save["starter"]} looks really energetic!')
				sg('\nJust as you turn to leave, another young trainer enters the lab.')
				sg(f'\nOAK: Ah, JOHNNY! Perfect timing! {save["name"]} here has just chosen a Pokémon! Why don\'t you choose one too?')
				sg(f'\nJOHNNY walks up to the table and thinks for a few seconds, before picking up a Poké Ball containing {save["rivalStarter"].upper()}.')
				sg(f'\nOAK: {save["starter"]} and {save["rivalStarter"]} are both brilliant choices!')
				sg('\nJOHNNY nods to you, then turns to walk away. But, before he does, Professor OAK calls him back.')
				sg(f'\nOAK: JOHNNY! Why don\'t you battle {save["name"]} before you go?')
				sg('\nJOHNNY stops and looks at you over his shoulder, as if he doesn\'t understand.')
				sg('\n...Suddenly, he gives a smile and tosses his Poké Ball into the air!')
				battle([Pokemon(save['rivalStarter'], 5, 'random', find_moves(save['rivalStarter'], 5))], battle_type='trainer', name='JOHNNY', start_diagloue='...', title='Pokémon Trainer', end_dialouge='...')
				sg(f'\nOAK: A marvellous battle! Congratulations, {save["name"] if save["flag"]["won_first_battle"] else "JOHNNY"}!')
				sg('Let me heal your Pokémon for you.')
				heal()
				sg('\nOAK: You can make your Pokémon stronger by training on Route 1.')
				sg('\nJOHNNY tips his hat to you before taking his leave of the Lab.')
				sg('You notice that he\'s heading North.')
				save['location'] = 'oakLab'
		elif option == 'a':
			save['location'] = 'playerHouseDown'
		elif option == 's':
			sg('\nThe water is a deep, clear blue.')
			if save['hms']['surf']:
				sp('\n...Would you like to use Surf? (Y/N)')
				option = ''
				while option not in yn:
					option = input('\n> ')
				if option in y:
					save['location'] = 'seaRoute21'
				else:
					sg('\nYou decided not to use Surf.')
		elif option == 'd':
			if save['flag']['chosen_starter']:
				save['location'] = 'oakLab'
			else:
				sg('\n...')
				sg('It appears to be locked.')
		elif option == 'm':
			menu_open = True
		else:
			sp('\nInvalid answer!')

	# oak's lab
	elif save['location'] == 'oakLab':
		sp('Current Location: OAK\'s Lab\n\n[a] - Go to Pallet Town\n[1] - Lab Assistant (Left)\n[2] - Lab Assistant (Right)\n[3] - Professor OAK\n[4] - OAK\'s Computer\n')
		while option == '':
			option = get()
		if option == 'a':
			save['location'] = 'pallet'
		elif option == '1':
			sg('\nASSISTANT: I study Pokémon as Professor OAK\'s aide.')
		elif option == '2':
			sg('\nASSISTANT: Professor OAK is an authority on Pokémon!')
			sg('Many Pokémon trainers hold him in high regard!')
		elif option == '3':
			if 'Oak\'s Parcel' in save['bag']:
				sg(f'\nOAK: Oh, {save["name"]}! How is my old Pokémon? Well, it seems to like you a lot.')
				sg('You must be talented as a Pokémon trainer!')
				sg('\n(You hold the parcel out to Professor OAK.)')
				sg('\nOAK: What? You have something for me?')
				sg(f'\n{save["name"]} delivered Oak\'s Parcel.')
				save['flag']['delivered_package'] = True
				save['bag'].pop('Oak\'s Parcel')
				sg('OAK: Ah! This is the custom POKE BALL I ordered! Thank you!')
				sg('\nJust at that moment, JOHNNY enters the building. OAK notices and calls him over.')
				sg('\nOAK: JOHNNY! You\'re just in time!')
				sg('I have a request of you two.')
				sg('On the desk there is my invention, POKEDEX!')
				sg('It automatically records data on Pokémon you\'ve seen or caught, like a hi-tech encyclopedia!')
				sg(f'\n{save["name"]} and JOHNNY! Take these with you!')
				sg(f'({save["name"]} obtained the POKEDEX!)')
				save['bag']['Pokedex'] = 1
				sg('\nOAK: To make a complete guide on all the Pokémon in the world...')
				sg('That was my dream! But, I\'m too old! I can\'t do it!')
				sg('So, I want you two to fulfill my dream for me!')
				sg('Get moving, you two! This is a great undertaking in Pokémon history!')
				sg('\nJOHNNY nods and takes his leave.')
				sg(f'\nOAK: Pokémon around the world wait for you, {save["name"]}!')
			else:
				sg('\nOAK: You\'ve caught a total of...')
				sg(f'\n{sum(1 if save["dex"][i]["caught"] else 0 for i in save["dex"])} Pokémon!')
		elif option == '4':
			sg('\nThere\' an email message here:')
			sg('"Calling all Pokémon trainers!\nThe elite trainers of Pokémon League are ready to take on all comers! Bring your best Pokémon and see how you rate as a trainer!\nPokémon LEAGUE HQ INDIGO PLATEAU\nPS: Professor OAK, please visit us!"')
		elif option == 'm':
			menu_open = True
		else:
			sp('\nInvalid answer!')

	# route 1 - south
	elif save['location'] == 'route1-s':
		if not save['flag']['been_to_route_1']: save['flag']['been_to_route_1'] = True
		sp('Current Location: Route 1 (South)\n\n[w] - Go to Route 1 (North)\n[s] - Go to Pallet Town\n')
		while option == '':
			option = get()
		if option == 'w':
			save['location'] = 'route1-n'
			encounter = get_encounter('route1-n', 'tall-grass')
			battle([Pokemon(encounter['pokemon'], encounter['level'], 'random')])
		elif option == 's':
			save['location'] = 'pallet'
		elif option == 'm':
			menu_open = True
		else:
			sp('\nInvalid answer!')

	# route 1 - north
	elif save['location'] == 'route1-n':
		sp('Current Location: Route 1 (North)\n\n[w] - Go to Viridian City (South)\n[s] - Go to Route 1 (South)\n')
		while option == '':
			option = get()
		if option == 'w':
			save['location'] = 'viridian-s'
		elif option == 's':
			save['location'] = 'route1-s'
			encounter = get_encounter('route1-s', 'tall-grass')
			battle([Pokemon(encounter['pokemon'], encounter['level'], 'random')])
		elif option == 'm':
			menu_open = True
		else:
			sp('\nInvalid answer!')

	# viridian city - south
	elif save['location'] == 'viridian-s':
		sp('Current Location: Viridian City (South)\n\n[w] - Go to Viridian City (North)\n[a] - Go to Route 22 (East)\n[s] - Go to Route 1 (North)\n[1] - Viridian Pokémon Centre\n[2] - Viridian Pokémart\n')
		while option == '':
			option = get()
		if option == 'w':
			if save['flag']['delivered_package']:
				sg('\nComing soon!') # will become: save['location'] = 'viridian-n'
			else:
				sg('\nAn old man is blocking the way, accompanied by an apologetic young lady.')
				sg('\nMAN: Hey you, get off my property!')
				sg('\nGIRL: Oh, grandpa! Don\'t be so mean!')
				sg('\nIt looks like you won\'t be able to pass until later.')
		elif option == 'a':
			sg('\nComing soon!')
		elif option == 's':
			save['location'] = 'route1-n'
		elif option == '1':
			heal()
			save['recent_center'] = 'viridian-s'
		elif option == '2':
			if save['flag']['delivered_package']:
				display_pokemart('viridian')
			elif 'Oak\'s Parcel' in save['bag']:
				sg('\nCLERK: Please deliver Oak\'s Parcel!')
			else:
				sg('\nCLERK: Hey! You came from PALLET TOWN? You know Professor OAK, right?')
				sg('His order came in. Will you take it to him?')
				save['bag']['Oak\'s Parcel'] = 1
				sg(f'\n({save["name"]} recieved Oak\'s Parcel!)\n')
				sg('\nCLERK: Okay! Say hi to the Professor for me!')
		elif option == 'm':
			menu_open = True

	# invalid location
	else:
		abort(f'The location "{save["location"]}" is not a valid location.')

	# end of loop
	if not dex_string:
		sp('')

# end program
