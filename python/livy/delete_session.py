import json, pprint, requests, textwrap
host = 'http://localhost:443'

r = requests.delete(host + '/sessions/0')
pprint.pprint(r.json())
