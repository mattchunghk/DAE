from pyspark.sql import SparkSession

packages = [
    "org.apache.hadoop:hadoop-aws:3.2.0",
    "org.apache.spark:spark-avro_2.12:2.4.4",
    "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1"
]

spark = SparkSession.builder.appName("Transform Google Trend stream")\
    .master('spark://172.1.0.2:7077')\
    .config("spark.jars.packages", ",".join(packages))\
    .getOrCreate()

df = spark.read.format("mongo").option(
    "uri", "mongodb://172.1.0.10/google_trends.openrice").load()
# df.filter(df.type =="details_href").show()
df.show()
