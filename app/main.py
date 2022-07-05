'''
Pokémon PythonRed

	Project Page - [https://Pokemon-PythonRed.github.io]
	Repository   - [https://github.com/Pokemon-PythonRed/Pokemon-PythonRed]
	License      - MIT

Comments Key:

	# comment (with space)
	#unused code (without space)
'''

# dependencies

#import datetime
#from getpass import getuser
import json
import math
import os
import platform
#import playsound
#import pygame
import random
#import string
import sys
import time
import webbrowser
#import winsound

# declare getch

if platform.system() == "Windows":
	from msvcrt import getch as getch
elif platform.system() == "Linux":
	from getch import getch as getch

# declare timed text output

textSpeed = 0.03

def sp(text):
	for char in f'{text}\n':
		time.sleep(textSpeed)
		sys.stdout.write(char)
		sys.stdout.flush()
	getch()

# load screen

sp('Loading...')

# store links

link = {
	'repository': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed',
	'installation': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed#installation',
	'issue': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed/issues/new'
}

# check for required files

if not (os.path.isfile(os.path.join(sys.path[0], i)) for i in [
	'dex.json',
	'level.json',
	'types.json' # TODO: add more files
]):
	sp(f'\nOne or more required files are not found.\n\nPlease see\n[{link.installation}]\nfor more information.\n\nPress Enter to exit.\n')
	input('>')
	sys.exit()

# declare clear

platforms = [['darwin', 'clear'], ['java', 'System.out.print("\\033[H\\033[2J");System.out.flush();'], [
	'linux', 'clear'], ['windows', 'cls']]
for i in range(len(platforms)):
	if platform.system().lower() == (platforms[i][0]):
		clsCommand = platforms[i][1]
		def cls(): return os.system(clsCommand)

exit = menuOpen = False
option = ''
y = ['y']
n = ['n']
yn = y + n

def abort():
	sp(f'\nERROR\n\nAn internal error has occured. There are two possible causes for this:\n\n- The save file is corrupted.\n- There is a bug within the program which threw a needless error.\n\nThese issues may be caused by editing the save file or the program file.\n\nIf you have not edited any files, feel free to create an issue on the repository by going to the link below.\n\nNote: your save file will be preserved in the program folder.\n\n[{link.issue}]\n\nPress Enter to exit.')
	input('>')
	sys.exit()

def backup():
	sp('Would you like to save your progress? Y/N\n')
	saveOption = ' '
	while saveOption.lower()[0] not in yn:
		saveOption = input('>') + ' '
	if saveOption.lower()[0] in y:
		open(os.path.join(sys.path[0], 'save.json'), 'w').write(f'{json.dumps(save, indent=4, sort_keys=True)}\n')
		sp('\nGame saved successfully!')

