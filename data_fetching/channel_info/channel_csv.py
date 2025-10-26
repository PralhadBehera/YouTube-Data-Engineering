from channel_fetch import get_channel_info
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

# Create Spark session with log4j config
spark = SparkSession.builder \
    .appName("channel_csv") \
    .config("spark.driver.extraJavaOptions",
            "-Dlog4j.configuration=file:///C:/Users/druva/Downloads/YouTube-Data-Engineering/data_fetching/channel_info/log4j.properties") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")
print("Spark version:", spark.version)

# Fetch channel info
info = get_channel_info()

# Define schema
schema = StructType([
    StructField("title", StringType(), True),
    StructField("channel_id", StringType(), True),
    StructField("view_count", StringType(), True),
    StructField("subscriber_count", StringType(), True),
    StructField("video_count", StringType(), True),
    StructField("uploads_playlist_id", StringType(), True)
])

# Create DataFrame
df = spark.createDataFrame([info], schema)

# Save as single CSV
df.coalesce(1).write.format("csv").mode("overwrite").option("header", "true").save("channel_info.csv")

# Show DataFrame
df.show()
