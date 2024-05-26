from datetime import datetime
import warnings
import os

from kafka import KafkaProducer

from Config.config import EXCEL_FILE
from data_handler import (
    Calaulate_Lowest_Distance,
    calculate_ttl,
    get_redis_connection,
    insert_governorates_data,
    insert_vehicles_data,
)
from excel_reader import read_excel_sheets

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
warnings.filterwarnings("ignore", category=UserWarning, module="tensorflow")
warnings.filterwarnings("ignore", category=UserWarning, module="keras")
import cv2
import matplotlib as plt
import pytesseract
from PIL import Image
import sys
from vehicle_type import Get_vehicle_type

# Vehicels before Cropping
# -----------------------------
BEFORE_1 = "Egyptain Cars\\Before Cropping\\0022.jpg"
BEFORE_2 = "Egyptain Cars\\Before Cropping\\0026.jpg"
BEFORE_3 = "Egyptain Cars\\Before Cropping\\0033.jpg"
BEFORE_4 = "Egyptain Cars\\Before Cropping\\0035.jpg"
BEFORE_5 = "Egyptain Cars\\Before Cropping\\0037.jpg"
BEFORE_6 = "Egyptain Cars\\Before Cropping\\0055.jpg"
BEFORE_7 = "Egyptain Cars\\Before Cropping\\0058.jpg"
BEFORE_8 = "Egyptain Cars\\Before Cropping\\0067.jpg"
BEFORE_9 = "Egyptain Cars\\Before Cropping\\0082.jpg"
BEFORE_10 = "Egyptain Cars\\Before Cropping\\0095.jpg"
BEFORE_11 = "Egyptain Cars\\Before Cropping\\0608.jpg"
BEFORE_12 = "Egyptain Cars\\Before Cropping\\0609.jpg"
BEFORE_13 = "Egyptain Cars\\Before Cropping\\0718.jpg"
BEFORE_14 = "Egyptain Cars\\Before Cropping\\1800.jpg"

# Vehicels after Cropping
# -----------------------------
AFTER_1 = "Egyptain Cars\\After Cropping\\11.png"
AFTER_2 = "Egyptain Cars\\After Cropping\\12.png"
AFTER_3 = "Egyptain Cars\\After Cropping\\13.png"
AFTER_4 = "Egyptain Cars\\After Cropping\\9.png"
AFTER_5 = "Egyptain Cars\\After Cropping\\10.png"
AFTER_6 = "Egyptain Cars\\After Cropping\\3.png"
AFTER_7 = "Egyptain Cars\\After Cropping\\2.png"
AFTER_8 = "Egyptain Cars\\After Cropping\\4.png"
AFTER_9 = "Egyptain Cars\\After Cropping\\5.png"
AFTER_10 = "Egyptain Cars\\After Cropping\\6.png"
AFTER_11 = "Egyptain Cars\\After Cropping\\1.png"
AFTER_12 = "Egyptain Cars\\After Cropping\\7.png"
AFTER_13 = "Egyptain Cars\\After Cropping\\8.png"
AFTER_14 = "Egyptain Cars\\After Cropping\\14.png"

vehicles = {
    BEFORE_1: AFTER_1,
    BEFORE_2: AFTER_2,
    BEFORE_3: AFTER_3,
    BEFORE_4: AFTER_4,
    BEFORE_5: AFTER_5,
    BEFORE_6: AFTER_6,
    BEFORE_7: AFTER_7,
    BEFORE_8: AFTER_8,
    BEFORE_9: AFTER_9,
    BEFORE_10: AFTER_10,
    BEFORE_11: AFTER_11,
    BEFORE_12: AFTER_12,
    BEFORE_13: AFTER_13,
    BEFORE_14: AFTER_14,
}


def Get_Vehicle_ID(vehicle):
    image = cv2.imread(vehicles[vehicle])

    # Path to the Tesseract executable (if not in your PATH)
    pytesseract.pytesseract.tesseract_cmd = r"D:\\Tesseract-OCR\\tesseract.exe"

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image, lang="ara_number")

    # Get vehicle types
    vehicle_type = Get_vehicle_type(vehicle)

    vehicle_ID = f"{text.strip()}_{vehicle_type}"

    return vehicle_ID


# x = Get_Vehicle_ID('Egyptain Cars\\Before Cropping\\0022.jpg')
# print(x)
# print(vehicles.keys())
# r = get_redis_connection()
# df_governorates, df_vehicles, df_travels, df_all_government = read_excel_sheets(
#     EXCEL_FILE
# )
# governorates_dict = insert_governorates_data(r, df_governorates)
# # insert_vehicles_data(r, df_vehicles)
# df_all_government.set_index("Start_gate\End_gate", inplace=True)
# df_dict = df_all_government.to_dict(orient="index")
# producer = KafkaProducer(bootstrap_servers="localhost:9092")
# topic_name = "travel-data"

# x = Get_Vehicle_ID("Egyptain Cars\\Before Cropping\\1800.jpg")
# print(x)
# vtype = x.split("_")[1]
# ttl, code = calculate_ttl(10, vtype, "Giza", governorates_dict, r)
# min_key, end_gate, min_value = Calaulate_Lowest_Distance("Giza", df_dict)
# print(
#     f"carid : {x} with ttl :{ttl} with end code :{code} with {min_key}, {end_gate},{min_value}"
# )
# s = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# mes = f"id:{x},s_g:{'Giza'},e_g:{end_gate},D:{min_value},s_d: {s}"

# producer.send(topic_name, mes.encode("utf-8"))
# producer.flush()
# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