class Pokemon:
	def __init__(self, name, species, level, ivs):
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
		self.ivs = ivs
		self.atktype = random.choice(['p', 's'])
		self.lvltype = dex[self.species]['xp']
		self.totalxp = level['total'][self.lvltype][self.level]
		self.currentxp = 0
	
		def resetStats(self):
			self.stats = {
				'hp': math.floor(((dex[self.species]['hp'] + self.ivs['hp']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['hp'])) / 4) * self.level) / 100) + self.level + 10,
				'atk': math.floor(((dex[self.species]['atk'] + self.ivs['atk']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['atk'])) / 4) * self.level) / 100) + 5,
				'def': math.floor(((dex[self.species]['def'] + self.ivs['def']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['def'])) / 4) * self.level) / 100) + 5,
				'spa': math.floor(((dex[self.species]['spa'] + self.ivs['spa']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['spa'])) / 4) * self.level) / 100) + 5,
				'spd': math.floor(((dex[self.species]['spd'] + self.ivs['spd']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['spd'])) / 4) * self.level) / 100) + 5,
				'spe': math.floor(((dex[self.species]['spe'] + self.ivs['spe']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['spe'])) / 4) * self.level) / 100) + 5
			}
			self.stats['chp'] = self.stats['hp']
		resetStats(self)
	
	def checkLevelUp(self):
		for i in save['party']:
			while i.currentxp >= level['next'][self.lvltype][self.level] and i.level < 100:
				i.currentxp -= level['next'][self.lvltype][self.level]
				i.level += 1
				i.resetStats()
				sp(f'\n{i.name} grew to level {i.level}!') 

	def checkFainted(self):
		if self.stats['chp'] <= 0:
			self.stats['chp'] = 0
			return True
		return False

	def battle(n, s, c, e, a, opponentParty):

		# TODO: calculate opponent stats

		sp(f'\n{n}: {s}')
		sp(f'\n{c} {n} wants to fight!')
		time.sleep(0.5)
		sp(f'\nGo, {save.party[0]["name"]}!')
		time.sleep(0.5)
		sp(f'\n{n} sent out {opponentParty[0]}!')
		party1 = len(save['party'])
		party2 = len(opponentParty)

		current = ''
		opponentCurrent = 0
		for i in range(party1):
			while current == '':
				if save['party'][i].stats['chp'] > 0:
					current = i

		def check(party):
			total = sum(i['hp'] for i in range(len(party)))
			return total > 0

		bars = math.ceil(save["party"][0].stats["chp"])*20
		opponentBars = math.ceil(opponentParty[0].stats["chp"])*20

		while check(save['party']) and check(opponentParty):
			sp(f'{save["party"][0].name}{" "*10-len(save["party"][0].name)}[{"="*bars}{" "*(20-bars)}]\n{save["party"][0].type}\n\n{opponentParty[0].name}{" "*10-len(opponentParty[0].name)}[{"="*opponentBars}{" "*(20-opponentBars)}]\n{opponentParty[0].type}')

		# TODO: player turn, opponent turn, damage calculation

		# TODO: win/loss conditions

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

getch()

cls()

