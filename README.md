# spark-livy
Spark Livy provides a local environment for developing Spark applications on Docker. It simulates a Spark cluster and integrates Apache Livy to efficiently manage Spark sessions.

## Tested on
Spark 3.5.4, Apache Livy 0.8, Java 11

## Issues
Apache Livy may not be supported yet with newer Spark versions. See : [Apache Livy Jira - Add support for Spark 3.5.4](https://issues.apache.org/jira/browse/LIVY-1010)

## Install Python requirements for tests
```
pip install -r requirements.txt
```

## Build and Start services (Spark Master, Spark Worker and Apache Livy)
```
docker compose up -d
```

## Testing the Spark Cluster - Spark Submit
**Submit a Spark job**
```
spark-submit --master spark://spark-master:7077 /python/spark-submit/test_spark.py
spark-submit --master spark://spark-master:7077 /python/spark-submit/test_pandas.py
```
## Testing the Spark Cluster - Spark REST API
**Submit a job to the Spark Cluster**
```
curl -X POST http://localhost:6066/v1/submissions/create --header "Content-Type:application/json;charset=UTF-8" --data '{"appResource": "","sparkProperties": {"spark.master": "spark://spark-master:7077","spark.app.name": "TestFromRestCall"},"clientSparkVersion": "","mainClass": "org.apache.spark.deploy.SparkSubmit","environmentVariables": { },"action": "CreateSubmissionRequest","appArgs": [ "/python/spark-submit/test_spark.py" ]}'

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

### Apache Livy REST API
Create a Livy Session (this will return a session id(0))
```
curl -X POST --data '{"kind": "pyspark", "name": "test pyspark session from python REST API", "proxyUser": "Mounir"}' -H "Content-Type: application/json" localhost:8998/sessions

{
   "id":0,
   "name":"test pyspark session from python REST API",
   "appId":null,
   "owner":null,
   "proxyUser":"Mounir",
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
   "proxyUser":"Mounir",
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

initiate PySpark. This will return a statement id(0)
```
curl -X POST -H 'Content-Type: application/json' -d'{"code":"from py4j.java_gateway import java_import\njava_import(spark._sc._jvm, \"org.apache.spark.sql.api.python.*\")"}' localhost:8998/sessions/0/statements

{
   "id":0,
   "code":"from py4j.java_gateway import java_import\njava_import(spark._sc._jvm, \"org.apache.spark.sql.api.python.*\")",
   "state":"waiting",
   "output":null,
   "progress":0.0,
   "started":0,
   "completed":0
}
```

Execute a PySpark code on the idle session id(0). This will return a statement id(1)
```
curl -X POST -H 'Content-Type: application/json' -d'{"code":"spark.createDataFrame([{\"id\": 1, \"name\": \"Mounir\"}]).show()"}' localhost:8998/sessions/0/statements

{
   "id":1,
   "code":"spark.createDataFrame([{\"id\": 1, \"name\": \"Mounir\"}]).show()",
   "state":"running",
   "output":null,
   "progress":0.0,
   "started":1737759484430,
   "completed":0
}
```
Check the statement id(1) on the session id(0)
```
curl -X GET localhost:8998/sessions/0/statements/1

{
   "id":1,
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

### Apache Livy REST API using Python Request library
```
python ./python/livy/start_session.py
python ./python/livy/wait_for_idle.py
python ./python/livy/init_java_gateway.py
python ./python/livy/run_code.py
python ./python/livy/run_code_external_file.py
python ./python/livy/delete_session.py
```
## Convert docker-compose to Helm chart
```
kompose --file docker-compose.yml convert -o helm -c
```
Some adjustments/cleaning was done on the helm chart created by kompose.

## Helm
```
helm package helm/spark-livy -d helm/

kubectl create namespace spark-livy

helm install -n spark-livy spark-livy helm/spark-livy-0.0.1.tgz

kubectl -n spark-livy get all

helm uninstall spark-livy -n spark-livy
```
