from kafka import KafkaConsumer
from dotenv import load_dotenv
import json
from google.cloud import bigquery

load_dotenv()

client = bigquery.Client()

consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(
                             m.decode('utf-8')))
#  auto_offset_reset='earliest'

midland_data = client.get_table('dea-proj.dea_proj_data.midland_v5')

consumer.subscribe(topics='midland_v5')


info_ids = []


for message in consumer:
    if message.value["_id"] not in info_ids:
        # print(message.value)
        result = client.insert_rows_json(midland_data, [message.value])
        info_ids.append(message.value["_id"])
