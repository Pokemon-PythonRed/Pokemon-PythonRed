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
from getpass import getuser
from json import dumps, load, loads
from math import ceil, floor, sqrt
from os import path, system, remove
from platform import system as platform
#import playsound
#import pygame
from random import choice, randint
#import string
from sys import path as syspath, stdout
from time import sleep
from webbrowser import open as webopen
#import winsound

# declare getch

if platform() == "Windows":
	from msvcrt import getch
elif platform() == "Linux":
	from getch import getch

# declare timed text output

text = {
	'slow': 0.03,
	'normal': 0.02,
	'fast': 0.01,
	'ultra': 0.005
}

textSpeed = 'normal'

def reset_sp(s):
	global sp, sg
	def sp(text, g=False):
		for char in f'{text}\n':
			sleep(s)
			stdout.write(char)
			stdout.flush()
		if g:
			getch()
	def sg(text):
		sp(text, g=True)
reset_sp(text[textSpeed])

# load screen

sp('Loading...')

# store links

link = {
	'repository': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed',
	'installation': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed#installation',
	'issue': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed/issues/new'
}

# check for required files

if not (path.isfile(path.join(syspath[0], i)) for i in [
	'dex.json',
	'level.json',
	'types.json' # TODO: add more files
]):
	sp(f'\nOne or more required files are not found.\n\nPlease see\n[{link.installation}]\nfor more information.\n\nPress Enter to exit.\n')
	input('> ')
	exit()

# declare clear

platforms = [['darwin', 'clear'], ['java', 'System.out.print("\\033[H\\033[2J");System.out.flush();'], [
	'linux', 'clear'], ['windows', 'cls']]
for i in range(len(platforms)):
	if platform().lower() == (platforms[i][0]):
		clsCommand = platforms[i][1]
		def cls(): return system(clsCommand)

exit = menuOpen = optionsOpen = False
option = ''
y, n, yn = ['y'], ['n'], ['y', 'n']

badges = ['Boulder', 'Cascade', 'Thunder', 'Rainbow', 'Soul', 'Marsh', 'Volcano', 'Earth']

def abort(message):
	sp(f'\nERROR - {message}\n\nIf you have not edited any files, feel free to create an issue on the repository by going to the link below.\nNote: your save file will be preserved in the program folder.\n\n[{link.issue}]\n\nPress Enter to exit.')
	input('> ')
	exit()

def backup():
	sp('Would you like to save your progress? Y/N\n')
	saveOption = ' '
	while saveOption.lower()[0] not in yn:
		saveOption = input('> ') + ' '
	if saveOption.lower()[0] in y:
		open(path.join(syspath[0], 'save.json'), 'w').write(f'{dumps(save, indent=4)}\n')
		sp('\nGame saved successfully!')

class Pokemon:
	def __init__(self, species, level, ivs):
		def randomiseIVs(self):
			for i in ['hp', 'atk', 'def', 'spa', 'spd', 'spe']:
				self.ivs[i] = randint(0, 31)
		if ivs == 'random':
			self.randomiseIVs()
		self.species = species
		self.name = dex[self.species].name
		self.type = dex[self.species].type
		self.level = level
		self.ivs = ivs
		self.atktype = choice(['physical', 'special'])
		self.lvltype = dex[self.species]['xp']
		self.totalxp = level.total[self.lvltype][self.level]
		self.currentxp = 0
		self.fainted = False

		def resetStats(self):
			self.stats = {
				'hp': floor(((dex[self.species]['hp'] + self.ivs['hp']) * 2 + floor(ceil(sqrt(self.ivs['hp'])) / 4) * self.level) / 100) + self.level + 10,
				'atk': floor(((dex[self.species]['atk'] + self.ivs['atk']) * 2 + floor(ceil(sqrt(self.ivs['atk'])) / 4) * self.level) / 100) + 5,
				'def': floor(((dex[self.species]['def'] + self.ivs['def']) * 2 + floor(ceil(sqrt(self.ivs['def'])) / 4) * self.level) / 100) + 5,
				'spa': floor(((dex[self.species]['spa'] + self.ivs['spa']) * 2 + floor(ceil(sqrt(self.ivs['spa'])) / 4) * self.level) / 100) + 5,
				'spd': floor(((dex[self.species].spd + self.ivs['spd']) * 2 + floor(ceil(sqrt(self.ivs['spd'])) / 4) * self.level) / 100) + 5,
				'spe': floor(((dex[self.species].spe + self.ivs['spe']) * 2 + floor(ceil(sqrt(self.ivs['spe'])) / 4) * self.level) / 100) + 5
			}
			self.stats['chp'] = self.stats['hp']

		resetStats(self)

	def canLevelUp(self, i):
		return i.currentxp >= level.next[self.lvltype][self.level] and i.level < 100

	def checkLevelUp(self, party):
		for i in party:
			while i.canLevelUp(i):
				i.currentxp -= level.next[self.lvltype][self.level]
				i.level += 1
				i.resetStats()
				sp(f'\n{i.name} grew to level {i.level}!')

	def checkFainted(self):
		if self.stats.chp <= 0:
			self.stats.chp = 0
			self.fainted = True
			return True
		return False

	def dealDamage(self, attacker):
		sp(f'\n{attacker.name} used a {attacker.type}-type attack on {self.name}!')
		if attacker.atktype == 'physical':
			damage = floor(
				((((2 * attacker.level / 5 + 2) * attacker.stats.atk * dex[attacker.species].atk) / (dex[self.species]['def'] * 50)) + 2) * randint(85, 100) / 100
			)
		elif attacker.atktype == 'special':
			damage = floor(
				((((2 * attacker.level / 5 + 2) * attacker.stats.spa * dex[attacker.species].spa) / (dex[self.species].spd * 50)) + 2) * randint(85, 100) / 100
			)
		self.stats.chp -= damage
		sp(f'\n{attacker.name} dealt {damage} damage to {self.name}!')
		self.checkFainted()
		if self.fainted:
			sp(f'\n{self.name} fainted!')

	def calculateXP(self, attacker, battleType='wild'):
		return (level.total[attacker.xptype][attacker.level] * attacker.level * (1 if battleType == 'wild' else 1.5)) / 7

