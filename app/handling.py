from input import is_debug
from output import colours, link, sp

# error message
def abort(message) -> None:
	print(f'\n{colours["FIRE"]}- - - INTERNAL ERROR - - -{colours["RESET"]}\n\nERROR MESSAGE: {message}\n\nIf you have not edited any files, feel free to create an issue on the repository by going to the link below.\n\nNote: your save file will be preserved in the program folder. Any unsaved progress will be lost (sorry).\n\n[{link["issue"]}]\n\nPress Enter to exit.')
	input('\n> ')
	global exit
	exit = True

# debug statements
def debug(text) -> None:
	if is_debug:
		sp(f'{colours["GROUND"]}Debug: {text}{colours["RESET"]}')
