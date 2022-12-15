from json import dumps, load
from os import path
from sys import path as syspath
with open(path.join(syspath[0], 'data/dex.json')) as f:
	old_dex = load(f)
new_dex = {}
for i in range(len(old_dex)):
	for key, dex_entry in old_dex.items():
		if dex_entry['index'] == i:
			new_dex[key] = dex_entry
			print(f'Added {dex_entry["name"]}')
			break
with open(path.join(syspath[0], 'data/dex.json'), 'w') as f:
	f.write(dumps(new_dex, indent=4).replace('    ', '\t'))
