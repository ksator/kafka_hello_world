from kafka import KafkaProducer

topic = "topic1" 
key="key1"
value="value1"
kafka = '100.123.35.0:9092'

producer = KafkaProducer(bootstrap_servers=[kafka], security_protocol="PLAINTEXT", retries=2, compression_type=None, request_timeout_ms=10000)
#producer.bootstrap_connected()
message = producer.send(topic, key = key, value = value)
producer.flush()



