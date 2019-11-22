# Requirements

## Requirements to use the file [docker-compose.yml](docker-compose.yml)  

The file [docker-compose.yml](docker-compose.yml) uses Docker images: 
- [wurstmeister/zookeeper](https://hub.docker.com/r/wurstmeister/zookeeper) 
- [wurstmeister/kafka](https://hub.docker.com/r/wurstmeister/kafka) 

### Install Docker

This is not covered in this repo  

### Install Docker-compose  

This is not covered in this repo  

## Requirements to use the file [consumer.py](consumer.py) and [producer.py](producer.py)

Run this command on Ubuntu 

```
pip install kafka-python  
```

## Requirements to use kafkacat  

Run this command on Ubuntu

```
apt-get install kafkacat
```

or install Docker and use the docker image [edenhill/kafkacat](https://hub.docker.com/r/edenhill/kafkacat/)  


