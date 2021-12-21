'''
Pokémon PythonRed | https://github.com/Pokemon-PythonRed
Key:
# comment (w/ space)
#spare code (w/o space)
'''

# import dependencies
#import datetime
#import getpass
import msvcrt
import os
#import json
import sys
import time
import random
import webbrowser
#import sqlite3
import platform
#import playsound
#import pygame
#from flask import Flask, render_template, request, url_for, redirect

# Flask stuff
'''
app = Flask(__name__)
@app.route('/home')
@app.route('/')
def index():
  return render_template("index.html")
'''

# create g()
g=lambda:msvcrt.getch()

# create sp()
textSpeed=0.01
def sp(words):
	for char in f'{words}\n':
    		time.sleep(textSpeed)
    		sys.stdout.write(char)
    		sys.stdout.flush()

# create cls()
platforms=[['darwin','clear'],['java','System.out.print("\\033[H\\033[2J");System.out.flush();'],['linux','clear'],['windows','cls']]
for i in range(len(platforms)):
	if platform.system().lower()==(platforms[i][0]):
		clsCommand=platforms[i][1]
		cls=lambda:os.system(clsCommand)
cls()

# title screen
title=['''\n                                  ,'\\\n    _.----.        ____         ,'  _\   ___    ___     ____\n_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.\n\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |\n \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |\n   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |\n     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |\n      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |\n       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |\n        \_.-'       |__|    `-._ |              '-.|     '-.| |   |\n                                `'                            '-._|\n''','                          PythonRed Version','\n                        Press Enter to begin!']
title.append(f"{title[0]}\n{title[1]}\n{title[2]}\n\n")
startOption=''
time.sleep(1)
print(title[0])
time.sleep(2.65)
print(title[1])
time.sleep(1.85)
input(title[2])
cls()
print(f'{title[3]}Please choose an option.\n\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')
while startOption!='2':
	startOption=input('>')
	if startOption!='2':
		cls()
	if startOption=='1':
		# Start db here; nothing as of right now
		print(f'{title[3]}Saving and continuing coming soon!\n\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')
	elif startOption=='3':
		try:
			webbrowser.open('https://github.com/Pokemon-PythonRed/Pokemon-PythonRed',new=2)
		except:
			print(f'{title[3]}Failed to open website, here\'s the link: https://github.com/Pokemon-PythonRed/Pokemon-PythonRed')
		else:
			print(f'{title[3]}Repository page opened successfully!')
		finally:
		    print('\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')
	elif startOption!='2':
		print(f'{title[3]}Invalid input!\n\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')

# load screen
print('')
load=1
for i in range(load):
  sp(f'Loading... (Step {str(i+1)} of {str(load)})')
  time.sleep(random.randrange(7,15)/10)
sp('Loaded!\n')
time.sleep(1)

sp('OAK: Hello there! Welcome to the world of POKéMON!\nPeople call me the POKéMON PROF!')
g()
sp('This world is inhabited by creatures called POKéMON! For some\npeople, POKéMON are pets. Others use them for fights. Myself...\nI study POKéMON as a profession.')
g()
sp('First, what is your name?\n\n1. PYTHON\n2. New Name\n')
introAnswer=''
while not introAnswer in ['1','2']:
	introAnswer=input('>')
if introAnswer=='1':
	playerName='PYTHON'
elif introAnswer=='2':
	sp('\n(Caps, 15 chars. max)')
	playerName=input('>')
	while len(playerName)>15 or playerName=='':
		playerName=input('>')
else:
	sp('Invalid answer!')
playerName=playerName.upper()
sp(f'Right! So your name is {playerName}!')
g()

'''
name = input('USERNAME: ')

while name != '' or name != None:
	name = str(name)
	sp('Is ' + name + ' your name? y/n')
	name_yn = input('> ')

	if name_yn[0].lower() not in ['y', 'n']:
		print('That is not an option! Try again!')
		time.sleep(1)
		input('> ')
	else:
		if name_yn[0].lower() == 'y':
			sp('Hello ' + name + '! Now, let's enter the story of pokemon...')
			time.sleep(1)
			input('> ')
			break
		else:
			sp('Oh, okay! What is your name? y/n')
			time.sleep(1)
			name = input('USERNAME: ')
'''

sp('Now, since you\'re so raring to go, I\'ve prepared a rival for you.')
g()
sp('He will go on an adventure just like yours, and battle you along\nthe way.')
g()
sp('...Erm, what is his name again?')
input('>')
sp('...\nHa, did you really think I\'d forgotten our Champion\'s name?')
g()
sp('His name is JOHNNY! He decided to donate his strong POKéMON and start\nhis journey over, using only the best techniques. You\'ll meet him soon!')
g()
print('')
sp(f'{playerName}! Your very own POKéMON legend is about to unfold! A world of\ndreams and adventures with POKéMON awaits! Let\'s go!')
g()
time.sleep(1)
sp('\nINTRO COMPLETE!\nPress Enter to exit.')
input('>')