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
from random import choice, randint
# TODO: from string import ...
from sys import exit as sysexit, path as syspath, stdout
from time import sleep
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
system("")

# type colours
colours = {
	"NORMAL"  : "\x1b[0;0m",
	"FIRE"	  : "\x1b[38;5;196m",
	"WATER"   : "\x1b[38;5;027m",
	"GRASS"	  : "\x1b[38;5;082m",
	"ELECTRIC": "\x1b[38;5;184m",
	"ICE"	  : "\x1b[38;5;159m",
	"FIGHTING": "\x1b[38;5;167m",
	"POISON"  : "\x1b[38;5;135m",
	"GROUND"  : "\x1b[38;5;215m",
	"FLYING"  : "\x1b[38;5;183m",
	"PSYCHIC" : "\x1b[38;5;198m",
	"BUG"	  : "\x1b[38;5;028m",
	"ROCK"	  : "\x1b[38;5;179m",
	"GHOST"	  : "\x1b[38;5;126m",
	"DRAGON"  : "\x1b[38;5;057m",
	"DARK"    : "\x1b[38;5;095m",
	"STEEL"   : "\x1b[38;5;250m",
	"FAIRY"   : "\x1b[38;5;212m",
	"RESET"	  : "\x1b[0;0m" 
}

# error message
def abort(message) -> None:
	print(f'\n\n\n- - - INTERNAL ERROR - - -\n\nERROR MESSAGE: {message}\n\nIf you have not edited any files, feel free to create an issue on the repository by going to the link below.\n\nNote: your save file will be preserved in the program folder. Any unsaved progress will be lost (sorry).\n\n[{link["issue"]}]\n\nPress Enter to exit.')
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
		save['flag']['hasSaved'] = True
		save_temp = save
		save_temp['party'] = [dump(i) for i in save['party']]
		save_temp['box'] = [dump(i) for i in save['box']]
		save_temp['lastPlayed'] = None # TODO: save time last played
		open(path.join(syspath[0], '.ppr-save'), 'w').write(f'{dumps(save_temp, indent=4, sort_keys=True)}\n')
		sp('\nGame saved successfully!')

