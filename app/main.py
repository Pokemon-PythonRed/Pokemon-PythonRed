# import system modules
from datetime import datetime
from getpass import getuser
from json import dumps, loads
from math import ceil, floor, sqrt
from os import path, system, remove
from platform import system as platform
from random import choice, choices, randint
from string import Formatter
from sys import exit as sysexit, path as syspath, stdout
from time import sleep, time
from typing import Optional, Union
from webbrowser import open as webopen

# import folderspace files
try:
	from abort_early import abort_early
	from data_opener import dex, save_template, xp
	from handling import abort, debug
	from input import exit, get, getch, getche, menu_open, options_open, y, yn
	from output import cls, link, reset_sp, sg, sp, text, text_speed
	from pokemon import badges, battle, display_pokemart, display_trainers, find_moves, get_encounter, heal, Pokemon, trainer_interaction
	from saving import backup
except ImportError as e:
	input(f'\n{e}.\n\nPlease see [https://github.com/Pokemon-PythonRed/Pokemon-PythonRed#installation] for more information.\n\nPress Enter to exit.\n')
	sysexit()

# import installed modules
from jsons import dump, load
from pygame.mixer import music

# set default text speed
reset_sp(speed=text[text_speed])

# load screen
sp('Loading...')

# clear screen
try:
	cls()
except NameError:
	abort_early()

# enables ANSI escape codes in Windows
system('')

