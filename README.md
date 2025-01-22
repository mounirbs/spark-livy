# spark-livy
Spark Livy How-To

## Docker Compose
**Start docker compose**
```docker-compose up --scale spark-worker=1```

## Spark Submit
**Submit a Spark job**
```
spark-submit --master spark://spark-master:7077 /python/test_spark.py
spark-submit --master spark://spark-master:7077 /python/test_pandas.py
```
## Spark REST API
**Submit a job to the Spark Cluster**
```
curl -XPOST http://localhost:6066/v1/submissions/create --header "Content-Type:application/json;charset=UTF-8" --data '{"appResource": "","sparkProperties": {"spark.master": "spark://spark-master:7077","spark.app.name": "TestFromRestCall"},"clientSparkVersion": "","mainClass": "org.apache.spark.deploy.SparkSubmit","environmentVariables": { },"action": "CreateSubmissionRequest","appArgs": [ "/python/test_spark.py" ]}'
```
**Get the status of a Spark Job**
```
curl -XGET http://localhost:6066/v1/submissions/status/<JobID>
```
## Apache Livy
**Based on [Docker-Livy](https://github.com/Wittline/docker-livy) and [Quick Start With Apache Livy](https://dzone.com/articles/quick-start-with-apache-livy)**
Create a Livy Session
```
curl -X POST --data '{"kind": "pyspark"}' -H "Content-Type: application/json" localhost:8998/sessions
```
Execute a PySpark code
```
curl localhost:8998/sessions/0/statements -X POST -H 'Content-Type: application/json' -d'{"code":"sc.parallelize([1, 2, 3, 4, 5]).count()"}' 
```
Check the statement
```
curl localhost:8998/sessions/0/statements/0
```
Close the session
```
curl localhost:8998/sessions/0 -X DELETE 
```