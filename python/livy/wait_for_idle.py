data = {'kind': 'pyspark'}
r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)
r.json()