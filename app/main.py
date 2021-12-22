'''
Pokémon PythonRed | https://github.com/Pokemon-PythonRed
	Key:
	# comment (w/ space)
	#code (w/o space)
'''


# dependencies

#import datetime
import getpass
import msvcrt
import os
import json
import sys
import time
#import random
import webbrowser
#import sqlite3
import platform
#import playsound
#import pygame


# create g()

def g():
	return msvcrt.getch()


# create sp()

textSpeed = 0.01
def sp(words):
	for char in f'{words}\n':
		time.sleep(textSpeed)
		sys.stdout.write(char)
		sys.stdout.flush()


# look for required files

if not os.path.isfile(os.path.join(sys.path[0], 'pokemon.json')):
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

title = ['''\n                                  ,'\\\n    _.----.        ____         ,'  _\   ___    ___     ____\n_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.\n\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |\n \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |\n   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |\n     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |\n      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |\n       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |\n        \_.-'       |__|    `-._ |              '-.|     '-.| |   |\n                                `'                            '-._|\n''', '                          PythonRed Version\n', '                        Press Enter to begin!']
title.append(f'{title[0]}\n{title[1]}\n{title[2]}\n\n')

startOption = ''

time.sleep(1)
print(title[0])

time.sleep(2.65)
print(title[1])

time.sleep(1.85)
print(title[2])

input('')

cls()

print(f'{title[3]}Please choose an option.\n\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')

while startOption != '2':
	startOption = input('>')

	if startOption not in ['1', '2']:
		cls()

	if startOption == '1':
		if os.path.isfile(os.path.join(sys.path[0], 'save.json')):
			temp = json.loads(open(os.path.join(sys.path[0], 'save.json')).read())
			if temp['data']['introComplete']:
				break
		print(f'{title[3]}No previous save file found!\n\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')

	elif startOption == '3':
		try:
			webbrowser.open(
					'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed', new=2)
		except:
			print(f'{title[3]}Failed to open website, here\'s the link:\nhttps://github.com/Pokemon-PythonRed/Pokemon-PythonRed')
		else:
			print(f'{title[3]}Repository page opened successfully!')
		finally:
			print('\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')

	else:
		print(
			f'{title[3]}Invalid input!\n\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')


# new game

if startOption == '2':
	sp('\nThis will overwrite any previous save data. Press Enter to continue.\n')
	input('>')


# load screen

sp('')
load = 3
for i in range(load):
	sp(f'Loading... (Step {str(i+1)} of {str(load)})')

	if i == 0:
		saveTemplate = {
			'trainer': {
				'name': '',
				'money': '',
				'hms': {
					'cut': False,
					'fly': False,
					'surf': False,
					'strength': False,
					'flash': False
				}
			},
			'data': {
				'introComplete': False,
				'currentLocation': ''
			},
			'pokemon': {
				'party': {
				},
				'box': {
				}
			}
		}

	elif i == 1:
		pokemon = json.loads(open(os.path.join(sys.path[0], 'pokemon.json')).read())
		open(os.path.join(sys.path[0], 'pokemon.json')).close()
		if startOption == '2':
			open(os.path.join(sys.path[0], 'save.json'), 'w').write(json.dumps(saveTemplate))
		save = json.loads(open(os.path.join(sys.path[0], 'save.json')).read())
		open(os.path.join(sys.path[0], 'save.json')).close()

	elif i == 2:
		exit = False
		option = temp = ''
		y = ['Y', 'y']
		n = ['N', 'n']
		yn = ['Y', 'N', 'y', 'n']
		def abort():
			cls()
			sp(f'\nExcuse me, {getpass.getuser()}, please don\'t hack your save file. Press Enter to exit.\n')
			input('>')
			sys.exit()
		def backup():
			sp('Would you like to save the game? Y/N\n')
			saveOption = ''
			while saveOption not in yn:
				saveOption = input('>')
			if saveOption in y:
				open(os.path.join(sys.path[0], 'save.json'), 'w').write(json.dumps(save))
				sp('\nGame saved successfully!')

sp('\nLoaded!\n')

time.sleep(1)


# check for hacking

if (
	(len(save['trainer']['name']) > 15) or
	(save['trainer']['name'] == '' and save['data']['introComplete']) or
	(save['trainer']['name'] != '' and not save['data']['introComplete'])
):
	abort()


while not exit:

	option = temp = ''


	# intro

	if save['data']['introComplete'] == False:
		sp('(Intro Start!)\n')
		time.sleep(1)
		sp('OAK: Hello there! Welcome to the world of POKéMON!\nPeople call me the POKéMON PROFESSOR!')
		g()
		sp('This world is inhabited by creatures called POKéMON!')
		g()
		sp('For some people, POKéMON are pets. Others use them\nfor fights. Myself...')
		g()
		sp('I study POKéMON as a profession.')
		g()
		sp('First, what is your name?\n\n1. PYTHON\n2. New Name\n')

		introAnswer = ''

		while not introAnswer in ['1', '2']:
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
		sp('Now, since you\'re so raring to go, I\'ve prepared a rival for you.')
		g()
		sp('He will go on an adventure just like yours, and battle you along\nthe way.')
		g()
		sp('...Erm, what is his name again?\n')
		input('>')
		sp('\n...\nHa, did you really think I\'d forgotten our Champion\'s name?')
		g()
		sp('His name is JOHNNY! He decided to donate his strong POKéMON and start\nhis journey over, using only the best techniques. You\'ll meet him soon!\n')
		g()
		sp(f'{playerName}! Your very own POKéMON legend is about to unfold! A world of\ndreams and adventures with POKéMON awaits! Let\'s go!')
		g()

		time.sleep(1)

		save['trainer']['name'] = playerName
		save['data']['currentLocation'] = 'playerHouseUp'
		save['data']['introComplete'] = True

		sp('\n(Intro Complete!)\n')


	# player house - upstairs

	elif save['data']['currentLocation'] == 'playerHouseUp':
		sp('Current Location: Player House (Upstairs)\n[s] - Save\n[d] - Go Downstairs\n[q] - Quit\n')

		while option == '':
			option = input('>')

		sp('')

		if option == 's':
			backup()

		elif option == 'd':
			sp('Coming soon!')

		elif option == 'q':
			sp('Are you sure you want to quit? Any unsaved progress will be lost. Y/N')
			option = ''

			while option not in yn:
				option = input('>')
			sp('')
			if option in y:
				exit = True

		else:
			sp('Invalid answer!')

	else:
		abort()

	sp('')
	time.sleep(1)
