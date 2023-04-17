from abort_early import abort_early

# menu variables
exit = is_debug = menu_open = options_open = False
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
def get() -> str:
	return input('> ')
