# About this repo 

Kakfa hello-world. 

This repo provides instructions to: 
- Deploy a Kakfa broker
- Use the command line tool Kafkacat: 
  - to publish messages to Kafka
  - to subscribe to topics and receive messages from Kafka
- Use python: 
  - to publish messages to the broker
  - to subscribe to topics and receive messages from Kafka
  
# Deploy a Kafka broker

The file [docker-compose.yml](docker-compose.yml) uses the Docker images [wurstmeister/zookeeper](https://hub.docker.com/r/wurstmeister/zookeeper) and [wurstmeister/kafka](https://hub.docker.com/r/wurstmeister/kafka) 

Install Docker and Docker-compose  

Edit the file [docker-compose.yml](docker-compose.yml) and update `KAFKA_ADVERTISED_HOST_NAME` with your host IP

Run this command to create and start the containers
```
$ docker-compose -f docker-compose.yml up -d
```

Run these commands to verify
```
$ docker images | grep wurstmeister
wurstmeister/kafka       latest              988f4a6ca13c        4 months ago        421MB
wurstmeister/zookeeper   latest              3f43f72cb283        10 months ago       510MB
```
```
$ docker ps
CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS              PORTS                                                NAMES
45b13d484728        wurstmeister/kafka       "start-kafka.sh"         9 hours ago         Up 9 hours          0.0.0.0:9092->9092/tcp                               kafka
0957d9af0d62        wurstmeister/zookeeper   "/bin/sh -c '/usr/sb…"   9 hours ago         Up 9 hours          22/tcp, 2888/tcp, 3888/tcp, 0.0.0.0:2181->2181/tcp   zookeeper
```
```
$ nc -vz 100.123.35.0 9092
Connection to 100.123.35.0 9092 port [tcp/*] succeeded!
```
# Kafkacat command line tool 

On Ubuntu, run this command to install kafkacat
```
$ apt-get install kafkacat
```

Alternatively, install Docker and use the Docker image [edenhill/kafkacat](https://hub.docker.com/r/edenhill/kafkacat/)  

In producer mode, Kafkacat reads messages from stdin, and sends them to the broker.  
Using the below command, Kafkacat is used in producer mode, the broker is 100.123.35.0:9092, the topic is Topic1.  
```
$ kafkacat -P -b 100.123.35.0:9092 -t Topic1
first message
second message
third message
```

In consumer mode, Kafkacat gets messages from the broker and writes messages to stdout.  
Using the below command, Kafkacat is used in consumer mode, the broker is 100.123.35.0:9092, the topic is Topic1.  
```
$ kafkacat -C -b 100.123.35.0:9092 -t Topic1
first message
second message
third message
```
Using the below command, Kafkacat consumes 2 messages and exit
```
$ kafkacat -C -b 100.123.35.0 -t Topic1 -c 2 -e
first message
second message
$ 
```
Using the below command, Kafkacat consumes the last 2 messages and exit
```
$ kafkacat -C -b 100.123.35.0:9092 -t Topic1 -o -2 -e
second message
third message
% Reached end of topic Topic1 [0] at offset 3: exiting
$ 
```

# Python

## Requirements to use the Python files [consumer.py](consumer.py) and [producer.py](producer.py)

On Ubuntu, run this command 
```
$ pip install kafka-python  
```


# Stop services 

To stop services without removing containers, run this command: 
```
$ docker-compose stop
Stopping kafka     ... done
Stopping zookeeper ... done
```
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
```
$ docker ps -a
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS                        PORTS               NAMES
45b13d484728        wurstmeister/kafka        "start-kafka.sh"         9 hours ago         Exited (143) 36 seconds ago                       kafka
0957d9af0d62        wurstmeister/zookeeper    "/bin/sh -c '/usr/sb…"   9 hours ago         Exited (137) 29 seconds ago                       zookeeper
e0
```

To stop services and remove containers, run this command: 
```
$ docker-compose down
Stopping kafka     ... done
Stopping zookeeper ... done
Removing kafka     ... done
Removing zookeeper ... done
```
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
```
$ docker ps -a
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS                        PORTS               NAMES
```
