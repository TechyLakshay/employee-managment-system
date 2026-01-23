import mysql.connector
from mysql.connector import Error
from app.logger import get_logger

logger = get_logger(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="password",
            database="employee_db"
        )
        logger.info("Database connection established")
        return connection

    except Error as e:
        logger.error(f"Database connection failed: {e}")
        return None

