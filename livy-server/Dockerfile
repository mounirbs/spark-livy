#https://github.com/apache/incubator-livy?tab=readme-ov-file#building-livy
# Reuse the same image built for Spark Master/Worker
FROM spark-livy-spark-master
USER root
ENV LIVY_HOME /opt/livy
WORKDIR /opti/

RUN apt-get update && apt-get install -y unzip \
    && curl "https://downloads.apache.org/incubator/livy/0.8.0-incubating/apache-livy-0.8.0-incubating_2.12-bin.zip" -O \
    && unzip "apache-livy-0.8.0-incubating_2.12-bin" \
    && rm -rf "apache-livy-0.8.0-incubating_2.12-bin.zip" \
    && mv "apache-livy-0.8.0-incubating_2.12-bin" $LIVY_HOME \
    && mkdir $LIVY_HOME/logs \
    && chown -R 1001:1001 $LIVY_HOME

USER 1001
