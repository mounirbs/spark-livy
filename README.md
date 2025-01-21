# spark-livy
Spark Livy How-To

## Docker Compose
**Start docker compose**
```docker-compose up --scale spark-worker=1```

## Spark Submit
**Submit a Spark job**
```
spark-submit --master spark://spark:7077 /python/test_spark.py
spark-submit --master spark://spark:7077 /python/test_pandas.py
```
## Spark REST API
** Submit a job to the Spark Cluster***
```
curl -XPOST http://localhost:6066/v1/submissions/create --header "Content-Type:application/json;charset=UTF-8" --data '{"appResource": "","sparkProperties": {"spark.master": "spark://spark:7077","spark.app.name": "TestFromRestCall"},"clientSparkVersion": "","mainClass": "org.apache.spark.deploy.SparkSubmit","environmentVariables": { },"action": "CreateSubmissionRequest","appArgs": [ "/python/test_spark.py" ]}'
```
** Get the status of a Spark Job**
```
curl -XGET http://localhost:6066/v1/submissions/status/driver-20250119021438-0010
```
## Apache Livy
**Test**
```
curl -X POST http://<container-ip>:8998/sessions -d '{"kind": "spark", "conf": {"spark.master": "spark://spark:7077"}}'
```

