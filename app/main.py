# import system modules
from contextlib import suppress
from copy import deepcopy
from datetime import datetime
from getpass import getuser
from importlib import import_module
from json import dumps, loads
from math import ceil, floor, sqrt
from os import path, system, remove
from platform import system as platform
from random import choice, choices, randint
from string import Formatter
from sys import exit as sysexit, path as syspath, stdout
from time import sleep, time
from typing import Optional, Union
from webbrowser import open as webopen

# import folderspace files
try:
	from abort_early import abort_early
	from data_opener import dex, items, locations, moves, rates, save_template, trainer_types, types, xp, pokemart, trainers
	from event_opener import Event
	from handling import abort, debug
	from input import exit_status, get, getch, getche, menu_open, options_open, y, yn
	from location_opener import Location
	from output import cls, link, reset_sp, sp, text, text_speed
	from pokemon import badges, battle, display_pokemart, display_trainers, find_moves, get_encounter, heal, Pokemon, trainer_interaction
	from saving import SaveFile
except ImportError as e:
	input(f'\n{e}.\n\nPlease see [https://github.com/Pokemon-PythonRed/Pokemon-PythonRed#installation] for more information.\n\nPress Enter to exit.\n')
	sysexit()

# import installed modules
from jsons import dump, load
from pygame.mixer import music

# set default text speed
reset_sp(speed=text[text_speed])

# load screen
sp([('Loading...', False)])

# clear screen
try:
	cls()
except NameError:
	abort_early()

# enables ANSI escape codes in Windows
system('')

# TODO: test title screen event
save = Event('title').execute(SaveFile(save_exists=False))

# reset getch according to options
reset_sp(text[save['options']['text_speed']])

# intro
if save['flag']['intro_complete'] == False:
	save = Event('intro').execute(save)

# main loop
while not exit_status:
	save['location'] = Location(save['location']).execute()

	# end program
