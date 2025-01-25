import json, pprint, requests, textwrap
host = 'http://livy-server:8998'

r = requests.get(host + '/sessions/1')
pprint.pprint(r.json())
