from fastapi import FastAPI
from app.routes.employee_routes import router as employee_router
from app.logger import get_logger

app = FastAPI(title="Employee Management API")
logger = get_logger(__name__)

app.include_router(employee_router)


@app.get("/")
def health_check():
    logger.info("Succesfully establish connection to the API")
    return {"status": "Employee API is running"}


 