# check if party is alive

def isAlive(self):
	return not (i.checkFainted() for i in self)

# randomise escape

def escape(self, opponent, escapeAttempts):
	number = floor((self.stats.spe * 32) / (floor(opponent.stats.spe / 4) % 256)) + 30 * escapeAttempts
	if number > 255 or floor(opponent.stats.spe / 4) % 256 == 0:
		return True

# create battle process

def battle(opponentParty=None, battleType='wild', name=None, startDiagloue=None, title=None, endDialouge=None, levelLow=None, levelHigh=None, earnXP=True):

	# sourcery skip: low-code-quality

	if opponentParty is None and battleType == 'wild':
		opponentParty = [Pokemon('BULBASAUR', randint(levelLow, levelHigh), 'random')]

	party1 = len(save['party'])
	party2 = len(opponentParty)

	current = ''
	opponentCurrent = 0
	for i in range(party1):
		while not current:
			if not save['party'][i].checkFainted():
				current = i

	# battle intro

	if battleType == 'trainer':
		sp(f'\n{name}: {startDiagloue}')
		sp(f'\n{title} {name} wants to fight!')
	elif battleType == 'wild':
		sp(f'\nA wild {opponentParty[opponentCurrent].name} appeared!')
	else:
		abort('Invalid battle type: neither trainer nor wild.')
	sleep(0.5)
	sp(f'\nGo, {save["party"][current].name}!')
	sleep(0.5)
	if battleType == 'trainer':
		sp(f'\n{n} sent out {opponentParty[opponentCurrent]}!')

	victory = False
	escape = False
	escapeAttempts = 0

	while save['party'].isAlive() and opponentParty.isAlive():

		beginCurrent = current
		playerAttackedThisTurn = False
		opponentAttackedThisTurn = False

		bars = ceil(save['party'][current].stats.chp)*20
		opponentBars = ceil(opponentParty[opponentCurrent].stats["chp"])*20

		sp(f'''{save["party"][current].name}{' '*15-len(save['party'][current].name)}[{'='*bars}{' '*(20-bars)}]\n{save["party"][current].type}\n\n{opponentParty[opponentCurrent].name}{' '*15-len(opponentParty[opponentCurrent].name)}[{'='*opponentBars}{' '*(20-opponentBars)}]\n{opponentParty[opponentCurrent].type}''')
		sp(f'\nWhat should {save["party"][current]} do?\n\n[1] - Attack\n[2] - Switch\n[3] - Item\n[4] - Run')
		choice = ''
		while not choice:
			choice = input('> ')
			if choice not in ['1', '2', '3', '4']:
				choice = ''
				sp('Invalid choice.')
			elif choice == '2' and len(save['party']) == 1:
				choice = ''
				sp('You can\'t switch out your only Pokémon!')

		# choose attack

		if choice == '1':
			if save['party'][current].stats.spe > opponentParty[opponentCurrent].stats.spe:
				opponentParty[opponentCurrent].dealDamage(save['party'][current])
				playerAttackedThisTurn = True

		# choose switch

		elif choice == '2':

			sp(f'''\nWhich Pokémon should you switch to?\n\n{
				''.join(f'{f"[{i+1}]" if not save["party"][i].checkFainted() else "FAINTED"} - {save["party"][i].name} ({save["party"][i].stats.chp}/{save["party"][i].stats.hp})' for i in range(party1))
			}''')
			switchChoice = ''
			while not switchChoice:
				while switchChoice == '':
					switchChoice = input('> ')
				try:
					if switchChoice not in [str(i+1) for i in range(party1)]:
						switchChoice = ''
						sp('Invalid choice.')
					elif save['party'][int(switchChoice)-1].checkFainted():
						switchChoice = ''
						sp('That Pokémon is fainted!')
				except (TypeError, ValueError):
					switchChoice = ''
					sp('Invalid choice.')
			current = int(switchChoice)-1

		# TODO: choose item

		# choose run

		elif choice == '4':
			if save['party'][current].escape(opponentParty[opponentCurrent], escapeAttempts):
				escape = True
				break

		# opponent attack

		if save['party'].isAlive() and opponentParty.isAlive():
			save['party'][current].dealDamage(opponentParty[opponentCurrent])
			opponentAttackedThisTurn = True

		if save['party'].isAlive() and opponentParty.isAlive() and not playerAttackedThisTurn:
			opponentParty[opponentCurrent].dealDamage(save['party'][current])
			playerAttackedThisTurn = True

		elif save['party'].isAlive() and not opponentParty.isAlive():
			victory = True
			break

		# DEBUG: check attack statuses

		sp(f'\nDEBUG:\nHigher Speed: {"Player" if save["party"][current].stats.spe > opponentParty[opponentCurrent].stats.spe else "Opponent"}\nPlayer Attacked: {playerAttackedThisTurn}\nOpponent Attacked: {opponentAttackedThisTurn}\n')

	# win/loss conditions

	if escape:
		sp('You escaped!')
	if save['party'].isAlive() and not opponentParty.isAlive():
		if battleType == 'trainer':
			sp(f'\n{save["party"][current].name} won the battle!')
		if earnXP == True:
			save['party'][current].currentxp += save['party'][current].calculateXP(opponentParty[opponentCurrent])
			save['party'][current].checkLevelUp()
			sleep(0.5)
		if battleType == 'trainer':
			sp(f'\n{name}: {endDialouge}')
			# TODO: give prize money

	elif opponentParty.isAlive() and not save['party'].isAlive():
		print()

