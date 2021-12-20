'''
Pokémon PythonRed | https://github.com/Pokemon-PythonRed
Comments may be removed at a later time.
'''

# import dependencies
import datetime
import getpass
import msvcrt
import os
import json
import time
import random
import webbrowser
import sqlite3
import platform
import playsound
import pygame
from flask import Flask, render_template, request, url_for, redirect # For future code if used in a web platform.

app = Flask(__name__)

"""
@app.route('/home')
@app.route('/')
def index():
  return render_template("index.html")
"""

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
  print(f"Loading... (Step {str(i+1)} of {str(load)})")
  time.sleep(random.randrange(7,15)/10)
print("Loaded!")
time.sleep(1)
