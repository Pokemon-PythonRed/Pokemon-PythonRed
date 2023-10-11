from abort_early import abort_early
from platform import platform as platform_name
from os import system
from sys import stdout
from time import sleep
from typing import Union

from input import getch, getche

# declare clear command
def cls(command: str='cls\nclear') -> int:
	return system(command)

# store links
link = {
	'repository': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed',
	'installation': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed#installation',
	'issue': 'https://github.com/Pokemon-PythonRed/Pokemon-PythonRed/issues/new/choose'
}

# type colours
colours = {
	'NORMAL': '\x1b[0;0m',
	'FIRE': '\x1b[38;5;196m',
	'WATER': '\x1b[38;5;027m',
	'GRASS': '\x1b[38;5;082m',
	'ELECTRIC': '\x1b[38;5;184m',
	'ICE': '\x1b[38;5;159m',
	'FIGHTING': '\x1b[38;5;167m',
	'POISON': '\x1b[38;5;135m',
	'GROUND': '\x1b[38;5;215m',
	'FLYING': '\x1b[38;5;183m',
	'PSYCHIC': '\x1b[38;5;198m',
	'BUG': '\x1b[38;5;028m',
	'ROCK': '\x1b[38;5;179m',
	'GHOST': '\x1b[38;5;126m',
	'DRAGON': '\x1b[38;5;057m',
	'DARK': '\x1b[38;5;095m',
	'STEEL': '\x1b[38;5;250m',
	'FAIRY': '\x1b[38;5;212m',
	'RESET': '\x1b[00;0;000m'
}

# declare timed text output
text = {
	'slow': 0.03,
	'normal': 0.02,
	'fast': 0.01,
	'ultra': 0.005,
	'hyper': 0.001
}

# set default text speed
text_speed = 'normal'

# timed text output
def reset_sp(speed: float=text[text_speed]) -> None:
	global sp
	def sp(text: str, wait_keypress: bool=False) -> None:
		for char in text:
			text_iter = list(text_iter)
			for key in colours.keys():
				text_iter[0] = text_iter[0].replace(f'`{key}`', f'`{colours[key]}{key}{colours["RESET"]}`')
			coloured = False
			colour_char = False
			i = 0
			for char in f'{text_iter[0]}\n':
				if char == '`':
					if not coloured:
						colour_char = True
					coloured = not coloured
					continue
				elif coloured and char == '[':
					colour_char = True
				elif not colour_char:
					sleep(speed)
				elif i >= 10:
					i = 0
					colour_char = False
					sleep(speed)
				else:
					i += 1
				stdout.write(char)
				stdout.flush()
			if text_iter[1]:
				getch()

reset_sp()
