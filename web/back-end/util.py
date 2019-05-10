from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from kafka.structs import TopicPartition, OffsetAndMetadata
from pickle import dumps, loads

kafka_address = '34.73.198.4:9092'
producer = KafkaProducer(bootstrap_servers=[kafka_address])

def kafkasend(topic, msg):
    '''
    @ param: topic: str, kafkatopic
    @ param: msg: any datastructure
    @ function: kafka send, print offset ater send
    '''
    # Asynchronous by default
    future = producer.send(topic, dumps(msg))
    # Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        log.exception()
        pass

    # Successful result returns assigned partition and offset
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)


# Receiver
# create consumber object
# ! these parameters needs to be monified if you want to change mode
# ! https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
consumer = None
def setConsumer(topic):
    consumer = KafkaConsumer(
        topic,
         bootstrap_servers=[kafka_address],
         auto_offset_reset='earliest', # initilaize offset 'earlist' means from 0, 'latest' from oldest
         group_id = '0', # different consumer needs different group_id
         value_deserializer=lambda x: loads(x))
    print("consumer's topic is set as: ", topic)
    return consumer

def kafkareceive(consumer):
    msg = consumer.poll(timeout_ms=1000, max_records = 1)
    if len(msg) == 0:
        return None
    else:
        # unpack data structure
        data =list(msg.values())[0][0].value
        return data

def buildhtml(data):
    #function: build html format display code
    names = ""
    # Construct Items list
    for i in range(len(data)):
        strbase = "<div onclick = 'get(this.id)' id = '%s'> %s </div>"%(data[i], data[i])
        names = names + '<tr>' + strbase +' </tr>'
    return names
