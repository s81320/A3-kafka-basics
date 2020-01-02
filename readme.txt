****************** how i started and lost lots of time

created conda environment A3kafka with python 3.7
setup requirement.txt with the packages i need. defenitely python-kafka.

get kafka (and zookeeper included) as described here 
http://kafka.apache.org/quickstart
-> works well with the cli , messages successfully send and received / produced and consumed

to run everything in a docker container, follow https://www.youtube.com/watch?v=U5PshJKECe4 (i have not done that yet)

when running, first start zookeeper server , then kafka server.

check out https://kafka-python.readthedocs.io/en/master/usage.html# for example code for producer and consumer
-> KafkaProducer(bootstrap_servers=['localhost:9092']) does not work with python 3.7 - have to use python 3.6
-> python 3.6 produces error: kafka.errors.NoBrokersAvailable: NoBrokersAvailable

read about the kafka producer, with code examples and associated youtube video https://medium.com/@codeanddogs/kafka-producer-in-python-f481ae1e4c5d
another chapter and video about the consumer. Actually a whole application explained from scratch. Uses pykafka.


******************* this worked better for me (on Mac)

2.1.2020
Switch	to pykafka

******************** to dos for the homework

the consumer should get (and print) the producerID for each received message

as in this example the messages are numbers, they should be sent as numbers (int) and not as strings.