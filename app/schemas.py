from pydantic import BaseModel, field_validator
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str
    datetime: str
    department_id: Optional[int] = None
    job_id: Optional[int] = None

    @field_validator('job_id', 'department_id', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == '':
            return None
        return v

class PostEmployee(BaseModel):
    id: int
    name: str
    datetime: str
    department_id: int
    job_id: int

    class Config:
        from_attributes = True

class DepartmentsCreate(BaseModel):
    department: str

class PostDepartments(BaseModel):
    department: str