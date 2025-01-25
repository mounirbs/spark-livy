import json, pprint, requests, textwrap
host = 'http://livy-server:8998'
headers = {'Content-Type': 'application/json'}
statements_url = host + '/sessions/0/statements'

data = {
  'code': textwrap.dedent("""
    df = spark.createDataFrame([{"id": 1, "name": "Mounir2"}])

    df.show()
    """)
}

r = requests.post(statements_url, data=json.dumps(data), headers=headers)
pprint.pprint(r.json())