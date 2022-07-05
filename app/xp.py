import json, os, sys
output = {
	"total": {
		"Erratic": {
			"1": 1
		}
	}
}
source = json.load(open(os.path.join(sys.path[0], 'data/experience.json')))
open(os.path.join(sys.path[0], 'level.json'), 'w').write('')
for i in range(100):
	output['total']['Erratic'][str(i+1)] = source[i]['Erratic total']
	output['total']['Fast'][str(i+1)] = source[i]['Fast total']
	output['total']['Medium Fast'][str(i+1)] = source[i]['Medium Fast total']
	output['total']['Medium Slow'][str(i+1)] = source[i]['Medium Slow total']
	output['total']['Slow'][str(i+1)] = source[i]['Slow total']
	output['total']['Fluctuating'][str(i+1)] = source[i]['Fluctuating total']
	output['next']['Erratic'][str(i+1)] = source[i]['Erratic next']
	output['next']['Fast'][str(i+1)] = source[i]['Fast next']
	output['next']['Medium Fast'][str(i+1)] = source[i]['Medium Fast next']
	output['next']['Medium Slow'][str(i+1)] = source[i]['Medium Slow next']
	output['next']['Slow'][str(i+1)] = source[i]['Slow next']
	output['next']['Fluctuating'][str(i+1)] = source[i]['Fluctuating next']
json.dump(output, open(os.path.join(sys.path[0], 'level.json'), 'w'), indent=4)
