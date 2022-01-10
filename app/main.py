'''
Pokémon PythonRed | [https://github.com/Pokemon-PythonRed]
Comments may be removed at a later time.
	Key:
	# comment (w/ space)
	#code (w/o space)
'''

# import files

#import __init__

# dependencies

#import datetime
import getpass
import json
import math
import os
import platform
#import playsound
#import pygame
import random
#import sqlite3
import sys
import time
import webbrowser
#import winsound

# create g()

if platform.system() == "Windows":
	from msvcrt import getch as g
elif platform.system() == "Linux":
	from getch import getch as g

# create sp()

textSpeed = 0.05

def sp(words):
	for char in f'{words}\n':
		time.sleep(textSpeed)
		sys.stdout.write(char)
		sys.stdout.flush()

# look for required files

if not (
    os.path.isfile(os.path.join(sys.path[0], 'pokemon.json')) and
    os.path.isfile(os.path.join(sys.path[0], 'types.json'))
):
	sp('\nOne or more required files are not found.\n\nPlease see\nhttps://github.com/Pokemon-PythonRed/Pokemon-PythonRed#installation \nfor more information.\n\nPress Enter to exit.\n')
	input('>')
	sys.exit()

# create cls()

platforms = [['darwin', 'clear'], ['java', 'System.out.print("\\033[H\\033[2J");System.out.flush();'], [
	'linux', 'clear'], ['windows', 'cls']]
for i in range(len(platforms)):
	if platform.system().lower() == (platforms[i][0]):
		clsCommand = platforms[i][1]
		def cls(): return os.system(clsCommand)
cls()

# title screen

title = ['''\n                                  ,'\\\n    _.----.        ____         ,'  _\   ___    ___     ____\n_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.\n\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |\n \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |\n   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |\n     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |\n      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |\n       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |\n        \_.-'       |__|    `-._ |              '-.|     '-.| |   |\n                                `'                            '-._|\n''', '                          PythonRed Version\n', '                       Press any key to begin!']
title.append(f'{title[0]}\n{title[1]}\n{title[2]}\n\n')

startOption = ''

time.sleep(1)
print(title[0])

time.sleep(2.65)
print(title[1])

time.sleep(1.85)
print(title[2])

g()

cls()

