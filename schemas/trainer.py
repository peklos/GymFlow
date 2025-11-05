from pydantic import BaseModel, EmailStr
from typing import Optional


class TrainerBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    address: Optional[str] = None
    specialization: Optional[str] = None


class TrainerCreate(TrainerBase):
    pass


class TrainerUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    specialization: Optional[str] = None


class TrainerResponse(TrainerBase):
    id: int

    class Config:
        from_attributes = True
