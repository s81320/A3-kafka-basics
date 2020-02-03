from pykafka import KafkaClient # start with pip install pykafka

# KAFKA CLIENT
client = KafkaClient(hosts='127.0.0.1:9092')

#KAFKA CONSUMER
topic = client.topics['A3-homework']
consumer = topic.get_simple_consumer()

# DO SOMETHING
for c in consumer:
	print(c.offset , ' : ' , c.value)