# pokemon class
class Pokemon:

	# set internals
	def __init__(self, species, level, ivs, chp=None, attack_type=None, current_xp=0, fainted=False) -> None:
		self.species = species
		self.index = dex[self.species]['index'] # type: ignore
		self.name = dex[self.species]['name'] # type: ignore
		self.type = dex[self.species]['type'] # type: ignore
		self.level = level
		self.ivs = ivs if ivs != 'random' else {i: randint(0, 31) for i in ['hp', 'atk', 'def', 'spa', 'spd', 'spe']}
		self.atk_type = attack_type or choice(['physical', 'special'])
		self.level_type = dex[self.species]['xp'] # type: ignore
		self.total_xp = xp['total'][self.level_type][str(self.level)] # type: ignore
		self.current_xp = current_xp

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
		self.reset_stats(chp, fainted)

	# reset stats
	def reset_stats(self, chp=None, fainted=None) -> None:
			self.stats = {
				'hp': floor(((dex[self.species]['hp'] + self.ivs['hp']) * 2 + floor(ceil(sqrt(self.ivs['hp'])) / 4) * self.level) / 100) + self.level + 10, # type: ignore
				'atk': floor(((dex[self.species]['atk'] + self.ivs['atk']) * 2 + floor(ceil(sqrt(self.ivs['atk'])) / 4) * self.level) / 100) + 5, # type: ignore
				'def': floor(((dex[self.species]['def'] + self.ivs['def']) * 2 + floor(ceil(sqrt(self.ivs['def'])) / 4) * self.level) / 100) + 5, # type: ignore
				'spa': floor(((dex[self.species]['spa'] + self.ivs['spa']) * 2 + floor(ceil(sqrt(self.ivs['spa'])) / 4) * self.level) / 100) + 5, # type: ignore
				'spd': floor(((dex[self.species]['spd'] + self.ivs['spd']) * 2 + floor(ceil(sqrt(self.ivs['spd'])) / 4) * self.level) / 100) + 5, # type: ignore
				'spe': floor(((dex[self.species]['spe'] + self.ivs['spe']) * 2 + floor(ceil(sqrt(self.ivs['spe'])) / 4) * self.level) / 100) + 5 # type: ignore
			}
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
	def deal_damage(self, attacker) -> None:
		sp(f'\n{attacker.name} used a {colours[attacker.type]}{attacker.type}{colours["RESET"]}-type attack on {self.name}!')
		critical = randint(0, 255) <= 17
		attack_defense = ('atk', 'def') if attacker.atk_type == 'physical' else ('spa', 'spd')
		damage = floor((((((2 * attacker.level / 5)+ 2) * 100 * attacker.stats[attack_defense[0]] / self.stats[attack_defense[1]]) / 50) + 2) * (1.5 if critical else 1) * randint(85, 100) / 100 * (type_effectiveness(attacker, self) if save['flag']['beenToRoute1'] else 1))
		self.stats['chp'] -= damage
		sp(f'\n{attacker.name} dealt {damage} damage to {self.name}!')
		if critical:
			sp('A critical hit!')
		for i in [
			(0, 'It had no effect!'),
			(0.5, 'It\'s super effective!'),
			(2, 'It\'s not very effective!')
		]:
			if types[self.type][attacker.type] == i[0]:
				sp(f'{i[1]}')
		self.check_fainted()
		if self.fainted:
			sp(f'\n{self.name} fainted!')

	# calculate xp rewarded after battle
	def calculate_xp(self, attacker, battle_type='wild') -> int:
		return (xp['total'][attacker.level_type][str(attacker.level)] * attacker.level * (1 if battle_type == 'wild' else 1.5)) / 7 # type: ignore

	# level up pokemon in context of battle
	def give_xp(self, attacker, battle_type='wild') -> None:
		self.current_xp += ceil(self.calculate_xp(attacker, battle_type))
		sg(f'\n{self.name} gained {self.calculate_xp(attacker, battle_type)} XP!')
		while self.current_xp >= xp['next'][self.level_type][self.level]: # type: ignore
			self.current_xp -= xp['next'][self.level_type][self.level] # type: ignore
			self.level_up(self)
			if self.level == 100:
				sp(f'\nCongratulations, {self.name} has reached level 100!')
				break

	# raw level up
	def level_up(self, pokemon):
		pokemon.level += 1
		pokemon.reset_stats()
		sp(f'{pokemon.name} grew to level {pokemon.level}!')

# catch Pokemon
def catch(pokemon) -> None:
	global save
	location = 'party' if len(save['party']) < 6 else 'box'
	save[location].append(pokemon)
	if pokemon.species not in save['dex']:
		save['dex'].update({pokemon.species: {'seen': True, 'caught': True}})
	else:
		if 'seen' not in save['dex'][pokemon.species]:
			save['dex'][pokemon.species]['seen'] = True
		if 'caught' not in save['dex'][pokemon.species]:
			save['dex'][pokemon.species]['caught'] = True
	if pokemon.type not in save['flag']['type']:
		save['flag']['type'].update({pokemon.type: {'seen': True, 'caught': True}})
	else:
		if 'seen' not in save['flag']['type'][pokemon.type]:
			save['flag']['type'][pokemon.species]['seen'] = True
		if 'caught' not in save['flag']['type'][pokemon.type]:
			save['flag']['type'][pokemon.species]['caught'] = True
	sg(f'\nYou caught {pokemon.name}!')
	sg(f'\n{pokemon.name} ({colours[pokemon.type]}{pokemon.type}{colours["RESET"]}-type) was added to your {location}.')

# check if party is alive
def is_alive(self) -> bool:
	return any(not i.fainted for i in self)

