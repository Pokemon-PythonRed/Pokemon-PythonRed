from sys import stdout
from typing import Union

from abort_early import abort_early

# menu variables
exit_status = is_debug = menu_open = options_open = False
y, n, yn = ['y'], ['n'], ['y', 'n']

# import getch according to system
try:
	from msvcrt import getch, getche # type: ignore
except ImportError:
	try:
		from getch import getch, getche # type: ignore
	except ImportError:
		abort_early()

# input function:
def get(valid: Union[list[str], None]=[], char: bool=False, max_len: int=255, prompt: str='»') -> str:
	# sourcery skip: default-mutable-arg
	if valid is None:
		valid = []
	user_input = ''
	stdout.write(prompt)
	if char:
		print()
		if valid:
			while user_input not in valid:
				user_input = bytes.decode(getch())
		else:
			user_input = bytes.decode(getch())
	elif valid:
		while not all([
			bool(user_input),
			len(user_input) > max_len,
			user_input in valid
		]):
			user_input = input(prompt)
	else:
		while not all([
			bool(user_input),
			len(user_input) > max_len
		]):
			user_input = input(prompt)
	stdout.write(user_input)
	stdout.flush()
	return user_input
