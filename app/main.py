# import system modules
from contextlib import suppress
from copy import deepcopy
from datetime import datetime
from getpass import getuser
from importlib import import_module
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
	from data_opener import dex, items, locations, moves, rates, save_template, trainer_types, types, xp, pokemart, trainers
	from event_opener import Event
	from handling import abort, debug
	from input import exit_status, get, getch, getche, menu_open, options_open, y, yn
	from location_opener import Location
	from output import cls, link, reset_sp, sp, text, text_speed
	from pokemon import badges, battle, display_pokemart, display_trainers, find_moves, get_encounter, heal, Pokemon, trainer_interaction
	from saving import SaveFile
except ImportError as e:
	input(f'\n{e}.\n\nPlease see [https://github.com/Pokemon-PythonRed/Pokemon-PythonRed#installation] for more information.\n\nPress Enter to exit.\n')
	sysexit()

# import installed modules
from jsons import dump, load
from pygame.mixer import music

# set default text speed
reset_sp(speed=text[text_speed])

# load screen
sp([('Loading...', False)])

# clear screen
try:
	cls()
except NameError:
	abort_early()

# enables ANSI escape codes in Windows
system('')

# TODO: test title screen event
save = Event('title').execute(SaveFile(save_exists=False))

# reset getch according to options
reset_sp(text[save['options']['text_speed']])

# intro
if save['flag']['intro_complete'] == False:
	save = Event('intro').execute(save)

# main loop
while not exit_status:
	save['location'] = Location(save['location']).execute()

