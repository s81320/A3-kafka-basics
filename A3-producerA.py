#!/usr/bin/python

from pykafka import KafkaClient # start with pip install pykafka

import time


# KAFKA CLIENT , TOPIC , PRODUCER
client = KafkaClient(hosts='127.0.0.1:9092')
topic = client.topics['A3-homework']
producer = topic.get_sync_producer()

# send integers
i = 2
while True:
	producer.produce(str(i).encode('utf-8'))
	i += 2
	time.sleep(1)

