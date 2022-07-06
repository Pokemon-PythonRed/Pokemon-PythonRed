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

def reset_sp(s):
	global sp, sg
	def sp(text, g=False):
		for char in f'{text}\n':
			time.sleep(s)
			sys.stdout.write(char)
			sys.stdout.flush()
		if g:
			getch()
	def sg(text):
		sp(text, g=True)
reset_sp(textSpeed)

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
	input('> ')
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
y, n, yn = ['y'], ['n'], ['y', 'n']

def abort(message):
	sp(f'\nERROR - {message}\n\nIf you have not edited any files, feel free to create an issue on the repository by going to the link below.\nNote: your save file will be preserved in the program folder.\n\n[{link.issue}]\n\nPress Enter to exit.')
	input('> ')
	sys.exit()

def backup():
	sp('Would you like to save your progress? Y/N\n')
	saveOption = ' '
	while saveOption.lower()[0] not in yn:
		saveOption = input('> ') + ' '
	if saveOption.lower()[0] in y:
		open(os.path.join(sys.path[0], 'save.json'), 'w').write(f'{json.dumps(save, indent=4, sort_keys=True)}\n')
		sp('\nGame saved successfully!')

class Pokemon:
	def __init__(self, species, level, ivs):
		def randomiseIVs(self):
			for i in ['hp', 'atk', 'def', 'spa', 'spd', 'spe']:
				self.ivs[i] = random.randint(0, 31)
		if ivs == 'random':
			self.randomiseIVs()
		self.species = species
		self.name = dex[self.species].name
		self.type = dex[self.species].type
		self.level = level
		self.ivs = ivs
		self.atktype = random.choice(['physical', 'special'])
		self.lvltype = dex[self.species].xp
		self.totalxp = level.total[self.lvltype][self.level]
		self.currentxp = 0
		self.fainted = False
	
		def resetStats(self):
			self.stats = {
				'hp': math.floor(((dex[self.species]['hp'] + self.ivs['hp']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['hp'])) / 4) * self.level) / 100) + self.level + 10,
				'atk': math.floor(((dex[self.species]['atk'] + self.ivs['atk']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['atk'])) / 4) * self.level) / 100) + 5,
				'def': math.floor(((dex[self.species]['def'] + self.ivs['def']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['def'])) / 4) * self.level) / 100) + 5,
				'spa': math.floor(((dex[self.species]['spa'] + self.ivs['spa']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['spa'])) / 4) * self.level) / 100) + 5,
				'spd': math.floor(((dex[self.species].spd + self.ivs['spd']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['spd'])) / 4) * self.level) / 100) + 5,
				'spe': math.floor(((dex[self.species].spe + self.ivs['spe']) * 2 + math.floor(math.ceil(math.sqrt(self.ivs['spe'])) / 4) * self.level) / 100) + 5
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
			damage = math.floor(
				((((2 * attacker.level / 5 + 2) * attacker.stats.atk * dex[attacker.species].atk) / (dex[self.species]['def'] * 50)) + 2) * random.randint(85, 100) / 100
			)
		elif attacker.atktype == 'special':
			damage = math.floor(
				((((2 * attacker.level / 5 + 2) * attacker.stats.spa * dex[attacker.species].spa) / (dex[self.species].spd * 50)) + 2) * random.randint(85, 100) / 100
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
	number = math.floor((self.stats.spe * 32) / (math.floor(opponent.stats.spe / 4) % 256)) + 30 * escapeAttempts
	if number > 255 or math.floor(opponent.stats.spe / 4) % 256 == 0:
		return True

# create battle process

def battle(opponentParty=None, battleType='wild', name=None, startDiagloue=None, title=None, endDialouge=None, levelLow=None, levelHigh=None, earnXP=True):

	# sourcery skip: low-code-quality

	if opponentParty is None and battleType == 'wild':
		opponentParty = [Pokemon('BULBASAUR', 5, 'random')]

	party1 = len(save.party)
	party2 = len(opponentParty)

	current = ''
	opponentCurrent = 0
	for i in range(party1):
		while not current:
			if not save.party[i].checkFainted():
				current = i

	# battle intro

	if battleType == 'trainer':
		sp(f'\n{name}: {startDiagloue}')
		sp(f'\n{title} {name} wants to fight!')
	elif battleType == 'wild':
		sp(f'\nA wild {opponentParty[opponentCurrent].name} appeared!')
	else:
		abort('Invalid battle type: neither trainer nor wild.')
	time.sleep(0.5)
	sp(f'\nGo, {save.party[current].name}!')
	time.sleep(0.5)
	if battleType == 'trainer':
		sp(f'\n{n} sent out {opponentParty[opponentCurrent]}!')
	
	victory = False
	escape = False
	escapeAttempts = 0

	while save.party.isAlive() and opponentParty.isAlive():

		beginCurrent = current
		playerAttackedThisTurn = False
		opponentAttackedThisTurn = False

		bars = math.ceil(save.party[current].stats.chp)*20
		opponentBars = math.ceil(opponentParty[opponentCurrent].stats["chp"])*20

		sp(f'''{save.party[current].name}{' '*15-len(save.party[current].name)}[{'='*bars}{' '*(20-bars)}]\n{save.party[current].type}\n\n{opponentParty[opponentCurrent].name}{' '*15-len(opponentParty[opponentCurrent].name)}[{'='*opponentBars}{' '*(20-opponentBars)}]\n{opponentParty[opponentCurrent].type}''')
		sp(f'\nWhat should {save.party[current]} do?\n\n[1] - Attack\n[2] - Switch\n[3] - Item\n[4] - Run')
		choice = ''
		while not choice:
			choice = input('> ')
			if choice not in ['1', '2', '3', '4']:
				choice = ''
				sp('Invalid choice.')
			elif choice == '2' and len(save.party) == 1:
				choice = ''
				sp('You can\'t switch out your only Pokemon!')

		# choose attack

		if choice == '1':
			if save.party[current].stats.spe > opponentParty[opponentCurrent].stats.spe:
				opponentParty[opponentCurrent].dealDamage(save.party[current])
				playerAttackedThisTurn = True
		
		# choose switch

		elif choice == '2':

			sp(f'''\nWhich Pokemon should you switch to?\n\n{
				''.join(f'{f"[{i+1}]" if not save.party[i].checkFainted() else "FAINTED"} - {save.party[i].name} ({save.party[i].stats.chp}/{save.party[i].stats.hp})' for i in range(party1))
			}''')
			switchChoice = ''
			while not switchChoice:
				while switchChoice == '':
					switchChoice = input('> ')
				try:
					if switchChoice not in [str(i+1) for i in range(party1)]:
						switchChoice = ''
						sp('Invalid choice.')
					elif save.party[int(switchChoice)-1].checkFainted():
						switchChoice = ''
						sp('That Pokemon is fainted!')
				except (TypeError, ValueError):
					switchChoice = ''
					sp('Invalid choice.')
			current = int(switchChoice)-1
		
		# TODO: choose item

		# choose run

		elif choice == '4':
			if save.party[current].escape(opponentParty[opponentCurrent], escapeAttempts):
				escape = True
				break

		# opponent attack

		if save.party.isAlive() and opponentParty.isAlive():
			save.party[current].dealDamage(opponentParty[opponentCurrent])
			opponentAttackedThisTurn = True
		
		if save.party.isAlive() and opponentParty.isAlive() and not playerAttackedThisTurn:
			opponentParty[opponentCurrent].dealDamage(save.party[current])
			playerAttackedThisTurn = True
		
		elif save.party.isAlive() and not opponentParty.isAlive():
			victory = True
			break

		# DEBUG: check attack statuses

		sp(f'\nDEBUG:\nHigher Speed: {"Player" if save.party[current].stats.spe > opponentParty[opponentCurrent].stats.spe else "Opponent"}\nPlayer Attacked: {playerAttackedThisTurn}\nOpponent Attacked: {opponentAttackedThisTurn}\n')

	# win/loss conditions
	
	if escape:
		sp('You escaped!')
	if save.party.isAlive() and not opponentParty.isAlive():
		if battleType == 'trainer':
			sp(f'\n{save.party[current].name} won the battle!')
		if earnXP == True:
			save.party[current].currentxp += save.party[current].calculateXP(opponentParty[opponentCurrent])
			save.party[current].checkLevelUp()
			time.sleep(0.5)
		if battleType == 'trainer':
			sp(f'\n{name}: {endDialouge}')
			# TODO: give prize money

	elif opponentParty.isAlive() and not save.party.isAlive():
		print()

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
	startOption = input('> ')
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
	input('> ')

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
		'chosenStarter': False,
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
	'party': []
}

