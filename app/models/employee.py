from pydantic import BaseModel, EmailStr, Field


class Employee(BaseModel):
    employee_id:  str    
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=18, le=60) 
    department: str
    manager_name: str
    email: EmailStr
    salary: float = 0.0 
    
 
