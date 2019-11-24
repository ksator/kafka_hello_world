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
# Kafkacat 

Kafkacat is a command line tool to produce and consume messages  

## Installation 

On Ubuntu, run this command to install kafkacat
```
$ apt-get install kafkacat
```

Alternatively, install Docker and use the Docker image [edenhill/kafkacat](https://hub.docker.com/r/edenhill/kafkacat/)  

## Produce and consume messages 

In producer mode, Kafkacat reads messages from stdin, and sends them to the broker.  
In consumer mode, Kafkacat gets messages from the broker and writes messages to stdout.  

Using the below command, Kafkacat is used in producer mode, the broker is 100.123.35.0:9092, the topic is Topic1.  
```
$ kafkacat -P -b 100.123.35.0:9092 -t Topic1
first message
second message
third message
```
Using the below command, Kafkacat is used in consumer mode
```
$ kafkacat -C -b 100.123.35.0:9092 -t Topic1
first message
second message
third message
```

## Limit the number of messages to consume 

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
## Change the delimiter 

### On the consumer 

Using the below command, Kafkacat consumes the messages, changes the delimiter ( default is `\n`) that separates messages on stdout, and exit 
```
$ kafkacat -C -b 100.123.35.0:9092 -t Topic1 -D "\n####\n" -e
first message
####
second message
####
third message
####
% Reached end of topic Topic1 [0] at offset 3: exiting
$
```
### On the producer 

You can also change on the producer the delimiter (default is `\n`) that splits input (stdin) into messages.  
Example with a new topic  
```
$ kafkacat -P -b 100.123.35.0:9092 -t Topic2 -D "##"
message 1##message 2##message 3##
```
```
$ kafkacat -C -b 100.123.35.0:9092 -t Topic2 -e
message 1
message 2
message 3
% Reached end of topic Topic2 [0] at offset 3: exiting
```
## Produce messages from files 

You can also produce messages from files. Kafkacat will read files.  
The entire file content will be sent as one single message. The producer will exit after sending the messages.  

```
$ more message1
The content of the file message1 is sent as one single message.
$ more message2
The content of the file message2
is sent
as one single message.
$ kafkacat -P -b 100.123.35.0:9092 -t Topic3 message1 message2
$
```
```
$ kafkacat -C -b 100.123.35.0:9092 -t Topic3 -e
The content of the file message1 is sent as one single message.

The content of the file message2
is sent
as one single message.

% Reached end of topic Topic3 [0] at offset 2: exiting
$ 
```
## Messages with a key

In the below example, the producer uses the delimiter is `:` to split keys and messages. 

```
$ kafkacat -P -b 100.123.35.0:9092 -t Topic4 -K:
key1:message1
Key2:message2
Key3:message3
```
In the below example, the consumer uses the delimiter is `:::` to split keys and messages. 

```
$ kafkacat -C -b 100.123.35.0:9092 -t Topic4 -K: -e
key1:::message1
Key2:::message2
Key3:::message3
$ 
```
In the below example, the consumer gets the messages without the keys

```
$ kafkacat -C -b 100.123.35.0:9092 -t Topic4 -e
message1
message2
message3
$
```
In the below example, the consumer changes the output format.  
It uses the option `%k` to get the messages key and `%s` to get the messages payload
```
$ kafkacat -C -b 100.123.35.0:9092 -t Topic4 -f "\nKey %k\nValue %s\n" -e

Key: key1
Value: message1

Key: Key2
Value: message2

Key: Key3
Value: message3
% Reached end of topic Topic5 [0] at offset 3: exiting
$
```

## List metadata from topics from a broker

```
$ kafkacat -L -b 100.123.35.0:9092
Metadata for all topics (from broker -1: 100.123.35.0:9092/bootstrap):
 1 brokers:
  broker 1001 at 100.123.35.0:9092
 6 topics:
  topic "Topic4" with 1 partitions:
    partition 0, leader 1001, replicas: 1001, isrs: 1001
  topic "Topic1" with 1 partitions:
    partition 0, leader 1001, replicas: 1001, isrs: 1001
  topic "Topic2" with 1 partitions:
    partition 0, leader 1001, replicas: 1001, isrs: 1001
  topic "Topic3" with 1 partitions:
    partition 0, leader 1001, replicas: 1001, isrs: 1001
```

## Using Docker 

Insteaf of installing kafkacat you can install Docker and use the Docker image [edenhill/kafkacat](https://hub.docker.com/r/edenhill/kafkacat/)  

```
$ docker run --rm -it edenhill/kafkacat:1.5.0 -C -b 100.123.35.0:9092 -t Topic1 -e
first message
second message
third message
% Reached end of topic Topic1 [0] at offset 3: exiting
$
```
```
$ docker images edenhill/kafkacat
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
edenhill/kafkacat   1.5.0               d3dc4f492999        2 months ago        22.4MB
```

# Python

## Requirements

On Ubuntu, run this command 
```
$ pip install kafka-python  
```
## Use Python to produce and consume messages  

### Produce a single message 

```
>>> from kafka import KafkaProducer
>>>
>>> topic = "topic6"
>>> key="key1"
>>> value="value1"
>>> kafka = '100.123.35.0:9092'
>>>
>>> producer = KafkaProducer(bootstrap_servers=[kafka], security_protocol="PLAINTEXT", retries=2, compression_type=None, request_timeout_ms=10000)
>>> producer.bootstrap_connected()
True
>>> message = producer.send(topic, key = key, value = value)
>>> producer.flush()
>>> exit()

```
### Consume messages
```
>>> from kafka import KafkaConsumer
>>>
>>> kafka = '100.123.35.0:9092'
>>> topic = "topic6"
>>>
>>> consumer1 = KafkaConsumer(topic, bootstrap_servers=kafka, security_protocol="PLAINTEXT", auto_offset_reset='earliest')
>>>
>>> consumer1.bootstrap_connected()
True
>>>
>>> consumer1.topics()
set([u'topic1', u'Topic2', u'topic3', u'topic4', u'topic6'])
>>>
>>> for message in consumer1:
...     print ("topic=%s offset=%d key=%s value=%s" % (message.topic, message.offset, message.key, message.value))
...
topic=topic6 offset=0 key=key1 value=value1

```
### Produce and consume messages 

use the Python files [consumer.py](consumer.py) and [producer.py](producer.py)

```
$ python producer.py
$ python consumer.py
topic=topic5 offset=0 key=key1 value=value1
topic=topic5 offset=1 key=key2 value=value2
```

# Stop services 

## stop services without removing containers

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

## stop services and remove containers
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
