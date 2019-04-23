from kafka import KafkaConsumer
from pickle import loads
from kafka.structs import TopicPartition, OffsetAndMetadata
import address

# create consumber object
# ! these parameters needs to be monified if you want to change mode
# ! https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
consumer = KafkaConsumer(
    'python-test',
     bootstrap_servers=[address_1],
     auto_offset_reset='earliest', # initilaize offset 'earlist' means from 0, 'latest' from oldest
     group_id = '0', # different consumer needs different group_id
     value_deserializer=lambda x: loads(x))

#consumer.seek(TopicPartition(topic='python-test', partition=0), 1)
# define topic partition
tp = TopicPartition(topic='python-test', partition=0)

# Approach 1: poll + seek control the offset manually
for i in range(3):
    # receive 1 record for 1 time, return dict
    msg = consumer.poll(timeout_ms=1000, max_records = 1)

    keys = list(msg.keys())
    value = msg[keys[0]]
    data = value[0]

    print(data.value)

    # receive the next position offset
    end = consumer.position(TopicPartition(topic='python-test', partition=0))

    # control the next offset
    consumer.seek(tp, end)

# Approach 2, automatically control the offset
while True
    msg = consumer.poll(timeout_ms=1000, max_records = 1)
