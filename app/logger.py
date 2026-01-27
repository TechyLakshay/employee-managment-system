import os
import logging
import uuid
from dotenv import load_dotenv

load_dotenv()
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("employee_app.log"),
        logging.StreamHandler()
    ]
)



logger = logging.getLogger("employee_app")

def get_logger(name: str):
    return logging.getLogger(f"employee_app.{name}")

def generate_correlation_id():
    return str(uuid.uuid4())

# import os
# import logging

# # Read log level from environment (DEBUG / INFO / WARNING / ERROR)
# LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# LOG_FORMAT = (
#     "%(asctime)s | %(levelname)s | %(name)s | "
#     "user_id=%(user_id)s system_id=%(system_id)s correlation_id=%(correlation_id)s | "
#     "%(message)s"
# )

# class ContextFilter(logging.Filter):
#     def filter(self, record):
#         # default values so logging never crashes
#         record.user_id = getattr(record, "user_id", "NA")
#         record.system_id = getattr(record, "system_id", "employee_app")
#         record.correlation_id = getattr(record, "correlation_id", "NA")
#         return True

# logging.basicConfig(
#     level=LOG_LEVEL,
#     format=LOG_FORMAT,
#     handlers=[
#         logging.FileHandler("employee_app.log"),
#         logging.StreamHandler()
#     ]
# )

# logger = logging.getLogger("employee_app")

# def get_logger(name: str):
#      return logging.getLogger(f"employee_app.{name}")

# def generate_correlation_id():
#      return str(uuid.uuid4())


