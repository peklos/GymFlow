from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class UserClientBase(BaseModel):
    login: str
    password: str


class ClientBase(BaseModel):
    full_name: str
    phone: str
    email: EmailStr
    address: Optional[str] = None
    date_of_birth: Optional[date] = None


class UserRegister(BaseModel):
    user_data: UserClientBase
    client_data: ClientBase


class UserLogin(BaseModel):
    login: str
    password: str


class ClientUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    date_of_birth: Optional[date] = None


class ClientResponse(BaseModel):
    id: int
    user_id: Optional[int] = None
    full_name: str
    phone: str
    email: str
    address: Optional[str] = None
    date_of_birth: Optional[date] = None
    registration_date: date

    class Config:
        from_attributes = True
