from pydantic import BaseModel
from typing import Optional
from datetime import date


class AttendanceBase(BaseModel):
    booking_id: Optional[int] = None
    schedule_id: int
    visit_date: date
    was_present: bool = False


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(BaseModel):
    was_present: bool


class AttendanceResponse(AttendanceBase):
    id: int

    class Config:
        from_attributes = True
