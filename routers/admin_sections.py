from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import models, database
from schemas import section as section_schemas
from typing import List

router = APIRouter(prefix="/admin/sections", tags=["Админ: Секции"])

@router.get("/", response_model=List[section_schemas.SectionResponse])
def get_all_sections(db: Session = Depends(database.get_db)):
    """Получить все секции"""
    sections = db.query(models.Section).all()
    return sections

@router.post("/", response_model=section_schemas.SectionResponse)
def create_section(section_data: section_schemas.SectionCreate, db: Session = Depends(database.get_db)):
    """Создать новую секцию"""
    new_section = models.Section(
        name=section_data.name,
        sport_type=section_data.sport_type,
        age_from=section_data.age_from,
        age_to=section_data.age_to,
        is_free=section_data.is_free,
        description=section_data.description
    )

    db.add(new_section)
    db.commit()
    db.refresh(new_section)

    return new_section

@router.patch("/{section_id}", response_model=section_schemas.SectionResponse)
def update_section(section_id: int, section_data: section_schemas.SectionUpdate, db: Session = Depends(database.get_db)):
    """Обновить секцию"""
    section = db.query(models.Section).filter(models.Section.id == section_id).first()

    if not section:
        raise HTTPException(status_code=404, detail="Секция не найдена")

    if section_data.name:
        section.name = section_data.name
    if section_data.sport_type:
        section.sport_type = section_data.sport_type
    if section_data.age_from is not None:
        section.age_from = section_data.age_from
    if section_data.age_to is not None:
        section.age_to = section_data.age_to
    if section_data.is_free is not None:
        section.is_free = section_data.is_free
    if section_data.description:
        section.description = section_data.description

    db.commit()
    db.refresh(section)

    return section

@router.delete("/{section_id}")
def delete_section(section_id: int, db: Session = Depends(database.get_db)):
    """Удалить секцию"""
    section = db.query(models.Section).filter(models.Section.id == section_id).first()

    if not section:
        raise HTTPException(status_code=404, detail="Секция не найдена")

    db.delete(section)
    db.commit()

    return {"message": "Секция удалена", "section_id": section_id}
