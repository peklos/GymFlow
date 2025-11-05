from pydantic import BaseModel
from typing import Optional


class EmployeeLogin(BaseModel):
    login: str
    password: str


class EmployeeCreate(BaseModel):
    login: str
    password: str
    role_id: int


class EmployeeUpdate(BaseModel):
    login: Optional[str] = None
    password: Optional[str] = None
    role_id: Optional[int] = None


class EmployeeResponse(BaseModel):
    id: int
    login: str
    password: str
    role_id: int
    role_name: Optional[str] = None

    class Config:
        from_attributes = True
