FROM bitnami/spark:3.5.4
USER root
RUN install_packages curl
USER 1001
RUN rm -r /opt/bitnami/spark/jars && \
    curl --location https://dlcdn.apache.org/spark/spark-3.5.4/spark-3.5.4-bin-hadoop3.tgz | \
    tar --extract --gzip --strip=1 --directory /opt/bitnami/spark/ spark-3.5.4-bin-hadoop3/jars/