from pydantic import BaseModel
from typing import Optional

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    company_name: str
    salary: float
    manager_id: Optional[int] = None
    department_id: Optional[int] = None

class EmployeeList(BaseModel):
    employees: list[EmployeeCreate]
