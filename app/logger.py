import os
import logging
import uuid
from dotenv import load_dotenv


load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("employee_app.log"),
        logging.StreamHandler()
    ],
    force=True   
)

logger = logging.getLogger("employee_app")

def get_logger(name: str):
    return logging.getLogger(f"employee_app.{name}")

def generate_correlation_id():
    return str(uuid.uuid4())


