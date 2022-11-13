import pandas as pd
import json
import http.client
from pyspark.sql import SparkSession
from dotenv import load_dotenv
from google.cloud import bigquery
import os

load_dotenv()

client = bigquery.Client()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')


packages = [
    "com.amazonaws:aws-java-sdk-s3:1.12.95",
    "org.apache.hadoop:hadoop-aws:3.2.0",
    "org.apache.spark:spark-avro_2.12:3.3.0",
    "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1"
]

spark = SparkSession.builder.appName("Transform Recent change stream")\
    .master('spark://172.1.0.2:7077')\
    .config("spark.jars.packages", ",".join(packages))\
    .config("spark.hadoop.fs.s3a.access.key", AWS_ACCESS_KEY)\
    .config("spark.hadoop.fs.s3a.secret.key", AWS_SECRET_KEY)\
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")\
    .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')\
    .config("spark.hadoop.fs.s3a.multipart.size", 104857600)\
    .config("com.amazonaws.services.s3a.enableV4", "true")\
    .config("spark.hadoop.fs.s3a.path.style.access", "false")\
    .getOrCreate()


# info_arr = []
# for info in data['stocks']:
#     if int(info['rent']) > 0:
#         info_dict = {
#             '_id': info['gstock_id'],
#             'region': info['region'],
#             'rent': info['rent'],
#             'area': info['area'],
#             'lat': info['lat'],
#             'lng': info['lng'],
#             'address': info['eng_addr_name'],
#             'dist': info['dist_eng_name'],
#         }
#         info_arr.append(info_dict)
# db.midland.insert_one(info_dict)

# df_to_parquet = spark.read.format("mongo").option(
#     "uri", "mongodb://172.1.0.10/estate.midland").load()

# df_to_parquet.show()

# df_to_parquet.write.parquet('s3a://openrice/midland.parquet')
# df = spark.read.parquet('s3a://openrice/midland.parquet')
# df = spark.read.parquet('s3a://openrice/restaurants.parquet')
# print(df.toJSON())
# df_to_parquet.show()

df = spark.read.parquet('s3a://openrice/midland.parquet').toJSON().collect()
df = json.dumps(df)
midland2_data = client.get_table('dea-proj.dea_proj_data.midland2')
for data in df:
    result = client.insert_rows_json(midland2_data, [data])
# midland2_data = client.get_table('dea-proj.dea_proj_data.midland2')
# result = client.insert_rows_json(midland2_data, df)
# df.show()


# print(pd.DataFrame(info_arr))
