from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql import functions as F
from pyspark.sql.functions import from_json, col, lit, split, when, coalesce, window
from Config.config import *
from Config.Logger import *

# ** ----------------- Create SparkSession -----------------
spark = (
    SparkSession.builder.appName("Spark")
    .config("spark.streaming.stopGracefullyOnShutdown", True)
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0")
    .config("spark.jars", MYSQL_CONNECTOR_PATH)
    .config("spark.driver.extraClassPath", MYSQL_CONNECTOR_PATH)
    .config("spark.sql.shuffle.partitions", 8)
    .master("local[*]")
    .getOrCreate()
)


# ** ----------------- Read from MYSQL -----------------
def read_from_mysql(table_name):
    df = (
        spark.read.format("jdbc")
        .option("url", MYSQL_JDBC_URL)
        .option("dbtable", table_name)
        .option("user", MYSQL_USER)
        .option("password", MYSQL_PASSWORD)
        .load()
    ).cache()

    return df


violations_df = read_from_mysql(VIOLATIONS_TABLE)
violations_df.show()

# ** ----------------- Read from KAFKA -----------------
schema = StructType(
    [
        StructField("ID", StringType(), True),
        StructField("Start Gate", StringType(), True),
        StructField("End Gate", StringType(), True),
        StructField("Start Date", StringType(), True),
        StructField("End Date", StringType(), True),
    ]
)

violations_stream_df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", KAFKA_BROKER)
    .option("subscribe", VIOLATIONS_TOPIC)
    .option("startingOffsets", "earliest")
    .load()
    .selectExpr("CAST(value AS STRING) ", "CAST(timestamp AS STRING)")
    .select(from_json("value", schema).alias("data"), "timestamp")
    .select("data.*", "timestamp")
)

# # ** ------------------------------ Count the number of Routes ---------------------------------
# routes_stream_df = (
#     violations_stream_df.groupBy(
#         window(violations_stream_df.timestamp, "1 hours"),
#         "Start Gate",
#         "End Gate",
#     )
#     .count()
#     .orderBy(col("count").desc())
# )

# # # Start the query
# query1 = (
#     routes_stream_df.writeStream.outputMode("Complete")
#     .format("console")
#     .option("truncate", "false")
#     .start()
#     .awaitTermination()
# )

# # ----------------- Count the number of violations for each vehicle type -----------------
# vehicle_stream_df = (
#     violations_stream_df.groupBy(
#         window(violations_stream_df.timestamp, "1 days"),
#         split(col("ID"), "_")[1].alias("Vehicle_Type"),
#     )
#     .count()
#     .orderBy(col("count").desc())
# )


# ** ----------------- Second Query -----------------
# query2 = (
#     vehicle_stream_df.writeStream.outputMode("complete")
#     .format("console")
#     .option("truncate", "false")
#     .start()
#     .awaitTermination()
# )
