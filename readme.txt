****************** i am working on a mac.

get kafka (and zookeeper included) as described here 
http://kafka.apache.org/quickstart
-> works well (on mac) with the cli , messages successfully send and received / produced and consumed

I tried to work with kafka-python
https://kafka-python.readthedocs.io/en/master/usage.html# for example code for producer and consumer
but ran into troubles. Like it did not work with python 3.7 - you have to use python 3.6
Still could not resolve this
-> python 3.6 produces error: kafka.errors.NoBrokersAvailable: NoBrokersAvailable

pykafka worked better for me. 

******************** to dos for the homework

the consumer should get (and print) the producerID for each received message

as in this example the messages are numbers, they should be sent as numbers (int) and not as strings.