# use item from bag
def use_item():
	global save
	item_used = False
	sp('\nPlease choose an item to use.')
	sp('\n'.join(f'{key}: {val}' for key, val in save['bag']))
	while not item_used:
		item = ''
		while not item:
			item = get()
		if item in save['bag']:
			if save['bag'][item] > 0:
				save['bag'][item] -= 1
				exec(items[item]['command']) # type: ignore
			else:
				sp('You have none of that item!')

# randomise escape
def escape(pokemon, opponent, escape_attempts) -> bool:
	return floor((pokemon.stats['spe'] * 32) / (floor(opponent.stats['spe'] / 4) % 256)) + 30 * escape_attempts > 255 or floor(opponent.stats['spe'] / 4) % 256 == 0

# calculate type effectiveness
def type_effectiveness(attacker, defender) -> float:
	return types[attacker.type][defender.type] # type: ignore

# calculate prize money
def prize_money(self=None, type='Pokémon Trainer') -> int:
	return floor(trainer[type] * max(i.level for i in (save['party'] if self is None else self))) # type: ignore

# create battle process
def battle(opponent_party=None, battle_type='wild', name=None, title=None, start_diagloue=None, end_dialouge=None, earn_xp=True) -> None:
	global save
	debug('Entered battle!')
	party_length = len(save['party'])
	current = ''
	opponent_current = 0
	for i in range(party_length):
		while not current:
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

	# check if parties are alive
	debug(f'\nPlayer party alive: {is_alive(save["party"])}\nOpponent party alive: {is_alive(opponent_party)}')

	# battle loop
	while is_alive(save['party']) and is_alive(opponent_party):

		# player turn
		debug('Turn start!')
		player_attacked_this_turn = False
		opponent_attacked_this_turn = False

		# calculate health bars according to ratio (chp:hp)
		bars = ceil((save['party'][current].stats['chp']/(save['party'][current].stats['hp']))*bars_length)
		opponent_bars = ceil((opponent_party[opponent_current].stats['chp']/(opponent_party[opponent_current].stats['hp']))*bars_length) # type: ignore
		debug(f'Player bars: {bars}\nOpponent bars: {opponent_bars}')
		debug(f'Player level: {save["party"][current].level}\nOpponent level: {opponent_party[opponent_current].level}') # type: ignore
		sp(f'''\n{save["party"][current].name}{' '*(name_length-len(save['party'][current].name))}[{'='*bars}{' '*(bars_length-bars)}] {str(save['party'][current].stats['chp'])}/{save['party'][current].stats['hp']} ({colours[save["party"][current].type]}{save["party"][current].type}{colours["RESET"]}) Lv. {save["party"][current].level}\n{opponent_party[opponent_current].name}{' '*(name_length-len(opponent_party[opponent_current].name))}[{'='*opponent_bars}{' '*(bars_length-opponent_bars)}] {opponent_party[opponent_current].stats['chp']}/{opponent_party[opponent_current].stats['hp']} ({colours[opponent_party[opponent_current].type]}{opponent_party[opponent_current].type}{colours["RESET"]}) Lv. {opponent_party[opponent_current].level}''') # type: ignore
		#sp(f'''\n{save["party"][current].name}{' '*(name_length-len(save['party'][current].name))}[{'='*bars}{' '*(bars_length-bars)}] {str(save['party'][current].stats['chp'])}/{save['party'][current].stats['hp']} ({save["party"][current].type}) Lv. {save["party"][current].level}\n{opponent_party[opponent_current].name}{' '*(name_length-len(opponent_party[opponent_current].name))}[{'='*opponent_bars}{' '*(bars_length-opponent_bars)}] {opponent_party[opponent_current].stats['chp']}/{opponent_party[opponent_current].stats['hp']} ({opponent_party[opponent_current].type}) Lv. {opponent_party[opponent_current].level}''') # type: ignore
		sp(f'\nWhat should {save["party"][current].name} do?\n\n[1] - Attack\n[2] - Switch\n[3] - Item\n[4] - Run\n')
		valid_choice = False
		while not valid_choice:
			choice = get()
			if choice == '2' and len(save['party']) == 1:
				sp('You can\'t switch out your only Pokémon!')
			elif choice == '3' and len(save['bag']) == 0:
				sp('You have no items!')
			elif choice == '4' and battle_type == 'trainer':
				sp('You can\'t run from a trainer battle!')
			elif choice in ['1', '2', '3', '4']:
				valid_choice = True

		# choose attack
		if choice == '1': # type: ignore
			if save['party'][current].stats['spe'] >= opponent_party[opponent_current].stats['spe']: # type: ignore
				opponent_party[opponent_current].deal_damage(save['party'][current]) # type: ignore
				player_attacked_this_turn = True

		# choose switch
		elif choice == '2': # type: ignore
			sp(f'''\nWhich Pokémon should you switch to?\n\n{
				''.join(f'{f"[{i+1}]" if not save["party"][i].check_fainted() else "FAINTED"} - {save["party"][i].name} ({save["party"][i].stats["chp"]}/{save["party"][i].stats["hp"]})' for i in range(party_length))
			}''')
			switch_choice = ''
			while not switch_choice:
				while switch_choice == '':
					switch_choice = get()
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
			current = int(switch_choice)-1

		# choose item
		elif choice == '3': # type: ignore
			use_item()

		# choose run
		elif choice == '4': # type: ignore
			if escape(save['party'][current], opponent_party[opponent_current], escape_attempts): # type: ignore
				escaped_from_battle = True
				break
			else:
				escape_attempts += 1

		# reset consecutive escape attempts
		if choice != '4': # type: ignore
			escape_attempts = 0

		# opponent attack
		if is_alive(save['party']) and is_alive(opponent_party):
			save['party'][current].deal_damage(opponent_party[opponent_current]) # type: ignore
			opponent_attacked_this_turn = True

		# player attack if player speed is lower
		if is_alive(save['party']) and is_alive(opponent_party) and not player_attacked_this_turn:
			opponent_party[opponent_current].deal_damage(save['party'][current]) # type: ignore
			player_attacked_this_turn = True

		# end battle if player wins
		elif is_alive(save['party']) and not is_alive(opponent_party):
			break

		# display turn details
		debug(f'Higher Speed: {"Player" if save["party"][current].stats["spe"] > opponent_party[opponent_current].stats["spe"] else "Opponent"}\nPlayer Attacked: {player_attacked_this_turn}\nOpponent Attacked: {opponent_attacked_this_turn}\n') # type: ignore

	# upon winning
	if escaped_from_battle:
		sp('You escaped!')
	if is_alive(save['party']) and not is_alive(opponent_party):
		if save['flag']['beenToRoute1']:
			if battle_type == 'trainer':
				sp(f'\n{save["party"][current].name} won the battle!')
			if earn_xp == True:
				save['party'][current].current_xp += ceil(save['party'][current].calculate_xp(opponent_party[opponent_current])) # type: ignore
				save['party'][current].check_level_up(save['party'])
				sleep(0.5)
			if battle_type == 'trainer':
				sp(f'\n{name}: {end_dialouge}')
				save['money'] += trainer[title] # type: ignore
				sp(f'You got ¥{trainer[title]}') # type: ignore
		else:
			save['flag']['wonFirstBattle'] = True

	# upon losing
	elif is_alive(opponent_party) and (not is_alive(save['party'])):
		if battle_type == 'trainer':
			if save['flag']['beenToRoute1']:
				save['money'] -= prize_money()
				sg('You lost the battle!')
				sg(f'You gave ¥{str(prize_money())} as prize money.')
			else:
				save['flag']['wonFirstBattle'] = False
		sg('...')
		sg(f'{save["name"]} blacked out!')
		save['location'] = save['recentCenter']
		heal()

	# if battle is neither won nor lost
	else:
		abort('\nInvalid battle state; neither won, lost, nor escaped. Could not load player turn.')

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
		if path.isfile(path.join(syspath[0], '.ppr-save')) and loads(open(path.join(syspath[0], '.ppr-save')).read())['flag']['hasSaved']:
			cls() # type: ignore
			print(f'{title[3]}Loading save file!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n\n> 1\n')
			break
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
	['save_template', 'save_template.json'],
	['trainer', 'trainer.json'],
	['types', 'types.json'],
	['xp', 'level.json']
]:
	try:
		exec(f'{i[0]} = loads(open(path.join(syspath[0], "data", "{i[1]}")).read())\nopen(path.join(syspath[0], "data", "{i[1]}")).close()')
	except Exception:
		abort(f'Failed to load {i} data!')

