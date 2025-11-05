from pydantic import BaseModel
from typing import Optional


class SectionBase(BaseModel):
    name: str
    sport_type: str
    age_from: Optional[int] = None
    age_to: Optional[int] = None
    is_free: bool = False
    description: Optional[str] = None


class SectionCreate(SectionBase):
    pass


class SectionUpdate(BaseModel):
    name: Optional[str] = None
    sport_type: Optional[str] = None
    age_from: Optional[int] = None
    age_to: Optional[int] = None
    is_free: Optional[bool] = None
    description: Optional[str] = None


class SectionResponse(SectionBase):
    id: int

    class Config:
        from_attributes = True
