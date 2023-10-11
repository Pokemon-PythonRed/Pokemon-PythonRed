from input import get
from output import sp
from saving import SaveFile

def intro(save: SaveFile) -> SaveFile:
	sp([
		('(Intro Start!)\n', False),
		('OAK: Hello there! Welcome to the world of Pokémon!', True),
		('My name is OAK! People call me the Pokémon Professor!', True),
		('This world is inhabited by creatures called Pokémon!', True),
		('For some people, Pokémon are pets. Others use them for fights. Myself...', True),
		('I study Pokémon as a profession.', True),
		('\nFirst, what is your name?\n\n[1] - PYTHON\n[2] - New Name\n', False)
	])
	intro_answer = get(['1', '2'])
	if intro_answer == '1':
		player_name = 'PYTHON'
	else:
		sp([('\n(Caps, 15 chars. max)\n', False)])
		player_name = get([], char=False, max_len=15)
	player_name = player_name.upper()
	sp([
		(f'\nRight! So your name is {player_name}!', True),
		('\nNow, since you\'re so raring to go, I\'ve prepared a rival for you.', True),
		('He will go on an adventure just like yours, and battle you along the way.', True),
		('\n...Erm, what is his name again?\n', False)
	])
	get([], char=False)
	sp([
		('\n...', True),
		('Hoho, just kidding! His name is JOHNNY! You\'ll meet him soon!\n', True),
		(f'{player_name}! Your very own Pokémon legend is about to unfold! A world of dreams and adventures with Pokémon awaits! Let\'s go!', True)
	])
	save['name'] = player_name
	save['location'] = 'playerhouse-up'
	save['flag']['intro_complete'] = True
	sp([('\n(Intro Complete!)', False)])
	return save
