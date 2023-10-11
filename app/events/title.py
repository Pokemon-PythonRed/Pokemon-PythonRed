from json import load
from os import path
from sys import path as syspath
from time import sleep
from webbrowser import open as webopen

from input import get, getch
from output import cls
from saving import SaveFile

def execute(save: SaveFile) -> SaveFile:

	# display title screen
	cls()
	sleep(1)
	print(r'''
                                 ,'\
    _.----.       ____         ,'  _\   ___    ___     ____
_,-'       `.    |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\     __     \   '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.   \ \    |  __ |  |/    ,','_  `.  |          | __  |    \|  |
  \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
   \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
    \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
     \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
      \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
       \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                               `'                            '-._|
''')
	sleep(2.65)
	print('                          PythonRed Version')
	sleep(1.85)
	print('                       Press any key to begin!')
	getch()
	print('\n\n[1] - Continue Game\n[2] - New Game\n[3] - GitHub Repository')
	start_option = ''
	while start_option != '2':
		start_option = get(['1', '2', '3'], char=True, max_len=1)

		# continue from save file
		if start_option == '1':
			try:
				has_saved = load(
					open(path.join(syspath[0], '.ppr-save')))['flag']['has_saved']
				if path.isfile(path.join(syspath[0], '.ppr-save')) and has_saved:
					break
			except KeyError:
				print('Your save file is outdated and the game cannot load it. Please back up your save file and contact us with option [3].')
			except ValueError:
				print('Your save file is empty and cannot be loaded!')
			else:
				print('No previous save file found!')

		# new game
		elif start_option == '2':
			break

		# open github link
		elif start_option == '3':
			try:
				webopen('https://github.com/Pokemon-PythonRed/Pokemon-PythonRed', new=2, autoraise=True)
			except Exception:
				print('Failed to open website, here\'s the link:\n[https://github.com/Pokemon-PythonRed/Pokemon-PythonRed]\n')
			else:
				print('Repository page opened successfully!')

	return save
