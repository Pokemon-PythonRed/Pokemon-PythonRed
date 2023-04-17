from json import load
from os import path
from sys import path as syspath

from handling import abort

# import from files
try:

	# dex
	dex = load(
		open(
			path.join(
				syspath[0], 'data', 'dex.json'
			), encoding='utf8'
		)
	)
	open(
		path.join(
			syspath[0], 'data', 'dex.json'
		)
	).close()

	# items
	items = load(
		open(
			path.join(
				syspath[0], 'data', 'items.json'
			), encoding='utf8'
		)
	)

	# moves
	moves = load(
		open(
			path.join(
				syspath[0], 'data', 'moves.json'
			), encoding='utf8'
		)
	)
	open(
		path.join(
			syspath[0], 'data', 'moves.json'
		)
	).close()

	# rates
	rates = load(
		open(
			path.join(
				syspath[0], 'data', 'map.json'
			), encoding='utf8'
		)
	)
	open(
		path.join(
			syspath[0], 'data', 'map.json'
		)
	).close()

	# save_template
	save_template = load(
		open(
			path.join(
				syspath[0], 'data', 'save_template.json'
			), encoding='utf8'
		)
	)
	open(
		path.join(
			syspath[0], 'data', 'save_template.json'
		)
	).close()

	# trainer_types
	trainer_types = load(
		open(
			path.join(
				syspath[0], 'data', 'trainer_types.json'
			), encoding='utf8'
		)
	)
	open(
		path.join(
			syspath[0], 'data', 'trainer_types.json'
		)
	).close()

	# types
	types = load(
		open(
			path.join(
				syspath[0], 'data', 'types.json'
			), encoding='utf8'
		)
	)
	open(
		path.join(
			syspath[0], 'data', 'types.json'
		)
	).close()

	# xp
	xp = load(
		open(
			path.join(
				syspath[0], 'data', 'level.json'
			), encoding='utf8'
		)
	)
	open(
		path.join(
			syspath[0], 'data', 'level.json'
		)
	).close()

	# pokemart
	pokemart = load(
		open(
			path.join(
				syspath[0], 'data', 'pokemart.json'
			), encoding='utf8'
		)
	)
	open(
		path.join(
			syspath[0], 'data', 'pokemart.json'
		)
	).close()

	# trainers
	trainers = load(
		open(
			path.join(
				syspath[0], 'data', 'trainers.json'
			), encoding='utf8'
		)
	)
	open(
		path.join(
			syspath[0], 'data', 'trainers.json'
		)
	).close()

# handle file error
except Exception:
	abort('Failed to load a file!')
