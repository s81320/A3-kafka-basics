# A3 streaming with kafka

I got kafka (and zookeeper included) as described here 
http://kafka.apache.org/quickstart
It worked well (on my mac) with the cli , messages successfully send and received / produced and consumed

Tried to work with kafka-python but ran into problems:
Like it did not work with python 3.7 - I switched to python 3.6
Still I could not resolve this error: kafka.errors.NoBrokersAvailable: NoBrokersAvailable

## pykafka
This library instantly worked well. The code is basic.

### to dos for the homework

* The consumer should get (and print) the producerID for each received message.

* Since in this example the messages are numbers, they should be sent as numbers (int) and not as strings. I think that would make sense.
