import threading , logging, time
from kafka import KafkaProducer

class Producer(threading.Thread):
	daemon = True

	def run(self):
		producer = KafkaProducer(bootstrap_server '...9092')

		while True:

			producer.send('topic-name' , 'message')
			time.sleep(1)
def main():
	tasks = [Producer()]

	for t in tasks:
		t.start()

	time.sleep(10)