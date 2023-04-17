from math import ceil, floor, sqrt
from random import choice, choices, randint
from time import sleep
from typing import Optional, Union

from data_opener import dex, items, moves, pokemart, rates, trainer_types, trainers, types, xp
from handling import abort, debug
from input import get, getch
from output import colours, sg, sp
from saving import backup

'''
File contains sections:
- POKEMON
- BATTLES
'''

# POKEMON

# constant data
types = ['NORMAL', 'FIRE', 'WATER', 'GRASS', 'ELECTRIC', 'ICE', 'FIGHTING', 'POISON', 'GROUND', 'FLYING', 'PSYCHIC', 'BUG', 'ROCK', 'GHOST', 'DARK', 'DRAGON', 'STEEL', 'FAIRY']
badges = ['Boulder', 'Cascade', 'Thunder', 'Rainbow', 'Soul', 'Marsh', 'Volcano', 'Earth']

# get trainers by location
def display_trainers(save: dict, loc) -> list:
	if loc not in trainers: return [] 

	possible_trainers = [
		trainer
		for trainer in trainers[loc]
		if not (
			trainer in save['flag']['characters_spoken']
			and trainer['leave_after_speaking']
		)
	]
	if not possible_trainers: return []

	valid_options = [i+1 for i in range(len(possible_trainers))]
	for i in valid_options:
		trainer = possible_trainers[i-1]
		if trainer['type'] == 'trainer':
			sp(f'[{i}] - Speak to {trainer["trainer_class"]}') # TODO: change to name
		elif trainer['type'] == 'character' and not (trainer in save['flag']['characters_spoken'] and trainer['leave_after_speaking']):
			sp(f'[{i}] - Speak to {trainer["name"]}')
	sp("")
	return [str(i) for i in valid_options]

# interact with trainer
def trainer_interaction(save: dict, loc, option) -> None: # sourcery skip: low-code-quality
	possible_trainers = []
	for trainer in trainers[loc]:
		if not (trainer in save['flag']['characters_spoken'] and trainer['leave_after_speaking']):
			possible_trainers.append(trainer)
	
	trainer = possible_trainers[int(option)-1]
	
	if trainer['type'] == "trainer":
		if trainer in save['flag']['trainer_fought']:
			sg(f'\n{trainer["trainer_class"]}: {trainer["after_battling_dialouge"]}') # TODO: change to trainer["name"] instead of trainer["trainer_class"]
			return

		battle(
			save,
			opponent_party=[Pokemon(save, pokemon['species'], pokemon['level'], ivs={ 'atk': 9, 'hp': 8, 'def': 8, 'spa': 8, 'spd': 8, 'spe': 8 }) for pokemon in trainer['pokemon']],
			battle_type="trainer", title=trainer['trainer_class'], start_diagloue=trainer['before_dialouge'], end_dialouge=trainer['win_dialouge']
		) # TODO: add names to battle

		save['flag']['trainer_fought'].append(trainer)
	
	elif trainer['type'] == 'character':

		if trainer in save['flag']['characters_spoken']:
			sp("")
			for line in trainer['after_text']:
				if line.startswith('`') and line.endswith('`'):
					item = line[1:-1].split(':')[0]
					amount = int(line[1:-1].split(':')[1])
					if item in save['bag']:
						save['bag'][item] += amount
					else:
						save['bag'][item] = amount
					sg(f'{save["name"]} recieved {amount} {item}(s)')
				else:
					sg(line)

		else:
			sp("")
			for line in trainer['text']:
				if line.startswith('`') and line.endswith('`'):
					item = line[1:-1].split(':')[0]
					amount = int(line[1:-1].split(':')[1])
					if item in save['bag']:
						save['bag'][item] += amount
					else:
						save['bag'][item] = amount
					sg(f'{save["name"]} recieved {amount} {item}(s)')
				else:
					sg(line)

			save['flag']['characters_spoken'].append(trainer)