# TODO: translate everything below this point into `data/locations.json` and `events/*.py`
	if False:

		# options menu
		if options_open == True:
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

		# player house - upstairs
		elif save['location'] == 'playerhouse-up':
			sp(f'Current Location: {save["name"]}\'s Room (Upstairs)\n\n[s] - Go Downstairs\n[1] - Computer\n[2] - Notebook\n')
			while option == '':
				option = get()
			if option == '1':
				sg('\n...')
				sg('Looks like you can\'t use it yet.')
			elif option == '2':
				sg('\nThe notebook is open to a page that says:\n\n"Use the [m] command in the overworld to open the menu.\nFrom the menu, you can save your progress, check your Pokémon, and more!"')
			elif option == 's':
				save['location'] = 'playerhouse-down'
			elif option == 'm':
				menu_open = True
			else:
				sp('\nInvalid answer!')

		# player house - downstairs
		elif save['location'] == 'playerhouse-down':
			sp(f'Current Location: {save["name"]}\'s House (Downstairs)\n\n[w] - Go Upstairs\n[d] - Go Outside\n')
			while option == '':
				option = get()
			if option == 'd':
				save['location'] = 'pallet'
			elif option == 'w':
				save['location'] = 'playerhouse-up'
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
					battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
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
					battle([Pokemon(save['rivalStarter'], 5, {}, find_moves(save['rivalStarter'], 5))], battle_type='trainer', name='JOHNNY', start_diagloue='...', title='Pokémon Trainer', end_dialouge='...')
					sg(f'\nOAK: A marvellous battle! Congratulations, {save["name"] if save["flag"]["won_first_battle"] else "JOHNNY"}!')
					sg('Let me heal your Pokémon for you.')
					heal(save)
					sg('\nOAK: You can make your Pokémon stronger by training on Route 1.')
					sg('\nJOHNNY tips his hat to you before taking his leave of the Lab.')
					sg('You notice that he\'s heading North.')
					save['location'] = 'oak-lab'
			elif option == 'a':
				save['location'] = 'playerhouse-down'
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
					save['location'] = 'oak-lab'
				else:
					sg('\n...')
					sg('It appears to be locked.')
			elif option == 'm':
				menu_open = True
			else:
				sp('\nInvalid answer!')

		# oak's lab
		elif save['location'] == 'oak-lab':
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
			trainer_options = display_trainers(save['location'])
			while option == '':
				option = get()
			if option == 'w':
				save['location'] = 'route1-n'
				encounter = get_encounter('route1-n', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 's':
				save['location'] = 'pallet'
			elif option == 'm':
				menu_open = True
			elif option in trainer_options:
				trainer_interaction(save['location'], option)
			else:
				sp('\nInvalid answer!')

		# route 1 - north
		elif save['location'] == 'route1-n':
			sp('Current Location: Route 1 (North)\n\n[w] - Go to Viridian City\n[s] - Go to Route 1 (South)\n')
			trainer_options = display_trainers(save['location'])
			while option == '':
				option = get()
			if option == 'w':
				save['location'] = 'viridian'
			elif option == 's':
				save['location'] = 'route1-s'
				encounter = get_encounter('route1-s', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 'm':
				menu_open = True
			elif option in trainer_options:
				trainer_interaction(save['location'], option)
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
					battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
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
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == '1':
				heal(save)
				save['recent_center'] = 'viridian'
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
			trainer_options = display_trainers(save['location'])
			while option == '':
				option = get()
			if option == 'w':
				save['location'] = 'viridian-forest-s'
				encounter = get_encounter('viridian-forest-s', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 's':
				save['location'] = 'viridian'
			elif option == 'd':
				if save['hms']['cut']:
					save['location'] = 'route2-w'
				else:
					sg('\nThere is a tree in the way')
					sg('\nMaybe a Pokémon could cut it down?')
			elif option in trainer_options:
				trainer_interaction(save['location'], option)
			elif option == 'm':
				menu_open = True

		elif save['location'] == 'viridian-forest-s':
			sp('Current Location: Viridian Forest (South)\n\n[a] - Go to Viridian Forest (West)\n[s] - Go to Route 2 (South)\n[d] - Go to Viridian Forest (East)\n')
			trainer_options = display_trainers(save['location'])
			while option == '':
				option = get()
			if option == 's':
				save['location'] = 'route2-s'
				encounter = get_encounter('route2-s', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 'a':
				save['location'] = 'viridian-forest-w'
				encounter = get_encounter('viridian-forest-w', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 'd':
				save['location'] = 'viridian-forest-e'
				encounter = get_encounter('viridian-forest-e', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option in trainer_options:
				trainer_interaction(save['location'], option)
			elif option == 'm':
				menu_open = True

		elif save['location'] == 'viridian-forest-w':
			sp('Current Location: Viridian Forest (West)\n\n[w] - Go to Viridian Forest (North)\n[s] - Go to Viridian Forest (South)\n[d] - Go to Viridian Forest (East)\n')
			trainer_options = display_trainers(save['location'])
			while option == '':
				option = get()
			if option == 's':
				save['location'] = 'viridian-forest-s'
				encounter = get_encounter('viridian-forest-s', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 'w':
				save['location'] = 'viridian-forest-n'
				encounter = get_encounter('viridian-forest-n', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 'd':
				save['location'] = 'viridian-forest-e'
				encounter = get_encounter('viridian-forest-e', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option in trainer_options:
				trainer_interaction(save['location'], option)
			elif option == 'm':
				menu_open = True

		elif save['location'] == 'viridian-forest-e':
			sp('Current Location: Viridian Forest (East)\n\n[w] - Go to Viridian Forest (North)\n[s] - Go to Viridian Forest (South)\n[a] - Go to Viridian Forest (West)\n')
			trainer_options = display_trainers(save['location'])
			while option == '':
				option = get()
			if option == 's':
				save['location'] = 'viridian-forest-s'
				encounter = get_encounter('viridian-forest-s', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 'w':
				save['location'] = 'viridian-forest-n'
				encounter = get_encounter('viridian-forest-n', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 'a':
				save['location'] = 'viridian-forest-w'
				encounter = get_encounter('viridian-forest-w', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option in trainer_options:
				trainer_interaction(save['location'], option)
			elif option == 'm':
				menu_open = True

		elif save['location'] == 'viridian-forest-n':
			sp('Current Location: Viridian Forest (North)\n\n[w] - Go to Route 2 (North)\n[a] - Go to Viridian Forest (West)\n[d] - Go to Viridian Forest (East)\n')
			trainer_options = display_trainers(save['location'])
			while option == '':
				option = get()
			if option == 'w':
				save['location'] = 'route2-n'
				encounter = get_encounter('route2-n', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 'a':
				save['location'] = 'viridian-forest-w'
				encounter = get_encounter('viridian-forest-w', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option == 'd':
				save['location'] = 'viridian-forest-e'
				encounter = get_encounter('viridian-forest-e', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option in trainer_options:
				trainer_interaction(save['location'], option)
			elif option == 'm':
				menu_open = True

		elif save['location'] == "route2-n":
			sp('Current Location: Route 2 (North)\n\n[w] - Go to Pewter City\n[s] - Go to Viridian Forest (North)\n')
			trainer_options = display_trainers(save['location'])
			while option == '':
				option = get()
			if option == 'w':
				sg("Coming soon") # Will become save['location'] = 'pewter'
			elif option == 's':
				save['location'] = 'viridian-forest-n'
				encounter = get_encounter('viridian-forest-n', 'tall-grass')
				battle([Pokemon(encounter['pokemon'], encounter['level'], {})])
			elif option in trainer_options:
				trainer_interaction(save['location'], option)
			elif option == 'm':
				menu_open = True

		# invalid location
		else:
			abort(f'The location "{save["location"]}" is not a valid location.')

		# end of loop
		if not dex_string:
			sp('')

	# end program
