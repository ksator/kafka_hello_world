from kafka import KafkaProducer

topic = "topic5" 
kafka = '100.123.35.0:9092'
messages = [{"key1":"value1"}, {"key2":"value2"}]

messages = [{"key":"key1", "value": "value1"}, {"key":"key2", "value": "value2"}]

producer = KafkaProducer(bootstrap_servers=[kafka], security_protocol="PLAINTEXT", retries=2, compression_type=None, request_timeout_ms=10000)
#producer.bootstrap_connected()

for item in messages: 
  message = producer.send(topic, key = item["key"], value = item["value"])

producer.flush()