# pokemart location
def display_pokemart(save: dict, loc) -> None: # sourcery skip: low-code-quality
	choice = ''
	action_choice = ''
	pokemart_exit = False
	while not pokemart_exit:
		while not action_choice:
			while not action_choice:
				sp("\n[b] - Buy\n[s] - Sell\n[e] - Back\n")
				action_choice = get()
			if action_choice not in ['b', 's', 'e']:
				action_choice = ''
		if action_choice == 'e':
			pokemart_exit = True
		elif action_choice == 's':
			sp(f'\nMoney: ¥{"{:,}".format(save["money"])}')
			while not choice:
				options = ['e']
				max_name_length = (len(max(pokemart[loc], key=len)))
				for i, item in enumerate(pokemart[loc], start=1):
					options.append(str(i))
					price_len = len("{:,}".format(items[item]["price"]))
					sp(f'[{i}] - {item}{" "*(max_name_length-len(item))}{" "*(8-price_len)}¥{"{:,}".format(items[item]["sell_price"])}')
				sp('[e] - Back\n')
				while not choice:
					choice = get()
				if choice not in options:
					choice = ''
			if choice == "e":
				action_choice = ''
				choice = ''
			else:
				amount = 0
				try:
					in_bag = save['bag'][pokemart[loc][int(choice)-1]]
				except KeyError:
					in_bag = 0
				sp(f'\n{pokemart[loc][int(choice)-1]}: ¥{"{:,}".format(items[pokemart[loc][int(choice)-1]]["sell_price"])} (in bag: {in_bag})')
				sp(items[pokemart[loc][int(choice)-1]]["description"])
				sp("How many would you like to sell(1-99)? (press 'e' to go back)\n")
				while not amount:
					while not amount:
						amount = get()
					if amount == 'e':
						break
					if (not amount.isnumeric()) or int(amount) > 99 or int(amount) < 1:
						amount = ''
				if amount == 'e':
					choice = ''
					amount = ''
				elif in_bag < int(amount):
					sp(f'\nYou do not have enough items (you need {int(amount)-in_bag} more)')
					amount = ''
				else:
					save['bag'][pokemart[loc][int(choice)-1]] -= int(amount)
					save['money'] += items[pokemart[loc][int(choice)-1]]["sell_price"]*int(amount)
					debug(f'Sold {amount} {pokemart[loc][int(choice)-1]}s for ¥{items[pokemart[loc][int(choice)-1]]["sell_price"]*int(amount)}')
					choice = ''

		elif action_choice == 'b':
			sp(f'\nMoney: ¥{"{:,}".format(save["money"])}')
			while not choice:
				options = ['e']
				max_name_length = (len(max(pokemart[loc], key=len)))
				for i, item in enumerate(pokemart[loc], start=1):
					options.append(str(i))
					price_len = len("{:,}".format(items[item]["price"]))
					sp(f'[{i}] - {item}{" "*(max_name_length-len(item))}{" "*(8-price_len)}¥{"{:,}".format(items[item]["price"])}')
				sp('[e] - Back\n')
				while not choice:
					choice = get()
				if choice not in options:
					choice = ''
			if choice == "e":
				action_choice = ''
				choice = ''
			else:
				amount = 0
				try:
					in_bag = save['bag'][pokemart[loc][int(choice)-1]]
				except KeyError:
					in_bag = 0

				sp(f'\n{pokemart[loc][int(choice)-1]}: ¥{"{:,}".format(items[pokemart[loc][int(choice)-1]]["price"])} (in bag: {in_bag})')
				sp(items[pokemart[loc][int(choice)-1]]["description"])
				sp("How many would you like to buy(1-99)? (press 'e' to go back)\n")
				while not amount:
					while not amount:
						amount = get()
					if amount == 'e':
						break
					if (not amount.isnumeric()) or int(amount) > 99 or int(amount) < 1:
						amount = ''
				if amount == 'e':
					choice = ''
					amount = ''
				else:
					required_money = items[pokemart[loc][int(choice)-1]]["price"]*int(amount)
					if required_money > save['money']:
						sp(f'\nYou do not have enough money (you need ¥{required_money-save["money"]} more)')
						amount = ''
					else:
						if pokemart[loc][int(choice)-1] not in save['bag']:
							save['bag'][pokemart[loc][int(choice)-1]] = int(amount)
						else:
							save['bag'][pokemart[loc][int(choice)-1]] += int(amount)
						save['money'] -= required_money
						sp(f'\n{save["name"]} obtained {amount} {pokemart[loc][int(choice)-1]}(s)')
						choice = ''

# use item from bag
def use_item(save: dict, battle=False) -> Optional[str]:
	item_used = False
	sp('\nPlease choose an item to use.')
	if battle:
		sp('\n'.join(f'{key}: {save["bag"][key]}' for key in save['bag'] if items[key]['battle']))
	else:
		sp('\n'.join(f'{key}: {save["bag"][key]}' for key in save['bag']))
	sp('[e] - Back\n')
	while not item_used:
		item = ''
		while not item:
			item = get()
		if item == "e":
			return "exit"
		if item in save['bag']:
			if save['bag'][item] > 0:
				save['bag'][item] -= 1
				# exec(items[item]['command'])
				return item
			else:
				sp('You have none of that item!')

