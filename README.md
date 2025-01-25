# spark-livy
Spark Livy How-To

## Docker Compose
**Start docker compose**
```docker-compose up --scale spark-worker=1```

**Start only one service**
```
docker compose -f 'docker-compose.yml' up -d --build '<service_name>'
```

## Spark Submit
**Submit a Spark job**
```
spark-submit --master spark://spark-master:7077 /python/test_spark.py
spark-submit --master spark://spark-master:7077 /python/test_pandas.py
```
## Spark REST API
**Submit a job to the Spark Cluster**
```
curl -X POST http://localhost:6066/v1/submissions/create --header "Content-Type:application/json;charset=UTF-8" --data '{"appResource": "","sparkProperties": {"spark.master": "spark://spark-master:7077","spark.app.name": "TestFromRestCall"},"clientSparkVersion": "","mainClass": "org.apache.spark.deploy.SparkSubmit","environmentVariables": { },"action": "CreateSubmissionRequest","appArgs": [ "/python/test_spark.py" ]}'

{
  "action" : "CreateSubmissionResponse",
  "message" : "Driver successfully submitted as driver-20250124235149-0000",
  "serverSparkVersion" : "3.3.0",
  "submissionId" : "driver-20250124235149-0000",
  "success" : true
}

```
**Get the status of a Spark Job**
```
curl -X GET http://localhost:6066/v1/submissions/status/<submissionId>

{
  "action" : "SubmissionStatusResponse",
  "driverState" : "FINISHED",
  "serverSparkVersion" : "3.3.0",
  "submissionId" : "driver-20250124235149-0000",
  "success" : true,
  "workerHostPort" : "172.21.0.3:37965",
  "workerId" : "worker-20250124234947-172.21.0.3-37965"
}
```
## Apache Livy
**Based on [Apache Livy 0.8.0-incubating - REST API](https://livy.apache.org/docs/latest/rest-api.html)**

Create a Livy Session (this will return a session id(0))
```
curl -X POST --data '{"kind": "pyspark", "name": "test pyspark session from python REST API"}' -H "Content-Type: application/json" localhost:8998/sessions

{
   "id":0,
   "name":"test pyspark session from python REST API",
   "appId":null,
   "owner":null,
   "proxyUser":null,
   "state":"starting",
   "kind":"pyspark",
   "appInfo":{
      "driverLogUrl":null,
      "sparkUiUrl":null
   },
   "log":[
      "stdout: ",
      "\nstderr: "
   ],
   "ttl":null,
   "driverMemory":null,
   "driverCores":0,
   "executorMemory":null,
   "executorCores":0,
   "conf":{      
   },
   "archives":[      
   ],
   "files":[      
   ],
   "heartbeatTimeoutInSecond":0,
   "jars":[      
   ],
   "numExecutors":0,
   "pyFiles":[      
   ],
   "queue":null
}
```
Wait for an idle status for the session id(0) before running the code
```
curl -X GET localhost:8998/sessions/0

{
   "id":0,
   "name":"test pyspark session from python REST API",
   "appId":null,
   "owner":null,
   "proxyUser":null,
   "state":"idle",
   "kind":"pyspark",
   "appInfo":{
      "driverLogUrl":null,
      "sparkUiUrl":null
   },
   "log":[
      ""
    ],
   "ttl":null,
   "driverMemory":null,
   "driverCores":0,
   "executorMemory":null,
   "executorCores":0,
   "conf":{      
   },
   "archives":[      
   ],
   "files":[      
   ],
   "heartbeatTimeoutInSecond":0,
   "jars":[      
   ],
   "numExecutors":0,
   "pyFiles":[      
   ],
   "queue":null
}
```

Execute a PySpark code on the idle session id(0). This will return a statement id(0)
```
curl -X POST -H 'Content-Type: application/json' -d'{"code":"spark.createDataFrame([{\"id\": 1, \"name\": \"Mounir\"}]).show()"}' localhost:8998/sessions/0/statements

{
   "id":0,
   "code":"spark.createDataFrame([{\"id\": 1, \"name\": \"Mounir\"}]).show()",
   "state":"running",
   "output":null,
   "progress":0.0,
   "started":1737759484430,
   "completed":0
}
```
Check the statement id(0) on the session id(0)
```
curl -X GET localhost:8998/sessions/0/statements/0

{
   "id":0,
   "code":"spark.createDataFrame([{\"id\": 1, \"name\": \"Mounir\"}]).show()",
   "state":"available",
   "output":{
      "status":"ok",
      "execution_count":1,
      "data":{
         "text/plain":
         "+---+------+\n
         | id|  name|\n
         +---+------+\n
         |  1|Mounir|"
      }
   },
   "progress":1.0,
   "started":1737759484430,
   "completed":1737759492048
}
```
Close the session id(0)
```
curl localhost:8998/sessions/0 -X DELETE 
```