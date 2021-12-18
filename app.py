'''
Pokémon PythonRed | https://github.com/Pokemon-PythonRed
Comments may be removed at a later time.
'''

# libraries
try:
	import datetime,getpass,math,msvcrt,os,platform,secrets,time,random,webbrowser,winsound
except ImportError:
    print('')
    while True:
        input('Please close the program and install the required dependencies before playing. See [https://github.com/Pokemon-PythonRed/Pokemon-PythonRed#faqs] for more information.')

# create cls()
platforms=[['darwin','clear'],['java','System.out.print("\\033[H\\033[2J");System.out.flush();'],['linux','clear'],['windows','cls']]
for i in range(len(platforms)):
	if platform.system().lower()==(platforms[i][0]):
		clsCommand=platforms[i][1]
		cls=lambda:os.system(clsCommand)

# title screen
# play title theme
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
print('\nPlease choose an option.\n\n1. Continue\n2. New Game\n3. GitHub Repository\n')
while startOption!='2':
	startOption=input('>')
	cls()
	if startOption=='1':
		print('\nSaving and continuing coming soon!\n\n1. Continue\n2. New Game\n3. GitHub Repository\n')
	elif startOption=='3':
		try:
			webbrowser.open('https://github.com/Pokemon-PythonRed/Pokemon-PythonRed',new=2)
		except:
			print('\nFailed to open website, here\'s the link: <https://github.com/Pokemon-PythonRed/Pokemon-PythonRed>.')
		else:
			print('\nRepository page opened successfully!')
		finally:
		    print('\n1. Continue\n2. New Game\n3. GitHub Repository\n')
	else:
		print('\nInvalid input!\n\n1. Continue\n2. New Game\n3. GitHub Repository\n')

# start game
cls()
input('\nWell, this is embarassing; there\'s nothing to play just yet!\n\nI haven\'t started the rewrite past the title menu.\n\nYou can press Enter to exit.')
end='''
print('If you chose "New Game" by accident, please quit now.')
print('Otherwise, press Enter to start a new game, and thanks')
input('for playing!')
cls()
print('')
print('Please wait..')
# play loading music
# create trainer profile
trainer={
	'name': '',
	'money': '0',
	'introComplete': False,
	'bag': {
		'': 0 # etc.
	},
	'introAnswer': '',
	'starterConfirm': False,
	'starter': '',
	'currentLocation': '',
	'currentMusic': 'none',
	'option': '',
	'hmsUnlocked': {
		'Surf': False # etc.
	}
}
time.sleep(1)
cls()
print('')
input('That\'s all for now! Press Enter to exit.')
'''