print(f'{title[3]}Please choose an option.\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

while startOption != '2':
	startOption = input('>')
	cls()

	if startOption == '1':
		if os.path.isfile(os.path.join(sys.path[0], 'save.json')):
			if json.loads(open(os.path.join(sys.path[0], 'save.json')).read())['introComplete']:
				cls()
				print(
					f'{title[3]}Loading save file!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')
				break
		print(f'{title[3]}No previous save file found!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	elif startOption == '2':
		cls()
		print(
			f'{title[3]}Starting game!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	elif startOption == '3':
		try:
			webbrowser.open(
    			'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed',
       			new = 2
        	)
		except:
			print(f'{title[3]}Failed to open website, here\'s the link:\nhttps://github.com/Pokemon-PythonRed/Pokemon-PythonRed')
		else:
			print(f'{title[3]}Repository page opened successfully!')
		finally:
			print('\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	else:
		print(
			f'{title[3]}Invalid input!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

# new game

if startOption == '2':
	sp('>2\n\nThis will overwrite any previous save data. Press Enter to continue.\n')
	input('>')

# load screen

sp('')
load = 3
for i in range(load):
	sp(f'Loading... (Step {str(i+1)} of {str(load)})')

	if i == 0:
		saveTemplate = {
            'box': [],
            'currentLocation': '',
            'hms': {
                'cut': False,
                'flash': False,
                'fly': False,
                'strength': False,
                'surf': False
            },
            'introComplete': False,
            'lastPlayed': '',
            'money': '',
            'name': '',
            'party': []
        }

		dex = json.loads(open(os.path.join(sys.path[0], 'pokemon.json')).read())
		open(os.path.join(sys.path[0], 'pokemon.json')).close()

		if startOption == '2':
			open(os.path.join(sys.path[0], 'save.json'), 'w').write(
				json.dumps(saveTemplate, indent=4, sort_keys=True))
		save = {**saveTemplate, **json.loads(open(os.path.join(sys.path[0], 'save.json')).read())}
		open(os.path.join(sys.path[0], 'save.json')).close()

		types = json.loads(open(os.path.join(sys.path[0], 'types.json')).read())
		open(os.path.join(sys.path[0], 'types.json')).close()

	elif i == 1:
		exit = menuOpen = False
		option = ''
		y = ['y']
		n = ['n']
		yn = y + n

		def abort():
			cls()
			sp(
				f'\nExcuse me, {getpass.getuser()}, but you shouldn\'t be able to see this.\nPlease don\'t edit the program, or your save file. Press Enter to exit.\n')
			input('>')
			sys.exit()

		def backup():
			sp('Would you like to save your progress? Y/N\n')
			saveOption = ' '
			while saveOption.lower()[0] not in yn:
				saveOption = input('>') + ' '
			if saveOption.lower()[0] in y:
				open(os.path.join(sys.path[0], 'save.json'), 'w').write(
					json.dumps(save, indent=4, sort_keys=True)
				)
				sp('\nGame saved successfully!')

		if i == 2:
			class Pokemon:
				def __init__(self, name, species, level, moves, ivs):
					if ivs == 'random':
						ivs = {
          					'hp': random.randint(1, 15),
               				'atk': random.randint(1, 15),
                   			'def': random.randint(1, 15),
                      		'spa': random.randint(1, 15),
                        	'spd': random.randint(1, 15),
                         	'spe': random.randint(1, 15)
                        }
					self.name = name
					self.species = species
					self.type = dex[self.index]['type']
					self.level = level
					self.moves = moves
					self.ivs = ivs
					self.atktype = random.choice(['p', 's'])
					self.stats = {
						'hp': math.floor(((dex[species]['hp'] + ivs['hp']) * 2 + math.floor(math.ceil(math.sqrt(ivs['hp'])) / 4) * self.level) / 100) + self.level + 10,
						'atk': math.floor(((dex[species]['atk'] + ivs['atk']) * 2 + math.floor(math.ceil(math.sqrt(ivs['atk'])) / 4) * self.level) / 100) + 5,
						'def': math.floor(((dex[species]['def'] + ivs['def']) * 2 + math.floor(math.ceil(math.sqrt(ivs['def'])) / 4) * self.level) / 100) + 5,
						'spa': math.floor(((dex[species]['spa'] + ivs['spa']) * 2 + math.floor(math.ceil(math.sqrt(ivs['spa'])) / 4) * self.level) / 100) + 5,
						'spd': math.floor(((dex[species]['spd'] + ivs['spd']) * 2 + math.floor(math.ceil(math.sqrt(ivs['spd'])) / 4) * self.level) / 100) + 5,
						'spe': math.floor(((dex[species]['spe'] + ivs['spe']) * 2 + math.floor(math.ceil(math.sqrt(ivs['spe'])) / 4) * self.level) / 100) + 5
					}
					self.stats['chp'] = self.stats['hp']

				def battle(n, s, c, e, a, opponentParty):

					# todo: calculate opponent stats

					sp(f'\n{n}: {s}')
					g()
					sp(f'\n{c} {n} wants to fight!')
					time.sleep(0.5)
					sp(f'\nGo, {save.party[0]["name"]}!')
					time.sleep(0.5)
					sp(f'\n{n} sent out {opponentParty[0]}!')
					#party1 = len(save['party'])
					#party2 = len(opponentParty)

					#current = ''
					#opponentCurrent = 0
					#for i in range(party1):
					#	while current == '':
					#		if save['party'][i].stats['chp'] > 0:
					#			current = i

					def check(party):
						total = sum(i['hp'] for i in range(len(party)))
						return total > 0

					bars = math.ceil(save["party"][0].stats["chp"])*20
					opponentBars = math.ceil(opponentParty[0].stats["chp"])*20

					while check(save['party']) and check(opponentParty):
						sp(f'{save["party"][0].name}{" "*10-len(save["party"][0].name)}[{"="*bars}{" "*(20-bars)}]\n{save["party"][0].type}\n\n{opponentParty[0].name}{" "*10-len(opponentParty[0].name)}[{"="*opponentBars}{" "*(20-opponentBars)}]\n{opponentParty[0].type}')

					# todo: player turn, opponent turn, damage calculation

					# todo: win/loss conditions

sp('\nLoaded! Press any key to continue.\n')
g()

# check for illegal save data

if (
	(len(save['name']) > 15) or
	(save['name'] == '' and save['introComplete']) or
	(save['name'] != '' and not save['introComplete']) # etc.
):
	abort()

while not exit:

	option = ''

	# intro

	if save['introComplete'] == False:

		sp('(Intro Start!)\n')
		g()
		sp('OAK: Hello there! Welcome to the world of POKéMON!')
		g()
		sp('My name is OAK! People call me the POKéMON PROFESSOR!')
		g()
		sp('This world is inhabited by creatures called POKéMON!')
		g()
		sp('For some people, POKéMON are pets. Others use them\nfor fights. Myself...')
		g()
		sp('I study POKéMON as a profession.')
		g()
		sp('\nFirst, what is your name?\n\n[1] - PYTHON\n[2] - New Name\n')

		introAnswer = ''

		while introAnswer not in {'1', '2'}:
			introAnswer = input('>')

		if introAnswer == '1':
			playerName = 'PYTHON'

		elif introAnswer == '2':
			sp('\n(Caps, 15 chars. max)\n')
			playerName = input('>')

			while len(playerName) > 15 or playerName == '':
				playerName = input('>')

		else:
			sp('Invalid answer!')

		playerName = playerName.upper()

		sp(f'\nRight! So your name is {playerName}!')
		g()
		sp('\nNow, since you\'re so raring to go, I\'ve prepared a rival for you.')
		g()
		sp('He will go on an adventure just like yours, and battle you along\nthe way.')
		g()
		sp('\n...Erm, what is his name again?\n')
		input('>')
		sp('\n...')
		g()
		sp('Hoho, just kidding! His name is JOHNNY! He\'s very well-known\naround here, and... quite a character. You\'ll meet him soon!\n')
		g()
		sp(f'{playerName}! Your very own POKéMON legend is about to unfold! A world of\ndreams and adventures with POKéMON awaits! Let\'s go!')
		g()

		save['name'] = playerName
		save['currentLocation'] = 'playerHouseUp'
		save['introComplete'] = True

		sp('\n(Intro Complete!)')

	elif menuOpen == True:
		sp(
			f'Menu\n[d] - POKéDEX\n[p] - POKéMON\n[i] - Item\n[t] - {save["name"]}\n[s] - Save Game\n[o] - Options\n[e] - Exit Menu\n[q] - Quit Game\n')

		while option == '':
			option = input('>')

		sp('')

		if option == 'd':
			sp('Coming soon!')

		elif option == 'p':
			for i in range(len(save['party'])):
				sp(i.name)

		elif option == 'i':
			sp('Coming soon!')

		elif option == 't':
			sp('Coming soon!')

		elif option == 's':
			backup()

		elif option == 'o':
			sp('Coming soon!')

		elif option == 'e':
			menuOpen = False

		elif option == 'q':
			sp('Are you sure you want to quit? Any unsaved progress will be lost. Y/N\n')
			option = ''

			while option not in yn:
				option = input('>')
			if option in y:
				exit = True

		else:
			sp('Invalid answer!')

	elif save['currentLocation'] == 'playerHouseUp':
		sp(
			f'Current Location: {save["name"]}\'s Room (Upstairs)\n\n[s] - Go Downstairs\n[1] - Computer\n[2] - Notebook\n')

		while option == '':
			option = input('>')

		if option == '1':
			sp('\n...\n')
			g()
			sp('Looks like you can\'t use it yet.')

		elif option == '2':
			sp(
				'\nThe notebook is open to a page that says:\n\n"Use the [m] command in the overworld to open the menu.\nFrom the menu, you can save your progress, check your POKéMON, and more!"')

		elif option == 's':
			save['currentLocation'] = 'playerHouseDown'

		elif option == 'm':
			menuOpen = True

		else:
			sp('Invalid answer!')

	elif save['currentLocation'] == 'playerHouseDown':
		sp(
			f'Current Location: {save["name"]}\'s House (Downstairs)\n\n[w] - Go Upstairs\n[d] - Go Outside\n')

		while option == '':
			option = input('>')

		if option == 'd':
			save['currentLocation'] = 'palletTown'

		elif option == 'w':
			save['currentLocation'] = 'playerHouseUp'

		elif option == 'm':
			menuOpen = True

		else:
			sp('Invalid answer!')

	elif save['currentLocation'] == 'palletTown':
		sp(
			f'Current Location: Pallet Town - "Shades of your journey await!"\n(Currently the furthest point.)\n\n[w] - Go to Route 1\n[a] - Go to {save["name"]}\'s House\n[s] - Go to Sea-Route 21\n[d] - Go to OAK\'s LAB\n')

		while option == '':
			option = input('>')

		if option == 'w':
			sp('Coming soon!\n')

		elif option == 'a':
			save['currentLocation'] = 'playerHouseDown'

		elif option == 's':
			sp('The water is a deep, clear blue.\n')

		elif option == 'd':
			sp('Coming soon!\n')

		elif option == 'm':
			menuOpen = True

		else:
			sp('Invalid answer!')

	elif save['currentLocation'] == 'oakLab':
		abort()

	else:
		abort()

	sp('')