# load save file

dex = json.loads(open(os.path.join(sys.path[0], 'dex.json')).read())
open(os.path.join(sys.path[0], 'dex.json')).close()

if startOption == '2':
	open(os.path.join(sys.path[0], 'save.json'), 'w').write(json.dumps(saveTemplate, indent=4, sort_keys=True))
save = {**saveTemplate, **json.load(open(os.path.join(sys.path[0], 'save.json')))}
json.dumps(open(os.path.join(sys.path[0], 'save.json')).read())
open(os.path.join(sys.path[0], 'save.json')).close()

types = json.loads(open(os.path.join(sys.path[0], 'types.json')).read())
open(os.path.join(sys.path[0], 'types.json')).close()

level = json.loads(open(os.path.join(sys.path[0], 'level.json')).read())
open(os.path.join(sys.path[0], 'level.json')).close()

# check for illegal save data

if (
	len(save['name']) > 15 or
	save['name'] == '' and save['flags']['introComplete'] or
	save['name'] != '' and not save['flags']['introComplete'] or
	save['flags']['chosenStarter'] and save['currentLocation'] == '' or
	save['flags']['chosenStarter'] and not save['flags']['introComplete']
):
	abort()

# reset getch according to options

reset_sp(float(save['options']['textSpeed']))

# main loop

