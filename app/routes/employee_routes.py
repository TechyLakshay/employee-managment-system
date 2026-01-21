from fastapi import APIRouter
from app.models.employee import Employee
from app.services.employee_service import (
    create_employee,
    get_all_employees,
    update_employee,
    delete_employee,
)

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/")
def add_employee(employee: Employee):
    return create_employee(employee)


@router.get("/")
def list_employees():
    return get_all_employees()


@router.put("/{employee_id}")
def modify_employee(employee_id: str, employee: Employee):
    return update_employee(employee_id, employee)


@router.delete("/{employee_id}")
def remove_employee(employee_id: str):
    return delete_employee(employee_id)
