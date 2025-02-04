import json, pprint, requests, textwrap
host = 'http://localhost:443'

r = requests.get(host + '/sessions/0')
pprint.pprint(r.json())
