# Requirements

### Requirements to use the file [docker-compose.yml](docker-compose.yml)  

The file [docker-compose.yml](docker-compose.yml) uses the Docker images [wurstmeister/zookeeper](https://hub.docker.com/r/wurstmeister/zookeeper) and [wurstmeister/kafka](https://hub.docker.com/r/wurstmeister/kafka) 

Install Docker and Install Docker-compose  

### Requirements to use the file [consumer.py](consumer.py) and [producer.py](producer.py)

On Ubuntu, run this command 
```
pip install kafka-python  
```

### Requirements to use kafkacat  

On Ubuntu, run this command 
```
apt-get install kafkacat
```

or install Docker and use the docker image [edenhill/kafkacat](https://hub.docker.com/r/edenhill/kafkacat/)  


