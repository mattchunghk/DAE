from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os

load_dotenv()

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

# df_to_parquet = spark.read.format("mongo").option(
#     "uri", "mongodb://172.1.0.10/openrice.restaurants").load()

# df_to_parquet.write.parquet('s3a://openrice/restaurants.parquet')

# df = spark.read.parquet('s3a://openrice/restaurants.parquet')
# df.write.json("./openrice.json")
# df.show()
