from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.errors import KafkaError
from pickle import loads
from pickle import dumps
from database import get_similar, get_best, get_info
import operator
address_1 = <Kafka Address>

consumer = KafkaConsumer('id',
                         bootstrap_servers=[address_1],
                         auto_offset_reset='earlist',  # initilaize offset 'earlist' means from 0, 'latest' from oldest
                         group_id='0',  # different consumer needs different group_id
                         value_deserializer=lambda x: loads(x)
                         )

producer = KafkaProducer(bootstrap_servers=[address_1])

def similar_user_recs(user):
    sim_user_list = get_similar(user)
    if not sim_user_list:
        return ('No data available on user {}'.format(user))
    best = []
    most_common = {}
    for i in sim_user_list:
        best.append(get_best(i))  #give user id, return a list of tv with max score
    for i in range(len(best)):
        for j in best[i]:
            if j in most_common:
                most_common[j] += 1
            else:
                most_common[j] = 1
    sorted_list = sorted(most_common.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_list[:5], [sorted_list[i][0] for i in range(5)]




while True:
    msg = consumer.poll(timeout_ms = 10000, max_records = 1)
    if not msg:
        continue
    print('receive', msg)
    value = list(msg.values())[0]
    user_id = value[0].value
    _,data = similar_user_recs(user_id)
    name = []
    for id in data:
        name.append(get_info('item','name',id))
    future = producer.send('cf_item', dumps(name))
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        log.exception()
        pass
    print ('predict sent!', record_metadata.offset)
