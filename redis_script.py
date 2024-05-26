import sys
from Config.config import *
from data_handler import *
from excel_reader import *

p = get_kafka_producer(KAFKA_BROKER)
r = get_redis_connection()
df_governorates, df_vehicles, df_travels, df_all_government = read_excel_sheets(
    EXCEL_FILE
)
# Read data from stdin (FlowFile content)
for line in sys.stdin:
    try:
        # Get Key from flow file
        word = line.strip()

        id = word.split(",")[0].split(":")[1]
        start_Gate = word.split(",")[1].split(":")[1]
        end_Gate = word.split(",")[2].split(":")[1]
        distance = word.split(",")[3].split(":")[1]
        start_date = word.split(",")[4].split(": ")[1]

        To_Nifi(r, df_governorates, id, start_Gate, end_Gate, distance, start_date)

    except Exception as e:
        print("Error:", e)
