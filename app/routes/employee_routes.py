
from fastapi import APIRouter
from app.models.employee import Employee
from app.logger import generate_correlation_id
from app.services.employee_service import (
    create_employee,
    get_all_employees,
    update_employee,
    delete_employee,
)

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/")
def add_employee(employee: Employee):
    correlation_id = generate_correlation_id()
    return create_employee(employee, correlation_id=correlation_id)


@router.get("/")
def list_employees():
    correlation_id = generate_correlation_id()
    return get_all_employees(correlation_id=correlation_id)


@router.put("/{employee_id}")
def modify_employee(employee_id: str, employee: Employee):
    correlation_id = generate_correlation_id()
    return update_employee(employee_id, employee, correlation_id=correlation_id)


@router.delete("/{employee_id}")
def remove_employee(employee_id: str):
    correlation_id = generate_correlation_id()
    return delete_employee(employee_id, correlation_id=correlation_id)
    