# pokemon center heal
def heal(save: dict, pokemon=None, party: Optional[list]=None, type='party') -> None:
	if party is None:
		party = []
	if type == 'party':
		party = party or save['party']
	elif type == 'single':
		pokemon = pokemon or save['party'][0]
		party = [pokemon]
	else:
		abort('Invalid heal type: neither party nor single.')
	sp('')
	for i in party:
			i.reset_stats()
			sp(f'{i.name} was healed to max health.')

	if type == 'party':
		backup(save, pokemon_centre=True)

# pokemon class
class Pokemon:

	# set internals
	def __init__(self, save: dict, species: str, level: int, ivs: dict, moves=None, chp=None, current_xp=0, fainted=False, player_pokemon = False) -> None:
		if ivs is None:
			ivs = {}
		self.species = species
		self.index = dex[self.species]['index']
		self.name = dex[self.species]['name']
		self.type = dex[self.species]['type']
		self.level = level
		self.ivs = ivs if ivs else {i: randint(0, 31) for i in ['hp', 'atk', 'def', 'spa', 'spd', 'spe']}
		self.level_type = dex[self.species]['xp']
		self.total_xp = xp['total'][self.level_type][str(self.level)]
		self.current_xp = current_xp
		self.moves = moves or find_moves(self.species, self.level)
		self.status = {
			'burn': False,
			'confusion': False,
			'freeze': False,
			'paralysis': False,
			'poison': False,
			'sleep': False
		}

		# update pokedex
		if self.species not in save['dex']:
			save['dex'].update({self.species: {'seen': True, 'caught': False}})
		else:
			if 'seen' not in save['dex'][self.species]:
				save['dex'][self.species]['seen'] = True
			if 'caught' not in save['dex'][self.species]:
				save['dex'][self.species]['caught'] = False
		if self.type not in save['flag']['type']:
			save['flag']['type'].update({self.type: {'seen': True, 'caught': False}})
		else:
			if 'seen' not in save['flag']['type'][self.type]:
				save['flag']['type'][self.species]['seen'] = True
			if 'caught' not in save['flag']['type'][self.type]:
				save['flag']['type'][self.species]['caught'] = False

		# initialise stats
		self.reset_stats(chp, fainted, player_pokemon)

	# reset stats
	def reset_stats(self, chp=None, fainted=None, player_pokemon = False) -> None:
			self.stats = {
				'hp': floor(((dex[self.species]['hp'] + self.ivs['hp']) * 2 + floor(ceil(sqrt(self.ivs['hp'])) / 4) * self.level) / 100) + self.level + 10,
				'atk': floor(((dex[self.species]['atk'] + self.ivs['atk']) * 2 + floor(ceil(sqrt(self.ivs['atk'])) / 4) * self.level) / 100) + 5,
				'def': floor(((dex[self.species]['def'] + self.ivs['def']) * 2 + floor(ceil(sqrt(self.ivs['def'])) / 4) * self.level) / 100) + 5,
				'spa': floor(((dex[self.species]['spa'] + self.ivs['spa']) * 2 + floor(ceil(sqrt(self.ivs['spa'])) / 4) * self.level) / 100) + 5,
				'spd': floor(((dex[self.species]['spd'] + self.ivs['spd']) * 2 + floor(ceil(sqrt(self.ivs['spd'])) / 4) * self.level) / 100) + 5,
				'spe': floor(((dex[self.species]['spe'] + self.ivs['spe']) * 2 + floor(ceil(sqrt(self.ivs['spe'])) / 4) * self.level) / 100) + 5
			}
			if player_pokemon == False:
				for move in self.moves:
					move['pp'] = list(filter(lambda m, move=move: m['name'] == move['name'], moves))[0]['pp']
			self.stats['chp'] = chp or self.stats['hp']
			self.fainted = fainted or self.stats['chp'] <= 0
			if self.fainted:
				self.stats['chp'] = 0

	def check_level_up(self) -> None:
		while self.current_xp >= xp['next'][self.level_type][str(self.level)]:
			self.current_xp -= xp['next'][self.level_type][str(self.level)]
			self.level_up(self)
			if self.level == 100:
				sp(f'\nCongratulations, {self.name} has reached level 100!')
				break

	# check if pokemon is fainted
	def check_fainted(self) -> bool:
		if self.stats['chp'] <= 0:
			self.stats['chp'] = 0
			self.fainted = True
			return True
		return False

	# lower chp when pokemon is attacked
	def deal_damage(self, save: dict, attacker, move) -> Optional[int]:
		move_entry = list(filter(lambda m: m['name'] == move['name'], moves))[0]
		sp(f'\n{attacker.name} used {move["name"].upper()}!')
		if move_entry['damage_class'] == 'status':
			# TODO: Implement status conditions
			sp(f'(Note: {move["name"].upper()} is a status move)')
		else:
			if randint(1,100) <= move_entry["accuracy"]:
				return self.damage_calc(save, move_entry, attacker)
			sp(f'{attacker.name} missed!')
			return 0

	def damage_calc(self, save: dict, move_entry, attacker):
		is_critical = critical()
		attack_defense = ('atk', 'def') if move_entry['damage_class'] == 'physical' else ('spa', 'spd')
		result = floor((((((2 * attacker.level * (2 if is_critical else 1) / 5) + 2) * move_entry['power'] * attacker.stats[attack_defense[0]] / self.stats[attack_defense[1]]) / 50) + 2) * (1.5 if move_entry['type'] == attacker.type else 1) * randint(217, 255) / 255 * (type_effectiveness(move_entry, self) if save['flag']['been_to_route_1'] else 1))

		self.stats['chp'] -= result
		if result > 0:
			sp(f'\n{attacker.name} dealt {result} damage to {self.name}!')
		if is_critical:
			sp('A critical hit!')
		for i in [
			(0, 'It had no effect!'),
			(0.5, 'It\'s super effective!'),
			(2, 'It\'s not very effective!')
		]:
			if types[self.type][move_entry['type'].upper()] == i[0]:
				sp(f'{i[1]}')
		self.check_fainted()
		if self.fainted:
			sp(f'\n{self.name} fainted!')
		return result

	def deal_struggle_damage(self, damage):
		sp(f'{self.name} is hit with recoil!')
		self.stats['chp'] -= floor(damage / 2)
		self.check_fainted()
		if self.fainted:
			sp(f'\n{self.name} fainted!')

	# calculate xp rewarded after battle
	def calculate_xp(self, battle_type='wild') -> int:
		return ceil((self.total_xp * self.level * (1 if battle_type == 'wild' else 1.5)) / 7) 

	# give xp from opponent pokemon to party in battle
	def give_xp(self, save, participating_pokemon, type='wild'):
		total_xp = self.calculate_xp(type)
		debug(f'total xp: {total_xp}')
		if 'EXP. ALL' in save['bag']:
			for p in participating_pokemon:
				save['party'][p].current_xp += floor(total_xp / (len(participating_pokemon) + 1))
				sg(f'{save["party"][p].name} gained {floor(total_xp / (len(participating_pokemon) + 1))} XP!')
				save['party'][p].check_level_up()

			other_pokemon = [pokemon for pokemon in save['party'] if pokemon not in participating_pokemon]
			for o in other_pokemon:
				save['party'][o].current_xp += floor((total_xp / (len(participating_pokemon) + 1)) / len(other_pokemon))
				sg(f'{save["party"][o].name} gained {floor((total_xp / (len(participating_pokemon) + 1)) / len(other_pokemon))} XP!')
				save['party'][o].check_level_up()

		else:
			for p in participating_pokemon:
				save['party'][p].current_xp += floor(total_xp / len(participating_pokemon))
				sg(f'{save["party"][p].name} gained {floor(total_xp / len(participating_pokemon))} XP!')
				save['party'][p].check_level_up()
			sp("")
		sleep(0.5)

	# evolve pokemon
	def evolve(self, save: dict):
		sp(f'\nWhat? {self.name} is evolving!')
		input_cancel = getch()
		# for _ in range(3):
		if input_cancel in ['e','b']:
			sg(f'{self.name} didn\'t evolve')
			return

		sleep(0.5)
		print("...")
		sleep(2)

		self.index += 1
		old_name = self.name
		for p in dex.keys():
			if dex[p]['index'] == self.index:
				self.species = p
				self.name = dex[self.species]['name']
		self.reset_stats()
		sg(f'\n{old_name} evolved into {self.species}!') 

		save['dex'][self.species] = {'seen': True, 'caught': True}
		save['flag']['type'][self.type] = {'seen': True, 'caught': True}
		for move in dex[self.species]['moves']:
			# TODO: Possibly keep track of moves that were forgotten too and not reprompt to learn as well?
			if move['level'] <= self.level and move['name'] not in (m['name'] for m in self.moves):
				self.learn_move(move)

	def learn_move(self, move): # sourcery skip: low-code-quality
		if len(self.moves) == 4:
			sg(f'{self.name} wants to learn {move["name"].upper()}!')
			sg(f'But {self.name} already knows 4 moves')
			all_moves = [*self.moves, move]
			move_forgotten = False
			while not move_forgotten:
				sp(f'Which move should {self.name} forget?\n')
				for i in range(5):
					print(f'[{i+1}] - {all_moves[i]["name"].upper().replace("-", " ")}')
				forget_move = ''
				while not forget_move:
					forget_move = get()
					if forget_move not in ['1', '2', '3', '4', '5']:
						forget_move = ''
					else:
						if forget_move == '5':
							sp(f'\nAre you sure you want {self.name} to not learn {move["name"].upper()}? (Y/N)')
						else:
							sp(f'\nAre you sure you want {self.name} to forget {all_moves[int(forget_move)-1]["name"].upper()}? (Y/N)')
						option = ''
						while option not in ['y','n']:
							option = get()
						if option in ['y']:
							if forget_move == '5':
								sp(f'\n{self.name} didn\'t learn {move["name"].upper()}')
							else:
								sp(f'\n{self.name} forgot {all_moves[int(forget_move)-1]["name"].upper()}\n')
								sp(f'\n{self.name} learned {move["name"].upper()}!')
								self.moves = [move for move in self.moves if move['name'] != all_moves[int(forget_move) - 1]['name']]
								self.moves.append({"name": move['name'], "pp": list(filter(lambda mv: mv['name'] == move['name'], moves))[0]['pp']})
							move_forgotten = True
		else:
			sg(f'{self.name} learned {move["name"].upper()}')
			self.moves.append({"name": move['name'], "pp": list(filter(lambda mv, move=move: mv['name'] == move['name'], moves))[0]['pp']}) 

	# raw level up
	def level_up(self, pokemon):
		pokemon.level += 1
		pokemon.reset_stats()
		sg(f'{pokemon.name} grew to level {pokemon.level}!')
		if ('evolution' in dex[pokemon.species]	and pokemon.level >= dex[pokemon.species]['evolution']):
			pokemon.evolve()
		for m in dex[pokemon.species]['moves']:
			if m['level'] == pokemon.level:
				pokemon.learn_move(m)

	# catch Pokemon
	def catch(self, save: dict, ball: str) -> bool: # sourcery skip: low-code-quality
		if max(bool(self.status[i]) for i in ['freeze', 'sleep']):
			status = 25
		elif max(bool(self.status[i]) for i in ['burn', 'poison', 'paralysis']):
			status = 12
		else:
			status = 0

		# find Poke Ball type
		ball_modifier = 0
		if ball == "Great Ball":
			ball_modifier = 201
		elif ball == "Master Ball":
			pass # guaranteed catch
		elif ball == "Poke Ball":
			ball_modifier = 256
		elif ball == "Ultra Ball":
			ball_modifier = 151
		else:
			abort(f'Invalid ball: {ball}')

		# decide whether caught
		C = dex[self.species]['catch']
		if ball == "Master Ball":
			catch = True
		elif self.stats['hp'] / (2 if ball == "Great Ball" else 3) >= self.stats['chp'] and (status + C + 1) / ball_modifier >= 1:
			catch = True
		else:
			X = randint(0, ball_modifier-1)
			if X < status:
				catch = True
			elif X > status + C:
				catch = False
			else:
				catch = min(
					255,
					self.stats['hp'] * 255 // (8 if ball == "Great Ball" else 12) // max(1, floor(self.stats['chp'] / 4))
					) >= randint(0, 255)

		if catch:
			return self.add_caught_pokemon(save)
		wobble_chance = ((C * 100) // ball_modifier * min(255, self.stats['hp'] * 255 // (8 if ball == "Great Ball" else 12) // max(1, floor(self.stats['chp'] / 4)))) // 255 + status
		debug(wobble_chance)

		if wobble_chance >= 0 and wobble_chance < 10: # No wobbles
			sp('The ball missed the Pokémon!')
		elif wobble_chance >= 10 and wobble_chance < 30: # 1 wobble
			sp('Darn! The Pokémon broke free!')
		elif wobble_chance >= 30 and wobble_chance < 70: # 2 wobbles
			sp('Aww! It appeared to be caught!')
		elif wobble_chance >= 70 and wobble_chance <= 100: # 3 wobbles
			sp('Shoot! It was so close too!')
		return False

	# once pokemon is caught, add to party or box
	def add_caught_pokemon(self, save):
		location = 'party' if len(save['party']) < 6 else 'box'
		save[location].append(self)
		save['dex'][self.species] = {'seen': True, 'caught': True}
		save['flag']['type'][self.type] = {'seen': True, 'caught': True}
		sg(f'\nYou caught {self.name}!')
		sg(f'\n{self.name} (`{self.type}`-type) was added to your {location}.')
		return True

# BATTLES

# battle screen variables
name_length = 15
bars_length = 20

# get pokemon to encounter
def get_encounter(loc, type) -> dict:
	pokemon = []
	weights = []
	for chance in rates[loc][type]:
		for i in range(len(rates[loc][type][chance])):
			pokemon.append(rates[loc][type][chance][i])
			weights.append(int(chance)/255)
	return choices(pokemon, weights)[0]

# check if party is alive
def is_alive(party: list[Pokemon]) -> bool:
	return any(not i.fainted for i in party)

# decide if damage is critical
def critical() -> bool:
	return randint(0, 255) <= 17

# randomise escape
def escape(pokemon, opponent, escape_attempts) -> bool:
	return floor((pokemon.stats['spe'] * 32) / (floor(opponent.stats['spe'] / 4) % 256)) + 30 * escape_attempts > 255 or floor(opponent.stats['spe'] / 4) % 256 == 0

# calculate type effectiveness
def type_effectiveness(move, defender) -> float:
	return types[move['type'].upper()][defender.type] 

# calculate prize money
def prize_money(save, party=None, type='Pokémon Trainer') -> int:
	return floor(trainer_types[type] * max(i.level for i in (party or save['party'])))

# find moves of a wild pokemon
def find_moves(name, level) -> list:
	learned_moves = [{**move, "pp": list(filter(lambda m, move=move: m['name'] == move['name'], moves))[0]['pp']} for move in dex[name]['moves'] if move['level'] <= level] 

	learned_moves = sorted(learned_moves, key=lambda m: m['level'], reverse=True)
	if len(learned_moves) >= 4:
		return list(map(lambda m: {"name": m['name'], "pp": m["pp"]}, learned_moves[:4]))
	else:
		return list(map(lambda m: {"name": m['name'], "pp": m["pp"]}, learned_moves))

# switch pokemon in battle
def switch_pokemon(save: dict, party_length: int) -> Union[int, str]:
	sp(f'''\nWhich Pokémon should you switch to?\n\n{
				chr(10).join(f'{f"[{i+1}]" if not save["party"][i].check_fainted() else "FAINTED"} - {save["party"][i].name} ({save["party"][i].stats["chp"]}/{save["party"][i].stats["hp"]}) - Level {save["party"][i].level} ({colours[save["party"][i].type.upper()]}{save["party"][i].type}{colours["NORMAL"]})' for i in range(party_length))
			}''')
	sp('[e] - Back\n')
	switch_choice = ''
	while not switch_choice:
		while switch_choice == '':
			switch_choice = get()
		if switch_choice == 'e':
			return 'exit'
		try:
			if switch_choice not in [str(i+1) for i in range(party_length)]:
				switch_choice = ''
				sp('\nInvalid choice.')
			elif save['party'][int(switch_choice)-1].check_fainted():
				switch_choice = ''
				sp('That Pokémon is fainted!')
		except (TypeError, ValueError):
			switch_choice = ''
			sp('\nInvalid choice.')
	return int(switch_choice)

# create battle process
def battle(save: dict, opponent_party: list=[], battle_type='wild', name=None, title=None, start_diagloue=None, end_dialouge=None, earn_xp=True) -> None:
	debug('Entered battle!')
	debug(f'Party: {[i.name for i in save["party"]]}')
	party_length = len(save['party'])
	current = ''
	opponent_current = 0
	for i in range(party_length):
		if not save['party'][i].check_fainted():
			debug(f'{save["party"][i].name} is the first alive Pokemon in the party.')
			current = i
			break

	# battle intro
	if battle_type == 'trainer':
		sg(f'\n{name if name else title}: {start_diagloue}')
		sg(f'\n{title} {name+" " if name else ""}wants to fight!')
	elif battle_type == 'wild':
		sp(f'\nA wild {opponent_party[opponent_current].name} appeared!')
	else:
		abort('\nInvalid battle type: neither trainer nor wild.')
	sp(f'\nGo, {save["party"][current].name}!')
	sleep(0.5)
	if battle_type == 'trainer':
		sp(f'\n{name if name else title} sent out {opponent_party[opponent_current].name}!') 

	# battle variables
	escaped_from_battle = False
	escape_attempts = 0
	caught = False
	catch_attempt = False
	switched = False
	participating_pokemon = [current]

	# check if parties are alive
	debug(f'\nPlayer party alive: {is_alive(save["party"])}\nOpponent party alive: {is_alive(opponent_party)}')

	# battle loop
	while is_alive(save['party']) and is_alive(opponent_party):

		# player turn
		debug('Turn start!')
		player_attacked_this_turn = False
		opponent_attacked_this_turn = False
		catch_attempt = False
		switched = False
		move_choice = ''
		chosen_move = {}

		# calculate health bars according to ratio (chp:hp)
		bars = ceil((save['party'][current].stats['chp']/(save['party'][current].stats['hp']))*bars_length)
		opponent_bars = ceil((opponent_party[opponent_current].stats['chp']/(opponent_party[opponent_current].stats['hp']))*bars_length)
		debug(f'Player bars: {bars}\nOpponent bars: {opponent_bars}')
		debug(f'Player level: {save["party"][current].level}\nOpponent level: {opponent_party[opponent_current].level}')
		sp(f'''\n{save["party"][current].name}{' '*(name_length-len(save['party'][current].name))}[{'='*bars}{' '*(bars_length-bars)}] {str(save['party'][current].stats['chp'])}/{save['party'][current].stats['hp']} (`{save["party"][current].type}`) Lv. {save["party"][current].level}\n{opponent_party[opponent_current].name}{' '*(name_length-len(opponent_party[opponent_current].name))}[{'='*opponent_bars}{' '*(bars_length-opponent_bars)}] {opponent_party[opponent_current].stats['chp']}/{opponent_party[opponent_current].stats['hp']} (`{opponent_party[opponent_current].type}`) Lv. {opponent_party[opponent_current].level}''')
		sp(f'\nWhat should {save["party"][current].name} do?\n\n[1] - Attack\n[2] - Switch\n[3] - Item\n[4] - Run\n')

		user_choice = ''
		valid_choice = False
		while not valid_choice:
			user_choice = get()
			if user_choice == '2' and len(save['party']) == 1:
				sp('You can\'t switch out your only Pokémon!')
			elif user_choice == '3' and len(save['bag']) == 0:
				sp('You have no items!')
			elif user_choice == '4' and battle_type == 'trainer':
				sp('You can\'t run from a trainer battle!')
			elif user_choice in ['1', '2', '3', '4']:
				valid_choice = True

		# choose attack
		if user_choice == '1':
			struggle = True
			for move_iter in save['party'][current].moves:
				if move_iter['pp'] > 0:
					struggle = False
			if struggle:
				sp(f'{save["party"][current].name} has no moves left!')
				chosen_move = {'name': 'struggle'}
			else:
				options = []
				sp('')
				move_names = []
				type_names = []
				for i in save['party'][current].moves:
					move_names.append(i['name'])
					type_names.append(list(filter(lambda m, i=i: m['name'] == i['name'], moves))[0]['type'])
				longest_move_name_length = len(max(move_names, key=len))
				longest_type_name_length = len(max(type_names, key=len))

				for i in range(len(save['party'][current].moves)):
					move_entry = list(filter(lambda m, i=i: m['name'] == save['party'][current].moves[i]['name'], moves))[0]
					sp(f'[{i+1}] - {save["party"][current].moves[i]["name"].upper().replace("-"," ")}{" "*(longest_move_name_length-len(save["party"][current].moves[i]["name"].upper().replace("-"," ")))} | `{move_entry["type"].upper()}`{" "*(longest_type_name_length-len(move_entry["type"].upper()))} - {save["party"][current].moves[i]["pp"]}/{move_entry["pp"]}')
					options.append(str(i+1))
				sp('[e] - Back\n')

				valid_choice = False
				while not valid_choice:
					move_choice = get()
					if move_choice in options:
						if save['party'][current].moves[int(move_choice)-1]['pp'] == 0:
							sp(f'{save["party"][current].name} cannot use {save["party"][current].moves[int(move_choice)-1]["name"]}')
						else: valid_choice = True
					elif move_choice == "e":
						valid_choice = True
				if move_choice == "e":
					continue

				chosen_move = save["party"][current].moves[int(move_choice)-1] 

			if save['party'][current].stats['spe'] >= opponent_party[opponent_current].stats['spe']:
				damage = opponent_party[opponent_current].deal_damage(save['party'][current], chosen_move)
				if chosen_move["name"] == "struggle":
					save['party'][current].deal_struggle_damage(damage)
				else:
					save["party"][current].moves[int(move_choice)-1]['pp'] -= 1 

				player_attacked_this_turn = True

		# choose switch
		elif user_choice == '2':
			switch_choice = switch_pokemon(save, party_length)

			if switch_choice == "exit":
				continue

			if int(switch_choice)-1 == current:
				continue

			current = int(switch_choice)-1
			switched = True
			if int(switch_choice)-1 not in participating_pokemon:
				participating_pokemon.append(current)

		# choose item
		elif user_choice == '3':
			item = use_item(save, battle=True)
			if item == "exit":
				continue
			if (item == 'Poke Ball' or item == 'Great Ball' or item == 'Ultra Ball' or item == 'Master Ball') and battle_type == 'trainer':
				sp("You can't catch another trainer's Pokémon!")
			elif item == 'Poke Ball':
				if opponent_party[opponent_current].catch("Poke Ball"):
					caught = True
					break
				else: catch_attempt = True
			elif item == 'Great Ball':
				if opponent_party[opponent_current].catch("Great Ball"):
					caught = True
					break
				else: catch_attempt = True
			elif item == 'Ultra Ball':
				if opponent_party[opponent_current].catch("Ultra Ball"):
					caught = True
					break
				else: catch_attempt = True
			elif item == 'Master Ball':
				if opponent_party[opponent_current].catch("Master Ball"):
					caught = True
					break
				else: catch_attempt = True

		# choose run
		elif user_choice == '4':
			if escape(save['party'][current], opponent_party[opponent_current], escape_attempts):
				escaped_from_battle = True
				break
			else:
				escape_attempts += 1

		# reset consecutive escape attempts
		if user_choice != '4':
			escape_attempts = 0

		# opponent attack
		if not save['party'][current].check_fainted() and not opponent_party[opponent_current].check_fainted():
			save['party'][current].deal_damage(opponent_party[opponent_current], choice(opponent_party[opponent_current].moves))
			opponent_attacked_this_turn = True

		# player attack if player speed is lower
		if save['party'][current].check_fainted() and opponent_party[opponent_current].check_fainted() and not player_attacked_this_turn and escape_attempts == 0 and not catch_attempt and not switched:
			damage = opponent_party[opponent_current].deal_damage(save['party'][current], chosen_move)
			if chosen_move['name'] == 'struggle':
				save['party'][current].deal_struggle_damage(damage)
			else:
				save['party'][current].moves[int(move_choice)-1]['pp'] -= 1
			player_attacked_this_turn = True

		# give XP when opponent faints
		if opponent_party[opponent_current].check_fainted() and earn_xp == True:
			opponent_party[opponent_current].give_xp(participating_pokemon, battle_type)
			if battle_type == 'trainer' and is_alive(opponent_party):
				opponent_current += 1
				sp(f'\n{name if name else title} sent out {opponent_party[opponent_current].name}!') 

		# end battle if player wins or loses
		if is_alive(save['party']) and not is_alive(opponent_party) or not is_alive(save['party']):
			break

		if save['party'][current].check_fainted():
			participating_pokemon = list(filter(lambda p, current=current: save['party'][p].name != save['party'][current].name, participating_pokemon))
			switch_choice = switch_pokemon(save, party_length)
			current = int(switch_choice)-1
			switched = True
			if int(switch_choice)-1 not in participating_pokemon:
				participating_pokemon.append(current)

		# display turn details
		debug(f'Higher Speed: {"Player" if save["party"][current].stats["spe"] > opponent_party[opponent_current].stats["spe"] else "Opponent"}\nPlayer Attacked: {player_attacked_this_turn}\nOpponent Attacked: {opponent_attacked_this_turn}\n') 

	# upon escaping
	if escaped_from_battle:
		sp('You escaped!')

	# upon catching
	elif caught:
		# TODO: earn xp
		pass 

	# upon winning
	elif is_alive(save['party']) and not is_alive(opponent_party):
		if save['flag']['been_to_route_1']:
			if battle_type == 'trainer':
				sg(f'\n{save["name"]} won the battle!')
				save['money'] += prize_money(opponent_party, title)
				sg(f'You recieved ¥{prize_money(opponent_party, title)} as prize money.')
				sg(f'\n{name if name else title}: {end_dialouge}')
		else:
			save['flag']['won_first_battle'] = True

	# upon losing
	elif is_alive(opponent_party) and (not is_alive(save['party'])):
		if battle_type == 'trainer':
			if save['flag']['been_to_route_1']:
				sg('You lost the battle!')
				sg(f'You gave ¥{round(save["money"] / 2)} as prize money.')
			else:
				save['flag']['won_first_battle'] = False
		sg('...')
		sg(f'{save["name"]} blacked out!')
		save['money'] = round(save['money'] / 2)
		save['location'] = save['recent_center']
		heal(save)

	# if battle is neither won nor lost
	else:
		abort('\nInvalid battle state; neither won, lost, caught, nor escaped. Could not load player turn.')