print(f'{title[3]}Please choose an option.\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

while startOption != '2':
	startOption = input('>')
	cls()

	if startOption == '1':
		if (os.path.isfile(os.path.join(sys.path[0], 'save.json')) and json.loads(open(os.path.join(sys.path[0], 'save.json')).read())['flags']['introComplete']):
			cls()
			print(f'{title[3]}Loading save file!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')
			break
		print(f'{title[3]}No previous save file found!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	elif startOption == '2':
		cls()
		print(f'{title[3]}Starting game!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	elif startOption == '3':
		try:
			webbrowser.open(link.repository, new = 2)
		except Exception:
			print(f'{title[3]}Failed to open website, here\'s the link:\n[{link.repository}]\n')
		else:
			print(f'{title[3]}Repository page opened successfully!')
		finally:
			print('\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	else:
		print(f'{title[3]}Invalid input!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

# new game

if startOption == '2':
	sp('>2\n\nThis will overwrite any previous save data. Press Enter to continue.\n')
	input('>')

# save file template

saveTemplate = {
	'badges': {
		'boulder': False,
		'cascade': False,
		'thunder': False,
		'rainbow': False,
		'soul': False,
		'marsh': False,
		'volcano': False,
		'earth': False
	},
	'box': [],
	'currentLocation': '',
	'flags': {
		'introComplete': False,
		'receivedStarter': False,
		'pokemonCaught': 0,
		'pokemonSeen': 0,
		'pokemonUncaught': 0,
		'typeSeen': [],
		'typeUncaught': [],
		'typeCaught': [],
		'trainerFought': {},
		'eggInDaycare': False
	},
	'hms': {
		'cut': False,
		'flash': False,
		'fly': False,
		'strength': False,
		'surf': False
	},
	'lastPlayed': '',
	'money': 0,
	'mysteryGiftsOpened': {
		# TODO: add mystery gifts
	},
	'name': '',
	'options': {
		'textSpeed': textSpeed
	},
	'party': [],
	'xpMultiplier': 1.0
}

# load save file

dex = json.loads(open(os.path.join(sys.path[0], 'dex.json')).read())
open(os.path.join(sys.path[0], 'dex.json')).close()

if startOption == '2':
	open(os.path.join(sys.path[0], 'save.json'), 'w').write(json.dumps(saveTemplate, indent=4, sort_keys=True))
save = {**saveTemplate, **json.loads(open(os.path.join(sys.path[0], 'save.json')).read())}
open(os.path.join(sys.path[0], 'save.json')).close()

types = json.loads(open(os.path.join(sys.path[0], 'types.json')).read())
open(os.path.join(sys.path[0], 'types.json')).close()

level = json.loads(open(os.path.join(sys.path[0], 'level.json')).read())
open(os.path.join(sys.path[0], 'level.json')).close()

# check for illegal save data

if (
	(len(save['name']) > 15) or
	(save['name'] == '' and save['flags']['introComplete']) or
	(save['name'] != '' and not save['flags']['introComplete']) # TODO: more checks
):
	abort()

# main loop

while not exit:

	option = ''

	# intro

	if save['flags']['introComplete'] == False:

		sp('(Intro Start!)\n')
		sp('OAK: Hello there! Welcome to the world of POKéMON!')
		sp('My name is OAK! People call me the POKéMON PROFESSOR!')
		sp('This world is inhabited by creatures called POKéMON!')
		sp('For some people, POKéMON are pets. Others use them\nfor fights. Myself...')
		sp('I study POKéMON as a profession.')
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
		sp('\nNow, since you\'re so raring to go, I\'ve prepared a rival for you.')
		sp('He will go on an adventure just like yours, and battle you along\nthe way.')
		sp('\n...Erm, what is his name again?\n')
		input('>')
		sp('\n...')
		sp('Hoho, just kidding! His name is JOHNNY! He\'s very well-known\naround here, and... quite a character. You\'ll meet him soon!\n')
		sp(f'{playerName}! Your very own POKéMON legend is about to unfold! A world of\ndreams and adventures with POKéMON awaits! Let\'s go!')

		save['name'] = playerName
		save['currentLocation'] = 'playerHouseUp'
		save['flags']['introComplete'] = True

		sp('\n(Intro Complete!)')

	elif menuOpen == True:
		sp(f'Menu\n[d] - POKéDEX\n[p] - POKéMON\n[i] - Item\n[t] - {save["name"]}\n[s] - Save Game\n[o] - Options\n[e] - Exit Menu\n[q] - Quit Game\n')

		while not option:
			option = input('>')

		sp('')

		if option == 'd':
			sp('Coming soon!')

		elif option == 'p':
			if save['party']:
				for i in range(len(save['party'])):
					sp(i.name)
			else:
				sp('Your party is empty!')

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
		sp(f'Current Location: {save["name"]}\'s Room (Upstairs)\n\n[s] - Go Downstairs\n[1] - Computer\n[2] - Notebook\n')

		while option == '':
			option = input('>')

		if option == '1':
			sp('\n...')
			sp('Looks like you can\'t use it yet.')

		elif option == '2':
			sp('\nThe notebook is open to a page that says:\n\n"Use the [m] command in the overworld to open the menu.\nFrom the menu, you can save your progress, check your POKéMON, and more!"')

		elif option == 's':
			save['currentLocation'] = 'playerHouseDown'

		elif option == 'm':
			menuOpen = True

		else:
			sp('Invalid answer!')

	elif save['currentLocation'] == 'playerHouseDown':
		sp(f'Current Location: {save["name"]}\'s House (Downstairs)\n\n[w] - Go Upstairs\n[d] - Go Outside\n')

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
		sp(f'Current Location: Pallet Town - "Shades of your journey await!"\n(Currently the furthest point.)\n\n[w] - Go to Route 1\n[a] - Go to {save["name"]}\'s House\n[s] - Go to Sea-Route 21\n[d] - Go to OAK\'s LAB\n')

		while option == '':
			option = input('>')

		if option == 'w':
			sp('\nComing soon!')

		elif option == 'a':
			save['currentLocation'] = 'playerHouseDown'

		elif option == 's':
			sp('\nThe water is a deep, clear blue.')

		elif option == 'd':
			sp('\nComing soon!')

		elif option == 'm':
			menuOpen = True

		else:
			sp('Invalid answer!')

	elif save['currentLocation'] == 'oakLab':
		abort()

	# TODO: add more locations

	# TODO: complete story dialogue

	else:
		abort()

	sp('')
