'''
Pokémon PythonRed | https://github.com/Pokemon-PythonRed
Comments may be removed at a later time.
'''

#import dependencies
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
from flask import Flask, render_template, request, url_for, redirect # For future code if used in a web platform.

#create cls()
platforms=[['darwin','clear'],['java','System.out.print("\\033[H\\033[2J");System.out.flush();'],['linux','clear'],['windows','cls']]
for i in range(len(platforms)):
	if platform.system().lower()==(platforms[i][0]):
		clsCommand=platforms[i][1]
		cls=lambda:os.system(clsCommand)

#title screen
startOption=''
time.sleep(1)
print('''
                                  ,'\\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
''')
time.sleep(2.65)
print('                          PythonRed Version')
time.sleep(1.85)
input('\n                        Press Enter to begin!')
cls()
print('\nPlease choose an option.\n\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')
while startOption!='2':
	startOption=input('>')
	cls()
	if startOption=='1':
		# Start db here
		# Nothing as of right now
		print('\nSaving and continuing coming soon!\n\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')

	elif startOption=='3':
		try:
			webbrowser.open('https://github.com/Pokemon-PythonRed/Pokemon-PythonRed',new=2)
		except:
			print('\nFailed to open website, here\'s the link: https://github.com/Pokemon-PythonRed/Pokemon-PythonRed')
		else:
			print('\nRepository page opened successfully!')
		finally:
		    print('\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')
	else:
		print('\nInvalid input!\n\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')
cls()

#load screen
load = 3
num = 1
while num <= load:
  print(f"Loading... (Step {num} of {load})")
  time.sleep(0.8)
  cls()
  num += 1
print("\nLoaded!")
time.sleep(1)
cls()
