from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from db import models, database
from schemas import section as section_schemas
from typing import List, Optional

router = APIRouter(prefix="/sections", tags=["Секции (клиент)"])


@router.get("/", response_model=List[section_schemas.SectionResponse])
def get_sections(
    sport_type: Optional[str] = Query(None, description="Фильтр по виду спорта"),
    is_free: Optional[bool] = Query(None, description="Только бесплатные секции"),
    age: Optional[int] = Query(None, description="Фильтр по возрасту"),
    db: Session = Depends(database.get_db)
):
    """Получить список секций с фильтрацией"""

    query = db.query(models.Section)

    # Фильтр по виду спорта
    if sport_type:
        query = query.filter(models.Section.sport_type == sport_type)

    # Фильтр: только бесплатные
    if is_free is not None:
        query = query.filter(models.Section.is_free == is_free)

    # Фильтр по возрасту
    if age:
        query = query.filter(
            (models.Section.age_from <= age) | (models.Section.age_from == None),
            (models.Section.age_to >= age) | (models.Section.age_to == None)
        )

    sections = query.all()
    return sections


@router.get("/{section_id}", response_model=section_schemas.SectionResponse)
def get_section(section_id: int, db: Session = Depends(database.get_db)):
    """Получить информацию о секции"""

    from fastapi import HTTPException

    section = db.query(models.Section).filter(models.Section.id == section_id).first()

    if not section:
        raise HTTPException(status_code=404, detail="Секция не найдена")

    return section