# debug statements
def debug(text) -> None:
	if is_debug:
		sp(f'DEBUG: {text}')

# load save file
if start_option == '1':
	save_temp = {**save_template, **loads(open(path.join(syspath[0], '.ppr-save'), 'r').read())} # type: ignore
	open(path.join(syspath[0], '.ppr-save')).close()
	save = save_temp
	for pokemon_location in ['party', 'box']:
		save[pokemon_location] = [Pokemon(i['species'], i['level'], i['ivs'], i['stats']['chp'], i['atk_type'], i['current_xp'], i['fainted']) for i in save_temp[pokemon_location]]
else:
	save = save_template # type: ignore
	save['badges'] = {i: False for i in badges}
	save['options']['textSpeed'] = 'normal'
if getuser() not in save['user']:
	save['user'].append(getuser())
is_debug = save['options']['debug']

# test party status (debug)
if start_option == '1':
	for i in range(len(save['party'])):
		debug(f'{type(save["party"][i])}')

# check for illegal save data
if max([
	len(save['name']) > 15,
	len(save['party']) > 6,
	save['flag']['beenToRoute1'] and len(save['party']) == 0,
	save['flag']['chosenStarter'] and not save['flag']['introComplete'],
	save['flag']['chosenStarter'] and save['location'] == '',
	save['name'] != '' and not save['flag']['introComplete'],
	save['name'] != save['name'].upper(),
	save['name'] == '' and save['flag']['introComplete']
]):
	abort('Illegal save data detected!')

