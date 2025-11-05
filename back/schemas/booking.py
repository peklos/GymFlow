from pydantic import BaseModel
from typing import Optional
from datetime import date


class BookingBase(BaseModel):
    section_id: int
    child_full_name: Optional[str] = None
    child_age: Optional[int] = None


class BookingCreate(BookingBase):
    pass


class BookingUpdate(BaseModel):
    status: str


class BookingResponse(BaseModel):
    id: int
    client_id: int
    section_id: int
    booking_date: date
    status: str
    child_full_name: Optional[str] = None
    child_age: Optional[int] = None

    class Config:
        from_attributes = True
