from pydantic import BaseModel
from typing import Optional
from datetime import time


class ScheduleBase(BaseModel):
    section_id: int
    trainer_id: int
    day_of_week: str
    start_time: time
    end_time: time
    location: Optional[str] = None


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleUpdate(BaseModel):
    section_id: Optional[int] = None
    trainer_id: Optional[int] = None
    day_of_week: Optional[str] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    location: Optional[str] = None


class ScheduleResponse(ScheduleBase):
    id: int
    section_name: Optional[str] = None
    trainer_name: Optional[str] = None
    time_start: Optional[str] = None
    time_end: Optional[str] = None

    class Config:
        from_attributes = True
