# A3 streaming with kafka
## messaging
I got kafka (and zookeeper included) as described here 
http://kafka.apache.org/quickstart
It worked well (on my mac) with the cli , messages successfully send and received / produced and consumed

Tried to work with the kafka-python library but ran into problems:
Like it did not work with python 3.7 - I switched to python 3.6
Still I could not resolve this error: kafka.errors.NoBrokersAvailable: NoBrokersAvailable
### pykafka
This library instantly worked well.
# streaming
Kafka messaging is for communication / data exchange in a distributed system. The more traditional approach ist to have nodes in a distributd system exchange data by using a database both / all parties write to and / or read from. When using messaging the "write to the database" becomes "publish a stream / topic (?)" and the read from a database" becomes "consume a stream".

Kafka streaming is to do stuff with the data on a node in the distributed system, that was consumed from a stream. Or to do do stuff before publishing to a stream. The "do stuff" can be: 
* (low level) doing computations, transforming the data stream (aggregation, enrichment, computations over windows)
* (high level) build applications and microservices.

Kafka Streams is a Java library. When you want to do kafka streaming in Python use Spark.
# alpha go movie
YES! watched it - liked it!
