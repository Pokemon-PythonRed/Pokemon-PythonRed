'''
Pokémon PythonRed | https://github.com/Pokemon-PythonRed
Comments may be removed at a later time.
'''

# libraries
try:
    import datetime, getpass, math, msvcrt, os, time, random, webbrowser, winsound, sqlite3
except ImportError:
    exit('Please close the program and install the required dependencies before playing. See [https://github.com/Pokemon-PythonRed/Pokemon-PythonRed#faqs] for more information.')

# create cls()
def cls():
  os.system("clear")

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
print('Please choose an option.\n\n1. Continue Game\n2. New Game\n3. GitHub Repository\n')
while startOption!='2':
	startOption=input('>')
	cls()
	if startOption=='1':
		# Start db here
		
    print("") # Nothing as of right now
    
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

load = 10
num = 0

while num < load:
  print("Loading... /")
  time.sleep(0.8)
  cls()
  print("Loading... -")
  time.sleep(0.8)
  cls()
  print("Loading... \\")
  time.sleep(0.8)
  cls()
  num += 1

print("Loaded!")
time.sleep(1)
cls()

