# from https://livy.apache.org/examples/

import json, pprint, requests, textwrap
host = 'http://livy_server:8998'
data = {'kind': 'spark'}
headers = {'Content-Type': 'application/json'}
r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)
print(r.json())
