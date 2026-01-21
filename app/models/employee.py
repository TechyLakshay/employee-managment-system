from pydantic import BaseModel


class Employee(BaseModel):
    employee_id:  str    # now string
    name: str
    age: int
    department: str
    manager_name: str
    email: str
    salary: float = 0.0   # if you want salary optional, set default
