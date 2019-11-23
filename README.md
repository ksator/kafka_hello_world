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
  
# Instructions

## Requirements

### Requirements to use the file [docker-compose.yml](docker-compose.yml)  

The file [docker-compose.yml](docker-compose.yml) uses the Docker images [wurstmeister/zookeeper](https://hub.docker.com/r/wurstmeister/zookeeper) and [wurstmeister/kafka](https://hub.docker.com/r/wurstmeister/kafka) 

Install Docker and Install Docker-compose  

### Requirements to use these Python files [consumer.py](consumer.py) and [producer.py](producer.py)

On Ubuntu, run this command 
```
$ pip install kafka-python  
```

### Requirements to use the tool kafkacat  

On Ubuntu, run this command 
```
$ apt-get install kafkacat
```

or install Docker and use the docker image [edenhill/kafkacat](https://hub.docker.com/r/edenhill/kafkacat/)  

## Deploy a Kafka broker

Edit the file [docker-compose.yml](docker-compose.yml) and update `KAFKA_ADVERTISED_HOST_NAME` with your host IP

Run this command
```
$ docker-compose -f docker-compose.yml up -d
```
Verify
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

## 

## to stop services 

### To stop services without removing containers
```
jcluser@ubuntu:~$ docker-compose stop
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

### to stop services and remove containers
```
jcluser@ubuntu:~$ docker-compose down
Stopping kafka     ... done
Stopping zookeeper ... done
Removing kafka     ... done
Removing zookeeper ... done
Removing network jcluser_default
```
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
```
$ docker ps -a
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS                        PORTS               NAMES
```
