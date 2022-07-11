import json, os, sys
output = {
	'total': {
		'erratic': {
			'1': 1
		}
	}
}
source = json.load(open(os.path.join(sys.path[0], 'experience.json')))
open(os.path.join(sys.path[0], '../level.json'), 'w').write('')
for i in range(100):
	output['total']['erratic'][str(i+1)] = source[i]['Erratic total']
	output['total']['fast'][str(i+1)] = source[i]['Fast total']
	output['total']['mediumfast'][str(i+1)] = source[i]['Medium Fast total']
	output['total']['mediumslow'][str(i+1)] = source[i]['Medium Slow total']
	output['total']['slow'][str(i+1)] = source[i]['Slow total']
	output['total']['fluctuating'][str(i+1)] = source[i]['Fluctuating total']
	output['next']['erratic'][str(i+1)] = source[i]['Erratic next']
	output['next']['fast'][str(i+1)] = source[i]['Fast next']
	output['next']['mediumfast'][str(i+1)] = source[i]['Medium Fast next']
	output['next']['mediumslow'][str(i+1)] = source[i]['Medium Slow next']
	output['next']['slow'][str(i+1)] = source[i]['Slow next']
	output['next']['fluctuating'][str(i+1)] = source[i]['Fluctuating next']
json.dump(output, open(os.path.join(sys.path[0], 'level.json'), 'w'), indent=4, ensure_ascii=False)
