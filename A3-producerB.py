#!/usr/bin/python

from pykafka import KafkaClient # start with pip install pykafka

import time


# KAFKA CLIENT , TOPIC , PRODUCER
client = KafkaClient(hosts='127.0.0.1:9092')
topic = client.topics['A3-homework']
producer = topic.get_sync_producer()

# SEND TEXT
#producer.produce('my text, from a python script'.encode('ascii'))
#time.sleep(1)
#producer.produce('something new, something blue'.encode('utf-8'))
# how to send an integer??
#producer.produce('345'.encode('utf-8'))

# send integers
i = 1
while True:
	producer.produce(str(i).encode('utf-8'))
	i+= 2
	time.sleep(2)