while not exit:

	option = ''

	# intro

	if save['flags']['introComplete'] == False:

		sp('(Intro Start!)\n')
		sg('OAK: Hello there! Welcome to the world of POKéMON!')
		sg('My name is OAK! People call me the POKéMON PROFESSOR!')
		sg('This world is inhabited by creatures called POKéMON!')
		sg('For some people, POKéMON are pets. Others use them\nfor fights. Myself...')
		sg('I study POKéMON as a profession.')
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
		sg('He will go on an adventure just like yours, and battle you along\nthe way.')
		sp('\n...Erm, what is his name again?\n')
		input('> ')
		sg('\n...')
		sg('Hoho, just kidding! His name is JOHNNY! He\'s very well-known\naround here, and... quite a character. You\'ll meet him soon!\n')
		sg(f'{playerName}! Your very own POKéMON legend is about to unfold! A world of\ndreams and adventures with POKéMON awaits! Let\'s go!')

		save['name'] = playerName
		save['currentLocation'] = 'playerHouseUp'
		save['flags']['introComplete'] = True

		sp('\n(Intro Complete!)')

	elif menuOpen == True:
		sp(f'Menu\n[d] - POKéDEX\n[p] - POKéMON\n[i] - Item\n[t] - {save["name"]}\n[s] - Save Game\n[o] - Options\n[e] - Exit Menu\n[q] - Quit Game\n')

		while not option:
			option = input('> ')

		sp('')

		if option == 'd':
			sp('Coming soon!')

		elif option == 'p':
			if save.party:
				for i in range(len(save.party)):
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
			sg('\nThe notebook is open to a page that says:\n\n"Use the [m] command in the overworld to open the menu.\nFrom the menu, you can save your progress, check your POKéMON, and more!"')

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

	# TODO: add more locations

	# TODO: complete story dialogue

	else:
		abort()

	sp('')
