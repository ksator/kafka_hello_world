from kafka import KafkaConsumer

kafka = '100.123.35.0:9092'
topic = "topic5" 

# auto_offset_reset can be set to 'latest' or 'earliest'
consumer1 = KafkaConsumer(topic, bootstrap_servers=kafka, security_protocol="PLAINTEXT", auto_offset_reset='earliest')

# Return True if the client is connected to the kafka server 
# consumer1.bootstrap_connected()

# Get all topics the user is authorized to view. 
# consumer1.topics()

for message in consumer1:
    print ("topic=%s offset=%d key=%s value=%s" % (message.topic, message.offset, message.key, message.value))
