from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for i in range(1, 100):
    print(f"Sending:{i}")
    producer.send('my-topic', {"number": i})
    time.sleep(1)
