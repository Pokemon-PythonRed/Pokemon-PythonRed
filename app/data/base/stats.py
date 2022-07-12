import json, os, sys
source = json.load(open(os.path.join(sys.path[0], 'xptypes.json')))
evolution = json.load(open(os.path.join(sys.path[0], 'evolution.json')))
catch = json.load(open(os.path.join(sys.path[0], 'catchrates.json')))
open(os.path.join(sys.path[0], 'stats.json'), 'w').write('')
with open(os.path.join(sys.path[0], '../dex.json'), 'a') as output:
	print('{\n')
	output.write('{\n')
	for i in range(len(source)):
		currentEvolution = next(
			(
				evolution[j]['Level'] for j in range(len(evolution))
				if source[i]['#'] == evolution[j]['Ndex']
			), ''
		)
		text = f'''	"{source[i]['Name'].upper()}": {{
		"index": {i + 1},
		"name": "{source[i]['Name']}",
		"type": "{source[i]['Type']}",{f"""
		"catch": {catch[int(source[i]['#']) - 1]['Catch Rate']},""" if i < len(catch) - 1 else ''}
		"xp": "{source[i]['XP Type']}",{f"""
		"evolution": {currentEvolution},""" if currentEvolution else ''}
		"total": {source[i]['Total']},
		"hp": {source[i]['HP']},
		"atk": {source[i]['Attack']},
		"def": {source[i]['Defense']},
		"spa": {source[i]['Sp. Atk']},
		"spd": {source[i]['Sp. Def']},
		"spe": {source[i]['Speed']}
	}},
'''
		print(text)
		output.write(text)
	print('}')
	output.write('}')
