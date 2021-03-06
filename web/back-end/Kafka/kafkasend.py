from kafka import KafkaProducer
from kafka.errors import KafkaError
from pickle import dumps
import address

producer = KafkaProducer(bootstrap_servers=[address_1])

# create data
data = ["hello"]

# Asynchronous by default
future = producer.send('python-test', dumps(data))

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