# display title screen
cls()
title = ['''\n                                  ,'\\\n    _.----.        ____         ,'  _\\   ___    ___     ____\n_,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.\n\\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  |\n \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |\n   \\    \\/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n    \\     ,-'/  /   \\    ,'   | \\/ / ,`.|         /  /   \\  |     |\n     \\    \\ |   \\_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    |\n      \\    \\ \\      /       `-.`.___,-' |  |\\  /| \\      /  | |   |\n       \\    \\ `.__,'|  |`-._    `|      |__| \\/ |  `.__,'|  | |   |\n        \\_.-'       |__|    `-._ |              '-.|     '-.| |   |\n                                `'                            '-._|\n''', '                          PythonRed Version\n', '                       Press any key to begin!'] 
title.append(f'{title[0]}\n{title[1]}\n{title[2]}\n\n')
sleep(1)
print(title[0])
sleep(2.65)
print(title[1])
sleep(1.85)
print(title[2])
getch()
cls()
print(f'{title[3]}Please choose an option.\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')
start_option = ''
while start_option != '2':
	start_option = get()
	cls()

	# continue from save file
	if start_option == '1':
		try:
			has_saved = loads(open(path.join(syspath[0], '.ppr-save')).read())['flag']['has_saved']
			if path.isfile(path.join(syspath[0], '.ppr-save')) and has_saved:
				cls()
				print(f'{title[3]}Loading save file!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n\n> 1\n')
				break
		except KeyError:
			print(f'{title[3]}Your save file is outdated and the game cannot load it. Please back up your save file and contact us with option [3].\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')
		except ValueError:
			print(f'{title[3]}Your save file is empty and cannot be loaded!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')
		else:
			print(f'{title[3]}No previous save file found!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	# new game
	elif start_option == '2':
		cls()
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

# load save file
if start_option == '1':
	save_temp = {**save_template, **loads(open(path.join(syspath[0], '.ppr-save'), 'r').read())}
	open(path.join(syspath[0], '.ppr-save')).close()
	save = save_temp
	for pokemon_location in ['party', 'box']:
		save[pokemon_location] = [Pokemon(save, species=i['species'], level=i['level'], ivs=i['ivs'], moves=i['moves'], chp=i['stats']['chp'], current_xp=i['current_xp'], fainted=i['fainted'], player_pokemon=True) for i in save_temp[pokemon_location]]
else:
	save = save_template
	save['badges'] = {i: False for i in badges}
	save['options']['text_speed'] = 'normal'
if getuser() not in save['user']:
	save['user'].append(getuser())
is_debug = save['options']['debug']

# test party status (debug)
if start_option == '1':
	for i in range(len(save['party'])):
		debug(f'{save["party"][i].name} is type {type(save["party"][i])}')

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
		intro_answer = player_name = ''
		while intro_answer not in ['1', '2']:
			intro_answer = get()
		if intro_answer == '1':
			player_name = 'PYTHON'
		elif intro_answer == '2':
			sp('\n(Caps, 15 chars. max)\n')
			player_name = get()
			while len(player_name) > 15 or player_name == '':
				player_name = get()
		else:
			sp('\nInvalid answer!')
		player_name = player_name.upper()
		sg(f'\nRight! So your name is {player_name}!')
		sg('\nNow, since you\'re so raring to go, I\'ve prepared a rival for you.')
		sg('He will go on an adventure just like yours, and battle you along the way.')
		sp('\n...Erm, what is his name again?\n')
		get()
		sg('\n...')
		sg('Hoho, just kidding! His name is JOHNNY! You\'ll meet him soon!\n')
		sg(f'{player_name}! Your very own Pokémon legend is about to unfold! A world of dreams and adventures with Pokémon awaits! Let\'s go!')
		save['name'] = player_name
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
			for i in dex.keys():
				if i in save['dex'].keys():
					dex_string += f'\n{dex[i]["index"]} - {i}: Seen' if save['dex'][i]['seen'] else ''
					if save['dex'][i]['caught']:
						dex_string += ', Caught'
			sp(f'{save["name"]}\'s Pokédex{dex_string}' if dex_string else '\nYou have no Pokémon in your Pokédex!')
		elif option == 'p':
			if save['party']:
				sp('\n'.join(f'{i.name} (`{i.type}`-type)\nLevel {i.level} ({i.current_xp}/{str(xp["next"][i.level_type][str(i.level)])} XP to next level)\n{i.stats["chp"]}/{i.stats["hp"]} HP' for i in save['party']))
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
			backup(save)
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
				encounter = get_encounter('route1-s', 'tall-grass')
				battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
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
						sp(f'\nDo you want the `{["GRASS", "FIRE", "WATER"][int(option)-1]}`-type Pokémon, {["Bulbasaur", "Charmander", "Squirtle"][int(option)-1]}? (Y/N)\n')
						confirm = ''
						while confirm not in yn:
							confirm = get()
						if confirm in y:
							save['flag']['chosen_starter'] = True
							save['starter'] = ['BULBASAUR', 'CHARMANDER', 'SQUIRTLE'][int(option)-1]
							save['dex'] = {save['starter']: {'seen': True, 'caught': True}}
							save['flag']['type'] = {dex[save['starter']]['type']: {'seen': True, 'caught': True}}
							for i in [('BULBASAUR', 'CHARMANDER'), ('CHARMANDER', 'SQUIRTLE'), ('SQUIRTLE', 'BULBASAUR')]:
								if save['starter'] == i[0]:
									save['rivalStarter'] = i[1]
							save['party'].append(Pokemon(save, save['starter'], 5, {
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
				battle(save, [Pokemon(save, save['rivalStarter'], 5, {}, find_moves(save['rivalStarter'], 5))], battle_type='trainer', name='JOHNNY', start_diagloue='...', title='Pokémon Trainer', end_dialouge='...')
				sg(f'\nOAK: A marvellous battle! Congratulations, {save["name"] if save["flag"]["won_first_battle"] else "JOHNNY"}!')
				sg('Let me heal your Pokémon for you.')
				heal(save)
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
		trainer_options = display_trainers(save, save['location'])
		while option == '':
			option = get()
		if option == 'w':
			save['location'] = 'route1-n'
			encounter = get_encounter('route1-n', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 's':
			save['location'] = 'pallet'
		elif option == 'm':
			menu_open = True
		elif option in trainer_options:
			trainer_interaction(save, save['location'], option)
		else:
			sp('\nInvalid answer!')

	# route 1 - north
	elif save['location'] == 'route1-n':
		sp('Current Location: Route 1 (North)\n\n[w] - Go to Viridian City\n[s] - Go to Route 1 (South)\n')
		trainer_options = display_trainers(save, save['location'])
		while option == '':
			option = get()
		if option == 'w':
			save['location'] = 'viridian'
		elif option == 's':
			save['location'] = 'route1-s'
			encounter = get_encounter('route1-s', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 'm':
			menu_open = True
		elif option in trainer_options:
			trainer_interaction(save, save['location'], option)
		else:
			sp('\nInvalid answer!')

	# viridian city
	elif save['location'] == 'viridian':
		sp('Current Location: Viridian City\n\n[w] - Go to Route 2 (South)\n[a] - Go to Route 22 (East)\n[s] - Go to Route 1 (North)\n[1] - Viridian Pokémon Centre\n[2] - Viridian Pokémart\n[3] - Viridian Pokemon Gym\n')
		while option == '':
			option = get()
		if option == 'w':
			if save['flag']['delivered_package']:
				save['location'] = 'route2-s'
				encounter = get_encounter('route2-s', 'tall-grass')
				battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
			else:
				sg('\nAn old man is blocking the way, accompanied by an apologetic young lady.')
				sg('\nMAN: Hey you, get off my property!')
				sg('\nGIRL: Oh, grandpa! Don\'t be so mean!')
				sg('\nIt looks like you won\'t be able to pass until later.')
		elif option == 'a':
			sg('\nComing soon!')
		elif option == 's':
			save['location'] = 'route1-n'
			encounter = get_encounter('route1-n', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == '1':
			heal(save)
			save['recent_center'] = 'viridian'
		elif option == '2':
			if save['flag']['delivered_package']:
				display_pokemart(save, 'viridian')
			elif 'Oak\'s Parcel' in save['bag']:
				sg('\nCLERK: Please deliver Oak\'s Parcel!')
			else:
				sg('\nCLERK: Hey! You came from PALLET TOWN? You know Professor OAK, right?')
				sg('His order came in. Will you take it to him?')
				save['bag']['Oak\'s Parcel'] = 1
				sg(f'\n({save["name"]} recieved Oak\'s Parcel!)\n')
				sg('\nCLERK: Okay! Say hi to the Professor for me!')
		elif option == '3':
			if save['badges']['Boulder'] and save['badges']['Cascade'] and save['badges']['Volcano'] and save['badges']['Marsh'] and save['badges']['Rainbow'] and save['badges']['Soul'] and save['badges']['Thunder']:
				save['location'] = 'viridian-gym'
			else:
				sg("\nThe gym is closed")
				sg('\nYou won\'t be able to enter until later.')
		elif option == 'm':
			menu_open = True

	elif save['location'] == 'route2-s':
		sp('Current Location: Route 2 (South)\n\n[w] - Go to Viridian Forest (South)\n[s] - Go to Viridian City\n[d] - Go to Route 2 (North)\n')
		trainer_options = display_trainers(save, save['location'])
		while option == '':
			option = get()
		if option == 'w':
			save['location'] = 'viridian-forest-s'
			encounter = get_encounter('viridian-forest-s', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 's':
			save['location'] = 'viridian'
		elif option == 'd':
			if save['hms']['cut']:
				save['location'] = 'route2-w'
			else:
				sg('\nThere is a tree in the way')
				sg('\nMaybe a Pokémon could cut it down?')
		elif option in trainer_options:
			trainer_interaction(save, save['location'], option)
		elif option == 'm':
			menu_open = True

	elif save['location'] == 'viridian-forest-s':
		sp('Current Location: Viridian Forest (South)\n\n[a] - Go to Viridian Forest (West)\n[s] - Go to Route 2 (South)\n[d] - Go to Viridian Forest (East)\n')
		trainer_options = display_trainers(save, save['location'])
		while option == '':
			option = get()
		if option == 's':
			save['location'] = 'route2-s'
			encounter = get_encounter('route2-s', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 'a':
			save['location'] = 'viridian-forest-w'
			encounter = get_encounter('viridian-forest-w', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 'd':
			save['location'] = 'viridian-forest-e'
			encounter = get_encounter('viridian-forest-e', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option in trainer_options:
			trainer_interaction(save, save['location'], option)
		elif option == 'm':
			menu_open = True

	elif save['location'] == 'viridian-forest-w':
		sp('Current Location: Viridian Forest (West)\n\n[w] - Go to Viridian Forest (North)\n[s] - Go to Viridian Forest (South)\n[d] - Go to Viridian Forest (East)\n')
		trainer_options = display_trainers(save, save['location'])
		while option == '':
			option = get()
		if option == 's':
			save['location'] = 'viridian-forest-s'
			encounter = get_encounter('viridian-forest-s', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 'w':
			save['location'] = 'viridian-forest-n'
			encounter = get_encounter('viridian-forest-n', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 'd':
			save['location'] = 'viridian-forest-e'
			encounter = get_encounter('viridian-forest-e', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option in trainer_options:
			trainer_interaction(save, save['location'], option)
		elif option == 'm':
			menu_open = True

	elif save['location'] == 'viridian-forest-e':
		sp('Current Location: Viridian Forest (East)\n\n[w] - Go to Viridian Forest (North)\n[s] - Go to Viridian Forest (South)\n[a] - Go to Viridian Forest (West)\n')
		trainer_options = display_trainers(save, save['location'])
		while option == '':
			option = get()
		if option == 's':
			save['location'] = 'viridian-forest-s'
			encounter = get_encounter('viridian-forest-s', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 'w':
			save['location'] = 'viridian-forest-n'
			encounter = get_encounter('viridian-forest-n', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 'a':
			save['location'] = 'viridian-forest-w'
			encounter = get_encounter('viridian-forest-w', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option in trainer_options:
			trainer_interaction(save, save['location'], option)
		elif option == 'm':
			menu_open = True

	elif save['location'] == 'viridian-forest-n':
		sp('Current Location: Viridian Forest (North)\n\n[w] - Go to Route 2 (North)\n[a] - Go to Viridian Forest (West)\n[d] - Go to Viridian Forest (East)\n')
		trainer_options = display_trainers(save, save['location'])
		while option == '':
			option = get()
		if option == 'w':
			save['location'] = 'route2-n'
			encounter = get_encounter('route2-n', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 'a':
			save['location'] = 'viridian-forest-w'
			encounter = get_encounter('viridian-forest-w', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option == 'd':
			save['location'] = 'viridian-forest-e'
			encounter = get_encounter('viridian-forest-e', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option in trainer_options:
			trainer_interaction(save, save['location'], option)
		elif option == 'm':
			menu_open = True

	elif save['location'] == "route2-n":
		sp('Current Location: Route 2 (North)\n\n[w] - Go to Pewter City\n[s] - Go to Viridian Forest (North)\n')
		trainer_options = display_trainers(save, save['location'])
		while option == '':
			option = get()
		if option == 'w':
			sg("Coming soon") # Will become save['location'] = 'pewter'
		elif option == 's':
			save['location'] = 'viridian-forest-n'
			encounter = get_encounter('viridian-forest-n', 'tall-grass')
			battle(save, [Pokemon(save, encounter['pokemon'], encounter['level'], {})])
		elif option in trainer_options:
			trainer_interaction(save, save['location'], option)
		elif option == 'm':
			menu_open = True

	# invalid location
	else:
		abort(f'The location "{save["location"]}" is not a valid location.')

	# end of loop
	if not dex_string:
		sp('')

# end program
