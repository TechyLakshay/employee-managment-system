
from fastapi import FastAPI
from app.routes.employee_routes import router as employee_router
from app.observability.correlation import CorrelationIdMiddleware
from app.observability.logger import setup_logging, get_logger
from app.observability import setup_observability

#  Setup logging 
setup_logging()

app = FastAPI(title="Employee Management API")

# Middleware
app.add_middleware(CorrelationIdMiddleware)

# OpenTelemetry
setup_observability(app)

# Logger
logger = get_logger(__name__)

# Routes
app.include_router(employee_router)

@app.get("/")
def health_check():
    logger.info("Successfully established connection to the API")
    return {"status": "Employee API is running"}
