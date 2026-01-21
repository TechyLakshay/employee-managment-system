# import mysql.connector
# from mysql.connector import Error


# def get_db_connection():
#     """
#     Creates and returns a MySQL database connection.
#     """
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="password",
#             database="employee_db"
#         )
#         return connection
#     except Error as error:
#         raise RuntimeError(f"Database connection failed: {error}")

import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",          
            password="password",  
            database="employee_db"  
        )
        return connection
    except Error as e:
        print("DB Connection Error:", e)
        return None