cls()

# title screen

title = ['''\n                                  ,'\\\n    _.----.        ____         ,'  _\   ___    ___     ____\n_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.\n\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |\n \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |\n   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |\n     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |\n      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |\n       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |\n        \_.-'       |__|    `-._ |              '-.|     '-.| |   |\n                                `'                            '-._|\n''', '                          PythonRed Version\n', '                       Press any key to begin!']
title.append(f'{title[0]}\n{title[1]}\n{title[2]}\n\n')

startOption = ''

sleep(1)
print(title[0])

sleep(2.65)
print(title[1])

sleep(1.85)
print(title[2])

getch()

cls()

print(f'{title[3]}Please choose an option.\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

while startOption != '2':
	startOption = input('> ')
	cls()

	if startOption == '1':
		if (path.isfile(path.join(syspath[0], 'save.json')) and loads(open(path.join(syspath[0], 'save.json')).read())['flags']['introComplete']):
			cls()
			print(f'{title[3]}Loading save file!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')
			break
		print(f'{title[3]}No previous save file found!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	elif startOption == '2':
		cls()
		print(f'{title[3]}Starting game!\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository\n')

	elif startOption == '3':
		try:
			webopen(link.repository, new=2, autoraise=True)
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
	print('> 2')
	sg('\nThis will overwrite any previous save data. Please enter the words "new file" to continue.\n\nIf you change your mind, please restart the program.\n')
	while startOption.lower() != 'new file':
		startOption = input('> ')

# import data

dex = loads(open(path.join(syspath[0], 'dex.json')).read())
open(path.join(syspath[0], 'dex.json')).close()

types = loads(open(path.join(syspath[0], 'types.json')).read())
open(path.join(syspath[0], 'types.json')).close()

level = loads(open(path.join(syspath[0], 'level.json')).read())
open(path.join(syspath[0], 'level.json')).close()

# save file template

saveTemplate = {
	'badges': {
		i: False for i in badges
	},
	'bag': {},
	'box': [],
	'currentLocation': '',
	'dex': {},
	'flags': {
		'chosenStarter': False,
		'eggInDaycare': False,
		'introComplete': False,
		'pokemonCaught': 0,
		'pokemonSeen': 0,
		'pokemonUncaught': 0,
		'trainerFought': {},
		'typeCaught': [],
		'typeSeen': [],
		'typeUncaught': []
	},
	'hms': {
		'cut': False,
		'flash': False,
		'fly': False,
		'strength': False,
		'surf': False
	},
	'lastPlayed': '',
	'money': 3000,
	'mysteryGiftsOpened': {
		# TODO: add mystery gifts
	},
	'name': '',
	'options': {
		'textSpeed': textSpeed
	},
	'party': []
}

# load save file

if startOption == '2':
	open(path.join(syspath[0], 'save.json'), 'w').write(dumps(saveTemplate, indent=4))
save = {**saveTemplate, **load(open(path.join(syspath[0], 'save.json')))}
dumps(open(path.join(syspath[0], 'save.json')).read())
open(path.join(syspath[0], 'save.json')).close()

# check for illegal save data

if (
	len(save['name']) > 15 or
	save['name'] != save['name'].upper() or
	save['name'] == '' and save['flags']['introComplete'] or
	save['name'] != '' and not save['flags']['introComplete'] or
	save['flags']['chosenStarter'] and save['currentLocation'] == '' or
	save['flags']['chosenStarter'] and not save['flags']['introComplete']
):
	abort()

# reset getch according to options

reset_sp(text[save['options']['textSpeed']])

# main loop

while not exit:

	option = ''

	# intro

	if save['flags']['introComplete'] == False:

		sp('(Intro Start!)\n')
		sg('OAK: Hello there! Welcome to the world of Pokémon!')
		sg('My name is OAK! People call me the Pokémon Professor!')
		sg('This world is inhabited by creatures called Pokémon!')
		sg('For some people, Pokémon are pets. Others use them for fights. Myself...')
		sg('I study Pokémon as a profession.')
		sp('\nFirst, what is your name?\n\n[1] - PYTHON\n[2] - New Name\n')

		introAnswer = ''

		while introAnswer not in ['1', '2']:
			introAnswer = input('> ')

		if introAnswer == '1':
			playerName = 'PYTHON'

		elif introAnswer == '2':
			sp('\n(Caps, 15 chars. max)\n')
			playerName = input('> ')

			while len(playerName) > 15 or playerName == '':
				playerName = input('> ')

		else:
			sp('Invalid answer!')

		playerName = playerName.upper()

		sg(f'\nRight! So your name is {playerName}!')
		sg('\nNow, since you\'re so raring to go, I\'ve prepared a rival for you.')
		sg('He will go on an adventure just like yours, and battle you along the way.')
		sp('\n...Erm, what is his name again?\n')
		input('> ')
		sg('\n...')
		sg('Hoho, just kidding! His name is JOHNNY! You\'ll meet him soon!\n')
		sg(f'{playerName}! Your very own Pokémon legend is about to unfold! A world of dreams and adventures with Pokémon awaits! Let\'s go!')

		save['name'] = playerName
		save['currentLocation'] = 'playerHouseUp'
		save['flags']['introComplete'] = True

		sp('\n(Intro Complete!)')

	elif optionsOpen == True:
		sp('Options Menu\n[1] - Text Speed\n[2] - (Coming Soon)\n[3] - (Coming Soon)\n[4] - Back\n') # TODO: music, sound effects

		while not option:
			option = input('> ')

		if option == '1':
			option = ''
			while option != '5':
				sp('\nText Speed\n[1] - Slow\n[2] - Normal\n[3] - Fast\n[4] - Ultra\n[5] - Back\n')
				option = ''
				while not option:
					option = input('> ')
				if option != '5':
					sp('')
				if option == '1':
					save['options']['textSpeed'] = 'slow'
					reset_sp(text[save['options']['textSpeed']])
					sp('Text Speed set to Slow!')
				elif option == '2':
					save['options']['textSpeed'] = 'normal'
					reset_sp(text[save['options']['textSpeed']])
					sp('Text Speed set to Normal!')
				elif option == '3':
					save['options']['textSpeed'] = 'fast'
					reset_sp(text[save['options']['textSpeed']])
					sp('Text Speed set to Fast!')
				elif option == '4':
					save['options']['textSpeed'] = 'ultra'
					reset_sp(text[save['options']['textSpeed']])
					sp('Text Speed set to Ultra!')
				elif option != '5':
					sp('Invalid answer!')

		elif option in ['2', '3']:
			sp('Coming Soon!')

		elif option == '4':
			optionsOpen = False

		else:
			sp('Invalid answer!')

	elif menuOpen == True:
		sp(f'Menu\n[d] - Pokédex\n[p] - Pokémon\n[i] - Item\n[t] - {save["name"]}\n[s] - Save Game\n[o] - Options\n[e] - Exit Menu\n[q] - Quit Game\n')

		while not option:
			option = input('> ')

		if option not in ['e', 'o']:
			sp('')

		if option == 'd':
			option = ''
			dexString = ''.join(
				f'\n{dex[i]["index"]} - {i}: Seen{", Caught" if save["dex"][i]["caught"] else ""}' if save['dex'][i]['seen'] else '' for i in save['dex']
			)
			sp(f"{save['name']}'s Pokédex{dexString}" or '\nYou have no Pokémon in your Pokédex!')

		elif option == 'p':
			if save['party']:
				for i in range(len(save['party'])):
					sp(i.name)
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
			sp(f'Money: {"{:,}".format(save["money"])}')
			sp(f'''Badges: {''.join(f"[{'x' if save['badges'][i] else ' '}]" for i in badges)}''')

		elif option == 's':
			backup()

		elif option == 'o':
			optionsOpen = True

		elif option == 'e':
			menuOpen = False

		elif option == 'q':
			sp('Are you sure you want to quit? Any unsaved progress will be lost. Y/N\n')
			option = ''

			while option not in yn:
				option = input('> ')
			if option in y:
				exit = True

		else:
			sp('Invalid answer!')

	elif save['currentLocation'] == 'playerHouseUp':
		sp(f'Current Location: {save["name"]}\'s Room (Upstairs)\n\n[s] - Go Downstairs\n[1] - Computer\n[2] - Notebook\n')

		while option == '':
			option = input('> ')

		if option == '1':
			sg('\n...')
			sg('Looks like you can\'t use it yet.')

		elif option == '2':
			sg('\nThe notebook is open to a page that says:\n\n"Use the [m] command in the overworld to open the menu.\nFrom the menu, you can save your progress, check your Pokémon, and more!"')

		elif option == 's':
			save['currentLocation'] = 'playerHouseDown'

		elif option == 'm':
			menuOpen = True

		else:
			sp('Invalid answer!')

	elif save['currentLocation'] == 'playerHouseDown':
		sp(f'Current Location: {save["name"]}\'s House (Downstairs)\n\n[w] - Go Upstairs\n[d] - Go Outside\n')

		while option == '':
			option = input('> ')

		if option == 'd':
			save['currentLocation'] = 'palletTown'

		elif option == 'w':
			save['currentLocation'] = 'playerHouseUp'

		elif option == 'm':
			menuOpen = True

		else:
			sp('Invalid answer!')

	elif save['currentLocation'] == 'palletTown':
		sp(f'Current Location: Pallet Town - "Shades of your journey await!"\n\n[w] - Go to Route 1\n[a] - Go to {save["name"]}\'s House\n[s] - Go to Sea-Route 21\n[d] - Go to OAK\'s LAB\n')

		while option == '':
			option = input('> ')

		if option == 'w':
			if save['flags']['chosenStarter']:
				save['currentLocation'] = 'route1'
			else:
				sp('\nComing soon!')

		elif option == 'a':
			save['currentLocation'] = 'playerHouseDown'

		elif option == 's':
			sg('\nThe water is a deep, clear blue.')
			if save['hms']['surf']:
				sp('\n...Would you like to use Surf? Y/N')
				option = ''
				while option not in yn:
					option = input('> ')
				if option in y:
					save['currentLocation'] = 'seaRoute21'
				else:
					sg('\nYou decided not to use Surf.')

		elif option == 'd':
			if save['flags']['chosenStarter']:
				save['currentLocation'] = 'oakLab'
			else:
				sg('\n...')
				sg('It appears to be locked.')

		elif option == 'm':
			menuOpen = True

		else:
			sp('Invalid answer!')

	elif save['currentLocation'] == 'oakLab':
		abort('Oak\'s Lab is currently inaccessible.')

	elif save['currentLocation'] == 'seaRoute21':
		abort('Route 21 is currently inaccessible.')

	else:
		abort()

	sp('')
