from fastapi import FastAPI
from app.routes.employee_routes import router as employee_router

app = FastAPI(title="Employee Management API")

app.include_router(employee_router)


@app.get("/")
def health_check():
    return {"status": "Employee API is running"}

# from fastapi import FastAPI
# from app.routes import employee # make sure this is the correct Employee model

# app = FastAPI(title="Employee Management API")

# app.include_router(employee)
# @app.get("/")
# def health_check():
#      return {"status": "Employee API is running"}
