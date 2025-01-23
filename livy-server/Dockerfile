#https://github.com/apache/incubator-livy?tab=readme-ov-file#building-livy
#FROM docker.io/bitnami/spark:2.4.5
#Use the spark image 3.5.4 already buily with the original hadoop3 jars 
FROM spark-livy-spark-master

USER root
ENV LIVY_HOME /opt/bitnami/livy
WORKDIR /opt/bitnami/

RUN install_packages unzip curl \
    && curl "https://downloads.apache.org/incubator/livy/0.8.0-incubating/apache-livy-0.8.0-incubating_2.12-bin.zip" -O \
    && unzip "apache-livy-0.8.0-incubating_2.12-bin" \
    && rm -rf "apache-livy-0.8.0-incubating_2.12-bin.zip" \
    && mv "apache-livy-0.8.0-incubating_2.12-bin" $LIVY_HOME \
    && mkdir $LIVY_HOME/logs \
    && chown -R 1001:1001 $LIVY_HOME

USER 1001
