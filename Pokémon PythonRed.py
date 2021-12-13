'''
Pokémon PythonRed | https://github.com/Pokemon-PythonRed
Comments may be removed at a later time.
'''

# libraries
try:
	import datetime,getpass,math,msvcrt,os,platform,secrets,time,random,webbrowser,winsound # should import smoothly
except ImportError:
    print('')
    while True:
        input('Please install the required dependencies before playing.')

# create cls()
platforms=[['darwin','clear'],['java','System.out.print("\\033[H\\033[2J");System.out.flush();'],['linux','clear'],['windows','cls']]
for i in range(len(platforms)):
	if platform.system().lower()==(platforms[i][0]):
		clsCommand=platforms[i][1]
		cls=lambda:os.system(clsCommand)

# title screen
# play title theme
startOption='0'
githubOption='0'
time.sleep(1)
print('')
print('''                                  ,'\ ''')
print('''    _.----.        ____         ,'  _\   ___    ___     ____''')
print('''_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.''')
print('''\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |''')
print(''' \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |''')
print('''   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |''')
print('''    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |''')
print('''     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |''')
print('''      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |''')
print('''       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |''')
print('''        \_.-'       |__|    `-._ |              '-.|     '-.| |   |''')
print('''                                `'                            '-._|''')
print('')
time.sleep(2.65)
print('                          PythonRed Version')
time.sleep(1.85)
print('')
input('                        Press Enter to begin!')
cls()
print('')
print('Please choose an option.')
print('')
print('1. Continue')
print('2. New Game')
print('')
while startOption!='2':
    startOption=input('>')
	cls()
    if startOption!='1':
		print('Saving and continuing coming soon!')
	    print('')
		print('1. Continue')
		print('2. New Game')
		print('')

# start game
cls()
print('')
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
