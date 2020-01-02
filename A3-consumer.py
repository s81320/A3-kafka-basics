from pykafka import KafkaClient # start with pip install pykafka

# KAFKA CLIENT
client = KafkaClient(hosts='127.0.0.1:9092')

#KAFKA CONSUMER
topic = client.topics['A3-homework']
consumer = topic.get_simple_consumer()

# DO SOMETHING
for c in consumer:
	print(c.offset , ' : ' , c.value)

#'compression_type', 'decode', 'delivery_report_q', 'offset', 'pack_into', 'partition', 
# 'partition_id', 'partition_key', 'produce_attempt', 'protocol_version', 'set_timestamp', 
# 'timestamp', 'timestamp_dt', 'value'	

# c is a pykafka.protocol.message.Message object
