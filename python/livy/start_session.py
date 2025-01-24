# from https://livy.apache.org/examples/
# requires pip install requests
import json, pprint, requests, textwrap
host = 'http://livy-server:8998'
data = {'kind': 'pyspark'}
headers = {'Content-Type': 'application/json'}
r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)
print(r.json())
