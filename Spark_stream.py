from datetime import datetime
from pdb import run
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql import functions as F
from pyspark.sql.functions import from_json, col, lit, split, when, coalesce, window
from Config.config import *
from Config.Logger import *


checkpoint_location = "output/checkpoints"


def run_spark_job():
    spark = (
        SparkSession.builder.appName("Spark")
        .config("spark.streaming.stopGracefullyOnShutdown", True)
        .config(
            "spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0"
        )
        .config("spark.jars", MYSQL_CONNECTOR_PATH)
        .config("spark.driver.extraClassPath", MYSQL_CONNECTOR_PATH)
        .config("spark.sql.shuffle.partitions", 8)
        .master("local[*]")
        .getOrCreate()
    )

    spark.conf.set("spark.sql.streaming.checkpointLocation", checkpoint_location)

    # Read from MySQL
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

    # Read data from MySQL
    # violations_df = read_from_mysql(VIOLATIONS_TABLE)
    # travels_df = read_from_mysql(TRAVELS_TABLE)

    # violations_df.show()

    # Read from Kafka
    schema = StructType(
        [
            StructField("ID", StringType(), True),
            StructField("Start Gate", StringType(), True),
            StructField("End Gate", StringType(), True),
            StructField("Start Date", StringType(), True),
            StructField("End Date", StringType(), True),
        ]
    )

    delays_schema = StructType(
        [
            StructField("ID", StringType(), True),
            StructField("Start Gate", StringType(), True),
            StructField("End Gate", StringType(), True),
            StructField("Start Date", StringType(), True),
            StructField("End Date", StringType(), True),
        ]
    )

    # Read data from Kafka
    violations_stream_df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BROKER)
        .option("subscribe", VIOLATIONS_TOPIC)
        .option("failOnDataLoss", False)
        .option("startingOffsets", "earliest")
        .load()
        .selectExpr("CAST(value AS STRING) ", "CAST(timestamp AS STRING)")
        .select(from_json("value", schema).alias("data"), "timestamp")
        .select("data.*", "timestamp")
    )

    query1 = (
        violations_stream_df.writeStream.format("json")
        .outputMode("append")
        .option("path", "output/violations")
        .option("checkpointLocation", checkpoint_location)
        .option("failOnDataLoss", "false")
        .start()
    )
    travels_stream_df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BROKER)
        .option("subscribe", KAFKA_TOPIC)
        .option("failOnDataLoss", False)
        .option("startingOffsets", "earliest")
        .load()
        .selectExpr("CAST(value AS STRING) ", "CAST(timestamp AS STRING)")
        .select(from_json("value", schema).alias("data"), "timestamp")
        .select("data.*", "timestamp")
    )

    query2 = (
        travels_stream_df.writeStream.format("json")
        .outputMode("append")
        .option("path", "output/travels")
        .option("checkpointLocation", "output/checkpoints/travels")
        .option("failOnDataLoss", "false")
        .start()
    )

    delays_stream_df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BROKER)
        .option("subscribe", DELAY_TOPIC)
        .option("failOnDataLoss", False)
        .option("startingOffsets", "earliest")
        .load()
        .selectExpr("CAST(value AS STRING) ", "CAST(timestamp AS STRING)")
        .select(from_json("value", schema).alias("data"), "timestamp")
        .select("data.*", "timestamp")
    )

    query3 = (
        delays_stream_df.writeStream.format("json")
        .outputMode("append")
        .option("path", "output/delays")
        .option("checkpointLocation", "output/checkpoints/delays")
        .option("failOnDataLoss", "false")
        .start()
    )

    query1.awaitTermination()
    query2.awaitTermination()
    query3.awaitTermination()

    spark.stop()


run_spark_job()
