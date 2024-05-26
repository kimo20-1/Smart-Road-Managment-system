from APP.Flask_Functions import check_type, hash_password
from Config.config import *
from MYSQL import DB_Connection


conn, cursor = DB_Connection(
    MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
)


def get_driver_info(name):
    if conn and cursor:
        try:

            query_driver = "SELECT * FROM drivers WHERE name = %s"
            cursor.execute(query_driver, (name,))
            driver_data = cursor.fetchone()

            if driver_data:

                driver_id = driver_data[0]

                query_travels = "SELECT Travel_id, Start_Gate, End_Gate, Distance, Start_Travel_Date, End_Travel_Date FROM travels WHERE Vehicle_id IN (SELECT id FROM vehicles WHERE driver_id = %s)"
                cursor.execute(query_travels, (driver_id,))
                travel_data = cursor.fetchall()

                query_violations = "SELECT Car_ID, Start_Gate, End_Gate, Start_Date, Arrival_End_Date, Payment_Status FROM violations WHERE Car_id IN (SELECT Number_type FROM vehicles WHERE driver_id = %s) AND Payment_Status = 'unpaid'"
                cursor.execute(query_violations, (driver_id,))
                violation_data = cursor.fetchall()

                travels = []
                for travel in travel_data:
                    travels.append(
                        {
                            "Travel_ID": travel[0],
                            "Start_Gate": travel[1],
                            "End_Gate": travel[2],
                            "Distance": travel[3],
                            "Start_Travel_Date": travel[4],
                            "End_Travel_Date": travel[5],
                        }
                    )

                violations = []
                for violation in violation_data:
                    violations.append(
                        {
                            "Travel_ID": violation[0],
                            "Start_Gate": violation[1],
                            "End_Gate": violation[2],
                            "Travel_Start_Date": violation[3],
                            "Travel_Arrival_Date": violation[4],
                            "Payment_Status": violation[5],
                        }
                    )

                return travels, violations
            else:
                return None, None

        except Exception as e:
            print(f"Error fetching travel and violation data: {e}")

    return None, None


travels, violations = get_driver_info("Mohamed Ali")
print(violations)
print(travels)
# def login():
#     # if request.method == "POST":
#     email = "Mohamed_Ali@gmail.com"
#     name = "Mohamed Ali"
#     password = hash_password("kareem_hani")
#     types = check_type(email)
#     if types == "admin":
#         cursor.execute(
#             "SELECT * FROM admins WHERE email = %s AND password = %s",
#             (email, password),
#         )
#         user = cursor.fetchone()
#         if user:
#             print("it is user")
#         else:
#             print("it is not user")
#     elif types == "driver":
#         cursor.execute(
#             "SELECT * FROM drivers WHERE email = %s AND password = %s",
#             (email, password),
#         )
#         user = cursor.fetchone()
#         if user:
#             print("it is admin")
#         else:
#             print("it is not driver")
#     else:
#         print("Invalid email or password. Please try again.")


# login()