# reset getch according to options
reset_sp(text[save['options']['textSpeed']])

# main loop
while not exit:
	option = dex_string = ''

	# intro
	if save['flag']['introComplete'] == False:
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
		save['flag']['introComplete'] = True
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
					save['options']['textSpeed'] = 'slow'
					sp('Text Speed set to Slow!')
				elif option == '2':
					save['options']['textSpeed'] = 'normal'
					sp('Text Speed set to Normal!')
				elif option == '3':
					save['options']['textSpeed'] = 'fast'
					sp('Text Speed set to Fast!')
				elif option == '4':
					save['options']['textSpeed'] = 'ultra'
					sp('Text Speed set to Ultra!')
				reset_sp(text[save['options']['textSpeed']])
		elif option in ['2', '3']:
			sp('Coming Soon!')
		elif option == '4':
			options_open = False
		else:
			sp('\nInvalid answer!')

	# pause menu
	elif menu_open == True:
		sp(f'Menu\n[d] - Pokédex\n[p] - Pokémon\n[i] - Item\n[t] - {save["name"]}\n[s] - Save Game\n[o] - Options\n[e] - Exit Menu\n[q] - Quit Game\n')
		while not option:
			option = get()
		if option not in ['e', 'o']:
			sp('')
		if option == 'd':
			option = ''
			dex_string = ''.join(
				f'\n{dex[i]["index"]} - {i}: Seen{", Caught" if save["dex"][i]["caught"] else ""}' if save['dex'][i]['seen'] else '' for i in save['dex'] # type: ignore
			)
			sp(f'{save["name"]}\'s Pokédex{dex_string}' if dex_string else '\nYou have no Pokémon in your Pokédex!')
		elif option == 'p':
			if save['party']:
				sp('\n'.join(f'{i.name} ({colours[i.type]}{i.type}{colours["RESET"]}-type)\nLevel {i.level} ({i.current_xp}/{str(xp["next"][i.level_type][str(i.level)])} XP to next level)\n{i.stats["chp"]}/{i.stats["hp"]} HP' for i in save['party'])) # type: ignore
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
			if save['flag']['chosenStarter']:
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
				while not save['flag']['chosenStarter']:
					sp('Go ahead and choose one!\n\n[1] - Bulbasaur\n[2] - Charmander\n[3] - Squirtle\n')
					option = ''
					while not option and option not in ['1', '2', '3']:
						option = get()
					if option in ['1', '2', '3']:
						sp(f'\nDo you want the {[colours["GRASS"], colours["FIRE"], colours["WATER"]][int(option)-1]}{["GRASS", "FIRE", "WATER"][int(option)-1]}{colours["RESET"]}-type Pokémon, {["Bulbasaur", "Charmander", "Squirtle"][int(option)-1]}? (Y/N)\n')
						confirm = ''
						while confirm not in yn:
							confirm = get()
						if confirm in y:
							save['flag']['chosenStarter'] = True
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
							}))
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
				battle([Pokemon(save['rivalStarter'], 5, 'random')], battle_type='trainer', name='JOHNNY', start_diagloue='...', title='Pokémon Trainer', end_dialouge='...')
				sg(f'\nOAK: A marvellous battle! Congratulations, {save["name"] if save["flag"]["wonFirstBattle"] else "JOHNNY"}!')
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
			if save['flag']['chosenStarter']:
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
			sg('\nOAK: You\'ve caught a total of...')
			sg(f'\n{sum(1 if save["dex"][i]["caught"] else 0 for i in save["dex"])} Pokémon!')
		elif option == '4':
			sg('\nThere\' an email message here:')
			sg('"Calling all Pokémon trainers!\nThe elite trainers of Pokémon League are ready to take on all comers! Bring your best Pokémon and see how you rate as a trainer!\nPOKEMON LEAGUE HQ INDIGO PLATEAU\nPS: Professor OAK, please visit us!"')
		elif option == 'm':
			menu_open = True
		else:
			sp('\nInvalid answer!')

	# route 1 - south
	elif save['location'] == 'route1-s':
		if not save['flag']['beenToRoute1']: save['flag']['beenToRoute1'] = True
		sp('Current Location: Route 1 (South)\n\n[w] - Go to Route 1 (North)\n[s] - Go to Pallet Town\n')
		while option == '':
			option = get()
		if option == 'w':
			save['location'] = 'route1-n'
			battle([Pokemon(choice(['PIDGEY', 'SPEAROW', 'RATTATA', 'BELLSPROUT']), randint(1, 5), 'random')])
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
			battle([Pokemon(choice(['PIDGEY', 'SPEAROW', 'RATTATA', 'BELLSPROUT']), randint(1, 5), 'random')])
		elif option == 'm':
			menu_open = True
		else:
			sp('\nInvalid answer!')

	# viridian city - south
	elif save['location'] == 'viridian-s':
		sp('Current Location: Viridian City (South)\n\n[w] - Go to Viridian City (North)\n[a] - Go to Route 22 (East)\n[s] - Go to Route 1 (North)\n[d] - Viridian Pokémon Centre\n')
		while option == '':
			option = get()
		if option == 'w':
			if save['flag']['deliveredPackage']:
				save['location'] = 'viridian-n'
			else:
				sg('\nAn old man is blocking the way, accompanied by an apologetic young lady.')
				sg('\nMAN: Hey you, get off my property!')
				sg('\nGIRL: Oh, grandpa! Don\'t be so mean!')
				sg('\nIt looks like you won\'t be able to pass until later.')
		elif option == 'a':
			sg('\nComing soon!')
		elif option == 's':
			save['location'] = 'route1-n'
		elif option == 'd':
			heal()
			save['recentCenter'] = 'viridian-s'
		elif option == 'm':
			menu_open = True

	# invalid location
	else:
		abort(f'The location "{save["location"]}" is not a valid location.')

	# end of loop
	if not dex_string:
		sp('')

# end program
