import json, pprint, requests, textwrap
host = 'http://livy-server:8998'

r = requests.delete(host + '/sessions/0')
pprint.pprint(r.json())
