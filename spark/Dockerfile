FROM bitnami/spark:3.0.0
USER root
RUN install_packages curl python

# Install Python Dependencies
COPY requirements.txt /opt/bitnami/   
RUN pip install -r /opt/bitnami/requirements.txt

USER 1001

#RUN rm -r /opt/bitnami/spark/jars && \
    #curl --location https://dlcdn.apache.org/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.tgz | \
    #tar --extract --gzip --strip=1 --directory /opt/bitnami/spark/ spark-3.0.0-bin-hadoop3/jars/